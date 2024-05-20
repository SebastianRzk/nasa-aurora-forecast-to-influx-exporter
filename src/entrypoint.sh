#!/bin/bash

echo "Aurora exporter has been started";
declare -p | grep -Ev 'BASHOPTS|BASH_VERSINFO|EUID|PPID|SHELLOPTS|UID' > /container.env;

# Setup a cron schedule
echo "SHELL=/bin/bash
BASH_ENV=/container.env
0 */4  * * * source /venv/bin/activate && python3 /src/main.py
# This extra line makes it a valid cron" > scheduler.txt;

source venv/bin/activate && python3 /src/main.py

crontab /scheduler.txt;
crond -f;
