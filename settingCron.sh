#!/bin/bash
# создать скрипт updateGit.sh
# добавить ssh ключ в ~/.ssh/
chmod +x updateGit.sh
chmod =600 ~/.ssh/id_rsa_gitPull
crontab -l > mycron
echo "0 21 * * * /home/pi/project/telegramBot_thermobox/updateGit.sh" > mycron
crontab mycron
rm mycron
