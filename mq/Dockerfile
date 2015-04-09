FROM ubuntu:latest

MAINTAINER Roman Orlov fooote@gmail.com

ENV ACTIVEMQ_HOME /opt/activemq
ENV ACTIVEMQ_VERSION 5.11.1

RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886
    
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections  && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections  && \
    DEBIAN_FRONTEND=noninteractive && \
    apt-get update && apt-get install -y \
    oracle-java7-installer

COPY activemq-$ACTIVEMQ_VERSION.deb /root/

RUN dpkg -i /root/activemq-$ACTIVEMQ_VERSION.deb

RUN useradd -d $ACTIVEMQ_HOME activemq && \
    chown activemq:activemq $ACTIVEMQ_HOME -R

USER activemq

EXPOSE 61616 8161


ENTRYPOINT ["/bin/bash", "-c", "$ACTIVEMQ_HOME/bin/activemq console"]
