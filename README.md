# telegramBot_door
Телеграм бот для проекта ThermoPost
# Функционал
0. Подписка на получение уведомлений от устройства \subscribe
0. Отписка от рассылки unsubscribe
0. Для подписынных пользователей выводится фотография и текст
## Команды
0. /subscribe - подписаться, необходимо ввести пароль он распологается в config
0. /unsubscribe - отписаться
0. /ping - проверить работаспособность системы (проверка камеры, пирометра, тепловизор, растояние)

## Установка:
0. mkdir telegramBot_door && cd telegramBot_door
0. python3 -m venv .env
0. source .env/bin/activate
0. pip install -r requirements.txt
0. Второй вариант, если какие либо пакеты не могут поставится: cat requirements.txt | xargs -n 1 pip install
0. Запуск: pyhton aiogram_bot.py

## Зависимости
pip install aiogram
pip install telebot
pip install busio
pip install adafruit-circuitpython-bme280
pip install opencv-python

## ДЛя отладки 
Тестовый стенд для телеграм бота: 
бот: @cmitbot
key = '122098803:AAE5b0l6s9XRVLvIn8-PIepNjOXwWff3r_8'

