#!/bin/bash
set -e
echo > /var/log/yandexer/monitor.log

while true; do
    xvfb-run /monitor.py >> /var/log/yandexer/monitor.log
    sleep 30
done
exec "$@"