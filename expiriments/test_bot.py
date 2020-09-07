'''
t.me/Institute_digit_door_bot
'''
token = '1350151278:AAFiJZMSdAT5DTNNfUA3C-jVdx8RQDwI3Vg'
IP_DOOR = '192.168.0.196'
POST_DOOR = 9091
DEBUG = False

import logging
import socket
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


def send_message(message):
    '''
    Отправляет команду на дверь
    :param message:
    :return:
    '''
    if not DEBUG:
        sock = socket.socket()
        sock.connect((IP_DOOR, POST_DOOR))

        sock.send(bytes(message, encoding='utf8'))
        data = sock.recv(1024)

        if data == bytes(message, encoding='utf8'):
            print("Команда дошла успешно")
        else:
            print("Что то пошло не так")

        sock.close()
    else:
        print("Команда отправленная на дверь {}".format(message))

def open_door(update, context):
    '''
    Открыть дверь
    :param update:
    :param context:
    :return:
    '''
    send_message('open')
    update.message.reply_text('open_door')

def disable_door(update, context):
    '''
    ОТключить замок
    :param update:
    :param context:
    :return:
    '''
    send_message('disable_door')
    update.message.reply_text('disable_door!')

def enable_door(update, context):
    '''
    Активировать замок
    :param update:
    :param context:
    :return:
    '''
    send_message('enable_door')
    update.message.reply_text('enable_door!')

def help_command(update, context):
    '''

    :param update:
    :param context:
    :return:
    '''
    update.message.reply_text('/open_door')

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main():
    """Start the bot."""
    # Создайте Updater и передайте ему токен вашего бота.
    # Обязательно установите use_context = True, чтобы использовать новые контекстные обратные вызовы
    # После версии 12 в этом больше не будет необходимости
    updater = Updater(token, use_context=True)

    # Получите диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # по разным командам - ответ в Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(CommandHandler("open_door", open_door))
    dp.add_handler(CommandHandler("disable_door", disable_door))
    dp.add_handler(CommandHandler("enable_door", enable_door))

    # по некоманде, т.е. сообщение - повторить сообщение в Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запустить бота
    updater.start_polling()

    # Запускать бота, пока вы не нажмете Ctrl-C или процесс не получит SIGINT,
    # SIGTERM или SIGABRT. Это следует использовать в большинстве случаев, поскольку
    # start_polling () не блокирует и корректно останавливает бота.
    updater.idle()


if __name__ == '__main__':
    main()