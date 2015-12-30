__author__ = 'huyansheng'
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("./index.html"))
print soup.title
print soup.head
print type(soup.a)
print "--------------"
print soup.p.attrs
print soup.p.string
print "--------------"
print soup.body.contents
print "--------------"
for child in soup.body.children:
    print child

print "--------------"
for child in soup.body.descendants:
    print child

