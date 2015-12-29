#!/user/bin/python
# -*- coding: utf-8 -*-
__author__ = 'huyansheng'
import urllib2
import urllib
from bs4 import BeautifulSoup
page =4
url = 'http://www.qiushibaike.com/hot/page/'+str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
headers = {"User-Agent":user_agent}
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response.read())
    for item in  soup.select('.content'):
        if type(item.string) == 'bs4.elment.Comment':
            print item.string
        else:
            print item
except urllib2.URLError, e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reason'):
        print e.reason