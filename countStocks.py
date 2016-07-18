# _*_ coding: utf-8 _*_
import os,sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
goalFile = open("output1.txt","r")
fileName = open("allStocks.txt","r")
outFile  = open("countStocks.txt","w")
count=dict()

for j in fileName.readlines():
	count[j[:-1]]=0
	
for i in goalFile.readlines():
	fileName.seek(0)
	for j in fileName.readlines():
		if (i.find(j[:-1])!=-1):
			count[j[:-1]]+=1

goalFile.close()

goalFile = open("output2.txt","r")

for i in goalFile.readlines():
	fileName.seek(0)
	for j in fileName.readlines():
		if (i.find(j[:-1])!=-1):
			count[j[:-1]]+=1

for key,x in count.items():
	outFile.write(key+"\t"+str(x)+"\n")

outFile.close()
fileName.close()
goalFile.close()
