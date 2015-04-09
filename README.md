#Устновка

Если это пустая Ubuntu 14.04, то нужно поставить git:
```
apt-get update && apt-get install -y git
```
Установить docker (не очень безопасный способ, но быстрый):
```
wget -qO- https://get.docker.com/ | sh
```
Установить fig:
```
curl -L https://github.com/docker/fig/releases/download/1.0.1/fig-`uname -s`-`uname -m` > /usr/local/bin/fig; chmod +x /usr/local/bin/fig
```
Клон репозитория:
```
git clone https://github.com/fote/yandextask
```
И запуск:
```
cd yandextask && fig up -d
```

Из контейнера с приложением наружу смотрит порт 8080, соответственно, URL для проверки:
```
http://<host_ip>:8080/camelot/
```


#Описание

После запуска будут собраны 4 docker-контейнера:
* PostgreSQL
* AcriveMQ
* Yandexer
* Monitor

```
# docker ps
CONTAINER ID        IMAGE                        COMMAND                CREATED             STATUS              PORTS                               NAMES
20bd432aaf6c        yandextask_monitor:latest    "/run_monitor.sh"      7 minutes ago       Up 7 minutes                                            yandextask_monitor_1    
583bdcd12a54        yandextask_yandexer:latest   "/yandexer_entrypoin   13 minutes ago      Up 13 minutes       18082/tcp, 0.0.0.0:8080->8080/tcp   yandextask_yandexer_1   
28588d4d22f6        postgres:latest              "/docker-entrypoint.   13 minutes ago      Up 13 minutes       5432/tcp                            yandextask_pg_1         
af2447960cd9        yandextask_mq:latest         "/bin/bash -c '$ACTI   13 minutes ago      Up 13 minutes       61616/tcp, 8161/tcp                 yandextask_mq_1 
```

Yandexer прилинкован к postgresql и activemq. Конфиг для приложения пишется в entrypoint-е, на основе переменных, переданных при линковке.

Monitor прилинкован к yandexer. Папка logs является общей точкой монтирования для yandexer-а и monitor-а.

