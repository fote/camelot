#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dryscrape, sys, os, re, time
from bs4 import BeautifulSoup

PLUGINS = ['INPUT', 'fetcher', 'result-saver','collector']
LOGFILE = '/var/log/yandexer/yandexer.log'

#берем переменную полученную при линковке к аппу, меняем tcp на http добавляем /camelot/
try:
    YANDEXER_URL = os.environ["YANDEXER_PORT"].replace('tcp','http') + '/camelot/'
    YANDEXER_PLUGINS_URL = YANDEXER_URL + 'pluginslist'
except:
    print 'Can\'t find YANDEXER_PORT env var. You should use --link=<yandexer_container>:yandexer'
    sys.exit(1)



def get_html(url):
    try:
        session = dryscrape.Session()
        session.visit(url)
        html = session.body()
        return html
    except:
        return 'error'

def is_dashboard_ok(html):
    if html == 'error':
        print 'Dashboard: ERROR while getting dashboard page'
        return 2    
    soup = BeautifulSoup(html)
    if soup.find_all('div', class_='collector widget ng-scope'):
        print 'Dashboard: OK'
        return 1
    else:
        print 'Dashboard: CRITICAL'
        return 0


def is_plugins_ok(html):
    if html == 'error':
        print 'Dashboard: ERROR while getting plugins page'
        return 2
    soup = BeautifulSoup(html)
    plugins_tree = soup.find('div', class_='tree well')
    for p in PLUGINS:
        m = re.search(str(p), str(plugins_tree), re.DOTALL)
        if m:
            print 'Plugin ' + p + ': OK'
        else:
            print 'Plugin ' + p + ': CRITICAL'

def watch_for_startup_errors(logfile):
    logfile.seek(0,2)
    while True:
        line = logfile.readline()
        if not line:
            time.sleep(0.2)
            continue
        if ('ERROR' in line) or ('error' in line):
            yield line
        if 'Started @' in line:
            break

def main():
    #print "==================Startup errors:=================="
    #logfile = open("/var/log/yandexer/yandexer.log","r")
    #loglines = watch_for_startup_errors(logfile)
    #for line in loglines:
    #   print line,

    print '==================' + time.strftime("%Y-%m-%d %H:%M:%S") + '=================='
    dashboard_page = get_html(YANDEXER_URL)
    is_dashboard_ok(dashboard_page)
        
    plugins_page = get_html(YANDEXER_PLUGINS_URL)
    is_plugins_ok(plugins_page)

    
if __name__ == '__main__':
    main()

