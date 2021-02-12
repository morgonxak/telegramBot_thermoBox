#!/bin/bash
git remote rm origin
git remote add origin git@github.com:morgonxak/telegramBot_thermoBox.git
git config --global user.email "thermobox@mail.com"
git config --global user.name "thermobox"
mkdir ~/.ssh/
chmod +x settingCron.sh

