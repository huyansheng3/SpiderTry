#!/user/bin/python
#coding= utf-8
__author__ = 'huyansheng'
import urllib2
import urllib
import os
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
        for item in  soup.select('.content'):  #每个item就是一个段子
            for string in item.stripped_strings:
                result+=string
                result+="\n"     #每个段子存在很多行
            result+="\n"
        print("成功获取第%d页的段子" % page)
        return result

    except urllib2.URLError, e:
        if hasattr(e,'code'):
            print e.code
        if hasattr(e,'reason'):
            print e.reason

def main():
    while True:
        count = 0
        all_stories = ''
        want_page = raw_input("请输入你想看多少页的段子：")
        if want_page.isdigit():
            for i in range(1,int(want_page)):
                all_stories+=getStories(count,i)
            #file_name = os.path.normpath(u'./糗事百科.txt')   #更为正规的写法，可适应不同的系统
            file_name = u"./糗事百科.txt"   #在保存的时候使用的是unicode编码，而本文默认采用的是utf-8的编码，所以就会导致乱码，明确指定unicode编码即可解决问题
            output = file(file_name,"w")
            output.writelines(all_stories.encode("utf-8"))
            output.close()
            print("------------------")
            print("所有段子已写入糗事百科.txt，开始开心的看段子吧")
        else:
            print("请输入整数")
if "__main__" == main():
    main()