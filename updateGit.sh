#!/bin/bash
eval `ssh-agent -s`
ssh-add ~/.ssh/id_rsa_gitPull
cd /home/pi/project/telegramBot_thermobox/
git fetch
git merge  --no-commit origin/master --allow-unrelated-histories
#svn stuff
kill $SSH_AGENT_PID
