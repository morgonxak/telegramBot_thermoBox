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

## Для отладки 
Тестовый стенд для телеграм бота: 
бот: @cmitbot
key = '122098803:AAE5b0l6s9XRVLvIn8-PIepNjOXwWff3r_8'

## Настройка коробки для обновлений через гит
0. Тестировать обновляется ли система в ветке testupdate она сделана специально для этого
0. Запустить settingGitUpdate.sh (bash settingGitUpdate.sh)
0. Поместить ssh ключ по пути ~/.ssh
0. Выполнить команду git fetch
0. Выполнить команду git merge origin master --allow-unrelated-histories
0. Устранить появившиеся конфликты
0. Запустить settingCron.sh (./settingCron.sh)
0. Командой crontab -e настроить нужное расписание обновлений
0. Дождаться выполнения cron расписания и выполнить git status, если требуется коммит, то добавить строку git commit -m"update" после git merge в updateGit.sh

### Скрипт settingGitUpdate.sh
Так как устройства изначально не настроены для работы с гитом, данный скрипт автоматически создает remote через ssh ссылку, создает локальный профиль git, добавляет папку .ssh

### Скрипт settingCron.sh
0. Делает исполняемым скрипт updateGit.sh
0. Изменяет права доступа к ssh ключу
0. Создает расписание в cron

### Скрипт updateGit.sh
0. Создает ssh agent
0. Добавялет в него ssh ключ
0. Изменяет текущую директорию на директорию с телеграм ботом
0. Получает данные с git и выполняет слияние
0. Уничтожает ssh agent
