from moduls import config, len
import logging
import asyncio
import subprocess

from aiogram import Bot, Dispatcher, executor, types
from moduls.dataBase import DATA_BASE_TELEGRAM_BOT
from moduls.config import *
from aiogram.types import InputFile
# from moduls.report.create_html_report import report_1

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

db = DATA_BASE_TELEGRAM_BOT(path_database_file, path_save_image)

userSub = False
# Команда активации подписки


@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    global userSub
    userSub = True
    await message.answer("введите код")


# Команда отписки
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    global userSub
    if not db.subscriber_exists(message.from_user.id):
        # если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
        db.add_subscriber(message.from_user.id, False)
        await message.answer("Вы итак не подписаны.")
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, False)
        userSub = False
        await message.answer("Вы успешно отписаны от рассылки.")


# отчет о работоспособности устройства
@dp.message_handler(commands=['ping'])
async def pingm(message: types.Message):
    await message.answer("отчет о работоспособности")
    # проверяет тепловизор(68 или 69)
    therm = subprocess.Popen("sudo i2cdetect -y 1 | grep 68", shell=True, stdout=subprocess.PIPE)
    out = therm.stdout.read()

    # await message.answer("тепловизор: "+str(out))
    if out:
        await message.answer("тепловизор работает")
    else:
        therm = subprocess.Popen("sudo i2cdetect -y 1 | grep 69", shell=True, stdout=subprocess.PIPE)
        out = therm.stdout.read()
        # await message.answer("тепловизор: " + str(out))
        if out:
            await message.answer("тепловизор работает")
        else:
            await message.answer("тепловизор не работает")

    # проверяет нижний пирометр(5a)
    pyro = subprocess.Popen("sudo i2cdetect -y 1 | grep 5a", shell=True, stdout=subprocess.PIPE)
    out = pyro.stdout.read()
    # await message.answer("пирометр: "+str(out))
    if out:
        await message.answer("нижний пирометр работает")
    else:
        await message.answer("нижний пирометр не работает")

    # проверяет камеру
    cam = subprocess.Popen("sudo vcgencmd get_camera | grep detected=1", shell=True, stdout=subprocess.PIPE)
    out = cam.stdout.read()
    # await message.answer("камера: "+str(out))
    if out:
        await message.answer("камера работает")
    else:
        await message.answer("камера не работает")

    # проверяет дальнометр
    if len.len():
        await message.answer("дальнометр работает")
    else:
        await message.answer("дальнометр не работает")






# Команда отписки
# @dp.message_handler(commands=['report'])
# async def get_report(message: types.Message):
#     if (not db.subscriber_exists(message.from_user.id)):
#         # если юзера нет в базе
#         await message.answer("Вы не авторизированны.")
#     else:
#         pass
#         # если он уже есть
#         # id = message.from_user.id
#         #
#         # period, data_db = db.get_data_for_report_1()
#         # print(period, data_db)
#         # rath_pdf_file = report_1(period, data_db, '/home/dima/PycharmProjects/telegramBot_thermobox/moduls/report/temp')
#         #
#         # agenda = InputFile(rath_pdf_file, filename="{}_{}.pdf".format(period[0].replace(' ', '_'), period[1].replace(' ', '_')))
#         # await bot.send_document(id, agenda)
#
# @dp.message_handler(commands=['menu'])
# async def get_menu(message: types.Message):
#     markup = types.ReplyKeyboardMarkup(row_width=1)
#     itembtn1 = types.KeyboardButton('Получить отчет за неделю')
#
#     markup.add(itembtn1)
#     chat_id = message.chat.id
#
#     await bot.send_message(chat_id, "Выберете пункт:", reply_markup=markup)


import os
async def send_out_sick():
    sick = db.get_sick_people()
    if not sick is None:
        data_time, name_image, recalculated = sick

        subscriptions = db.get_subscriptions()

        date_time = data_time[:data_time.rfind('.')]  #2020-12-03 04:00:14.183183
        text = "Обнаружен посетитель с повышенной температурой "#.format(recalculated)
        image_path = os.path.join(path_log, name_image+'.jpg')

        # with open(image_path, 'rb') as photo:
        for s in subscriptions:
            with open(image_path, 'rb') as photo:
                print("отправить ", s)
                await bot.send_photo(
                    s[1],
                    photo,
                    caption=str(date_time) + "\n" + text,
                    disable_notification=True
                )

def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(DELAY, repeat, coro, loop)


# проверка введенного пароля
@dp.message_handler(content_types=["text"])
async def enterpass(message: types.Message):
    global userSub
    if userSub and message.text == config.passw:
        if not db.subscriber_exists(message.from_user.id):
            # если юзера нет в базе, добавляем его
            db.add_subscriber(message.from_user.id)
        else:
            # если он уже есть, то просто обновляем ему статус подписки
            db.update_subscription(message.from_user.id, True)
        await message.answer(
            "Вы успешно подписались на рассылку!\nЖдите, скоро выйдут новые обзоры и вы узнаете о них первыми =)")
        userSub = False
    elif userSub and message.text != config.passw:
        await message.answer("Код неверен")

# запускаем лонг поллинг
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_later(DELAY, repeat, send_out_sick, loop)

    executor.start_polling(dp, skip_updates=True)