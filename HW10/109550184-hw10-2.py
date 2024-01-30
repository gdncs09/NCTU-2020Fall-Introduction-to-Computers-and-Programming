import urllib.request, urllib.parse, urllib.error
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import re
url="https://www.ptt.cc/bbs/HCI/index20.html"
#Main
#req=Request(url,headers={'User-Agent': 'Mozilla/5.0'})
#html=urlopen(req).read()
webpage=urllib.request.urlopen(Request(url,headers={'User-Agent': 'Mozilla/5.0'})).read().decode("utf-8")
soup=BeautifulSoup(webpage,"html.parser")

'''
<div class="title">
<a href="/bbs/MobileComm/M.1539248247.A.3CF.html"> Re: [請益] 請問我能申請到
中上的美國 HCI 研究所嗎</a>
</div>
'''
#1 Find some line 
tags=soup("div",class_="title")
titles=re.findall('<a href="(.*?)">(.*?)</a>',str(tags)) #Find ('(.*?)','(.*?)')
for title in titles: #Output answer
    print(title[0],title[1])

#2 Count category
categorys=re.findall('(\[.*?\])',str(tags)) #Find 
category_count=dict()
for category in categorys:
    category_count[category]=category_count.get(category,0)+1 #Count
for category,count in category_count.items(): #Output answer
    print(category,':',count)
    

