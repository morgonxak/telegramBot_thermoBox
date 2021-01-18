from moduls import config
import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from moduls.dataBase import DATA_BASE_TELEGRAM_BOT
from moduls.config import *
from aiogram.types import InputFile


# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

db = DATA_BASE_TELEGRAM_BOT(path_database_file, path_save_image)

# Команда активации подписки
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(message.from_user.id)
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, True)

    await message.answer(
        "Вы успешно подписались на рассылку!\nЖдите, скоро выйдут новые обзоры и вы узнаете о них первыми =)")


# Команда отписки
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        # если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
        db.add_subscriber(message.from_user.id, False)
        await message.answer("Вы итак не подписаны.")

    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, False)
        await message.answer("Вы успешно отписаны от рассылки.")


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

# запускаем лонг поллинг
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_later(DELAY, repeat, send_out_sick, loop)

    executor.start_polling(dp, skip_updates=True)