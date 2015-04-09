FROM ubuntu:latest

MAINTAINER Roman Orlov fooote@gmail.com
WORKDIR /root

RUN apt-get update && apt-get install -y \
    libqt4-dev \
    libqtwebkit-dev \
    qt4-qmake \
    build-essential \
    python-lxml python-pip \
    git \
    xvfb
    
RUN git clone https://github.com/niklasb/dryscrape.git dryscrape && \
    cd dryscrape && \
    pip install -r requirements.txt && \
    pip install beautifulsoup4 && \
    python setup.py install

COPY monitor.py /
COPY run_monitor.sh /
ENTRYPOINT ["/run_monitor.sh"]
