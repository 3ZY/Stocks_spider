#coding=utf-8
#抓内容
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
inputFile = open('urlyes.txt','r')
outputFile = open('output.txt','a+')
lines=inputFile.readlines()
res_data=dict()
for i in range(20000,30000):#总共0-59902
	print i
	html = getHtml(lines[i][:-1])#获得文件中第i行链接
	soup = BeautifulSoup(html);#转换为bs
	#获取class=art_title的div中的文本，标题
	content = soup.find('div',class_="art_title")
	res_data['title']=content.getText()
	#获取日期
	content = soup.find('span',class_="gray")
	res_data['date']=content.getText()
	#获取内容
	content = soup.find('div',class_='art_context')
	res_data['summary']=content.getText()
	#写到文件
	outputFile.write('Title:'+res_data['title'])
	outputFile.write('Date:\n'+res_data['date'])
	outputFile.write('\nSummary:'+res_data['summary'])
	outputFile.write('--=--=--\n')
inputFile.close()
outputFile.close()
	

