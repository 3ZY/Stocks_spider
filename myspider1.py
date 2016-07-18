#coding=utf-8
#抓链接
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import urllib
from bs4 import BeautifulSoup
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
outputFile = open("urlyes.txt","a+")
for i in range(513,1000):
	print i
	xxx=1716-i
	#获取源代码
	html = getHtml("http://stock.hexun.com/stocknews/index-"+str(xxx)+".html")
	
	soup = BeautifulSoup(html)#转换成bs
	content = soup.find('div',class_="temp01")#bstag
	#获取所有目标链接
	links = content.find_all('a',href=re.compile(r'http://stock.hexun.com/(\d+)-(\d+)-(\d+)/(\d+).html'))
	for link in links:
		outputFile.write(link['href'])
		outputFile.write('\n')
outputFile.close()

