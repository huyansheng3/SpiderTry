#!/user/bin/python
# -*- coding: utf-8 -*-
__author__ = 'huyansheng'
import urllib2
import urllib
from bs4 import BeautifulSoup


def getStories(count,page):
    url = 'http://www.qiushibaike.com/hot/page/'+str(page)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    headers = {"User-Agent":user_agent}
    result = ""
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        soup = BeautifulSoup(response.read())
        for item in  soup.select('.content'):
            for string in item.stripped_strings:
                result+=string
                result+="\n"
                print result
                print str(page)
            result+="\n"
        return result

    except urllib2.URLError, e:
        if hasattr(e,'code'):
            print e.code
        if hasattr(e,'reason'):
            print e.reason

def main():
    count = 0
    all_stories = ''
    for i in range(1,100):
        all_stories+=getStories(count,i)

    output = file("./qiushibaike.txt","w")
    output.writelines(all_stories.encode("utf-8"))
    output.close()
if "__main__" == main():
    main()