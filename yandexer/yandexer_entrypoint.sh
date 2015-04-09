#!/bin/bash
set -e
CONF_FILE="/opt/yandexer/yandexer.properties"
LOG_FILE="/var/log/yandexer/yandexer.log"

echo "jms.broker.list=(${MQ_PORT_61616_TCP})?randomize=false&priorityBackup=true" > "$CONF_FILE"
echo "yandexer.jdbc.url=jdbc:postgresql://${PG_PORT_5432_TCP_ADDR}:${PG_PORT_5432_TCP_PORT}/${PG_ENV_POSTGRES_USER}" >> "$CONF_FILE"
echo "yandexer.jdbc.user=${PG_ENV_POSTGRES_USER}" >> "$CONF_FILE"
echo "yandexer.jdbc.password=${PG_ENV_POSTGRES_PASSWORD}" >> "$CONF_FILE"

cd /opt/yandexer
export MAVEN_OPTS="-XX:MaxPermSize=512m -Xmx2048m -Xbootclasspath/a:."
mvn clean compile camelot-test:run > "$LOG_FILE"


exec "$@"