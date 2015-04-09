FROM ubuntu:latest

MAINTAINER Roman Orlov fooote@gmail.com

WORKDIR /root

RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886

RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections  && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections  && \
    DEBIAN_FRONTEND=noninteractive && \
    apt-get update && apt-get install -y \
    oracle-java7-installer \
    git \
    libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev #для phantomjs

#приносим в образ deb-пакеты
COPY *.deb /root/

#установка maven
RUN dpkg -i /root/maven-3.2.5.deb

#ставим phantomjs
RUN dpkg -i /root/phantomjs-1.9.8.deb

#клон исходников
RUN mkdir /opt/yandexer && git clone https://github.com/yandex-qatools/camelot-yandexer.git /opt/yandexer

#убираем кэши и инсталяторы
RUN rm -rf /var/cache/oracle-jdk8-installer  && \
    apt-get clean  && \
    rm -rf /var/lib/apt/lists/* /root/*.deb

EXPOSE 8080 18082
COPY yandexer_entrypoint.sh /
ENTRYPOINT ["/yandexer_entrypoint.sh"]