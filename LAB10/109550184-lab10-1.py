from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

#Open
url='https://www.goldenhorse.org.tw/awards/nw'
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser') 

'''
content > div:nth-child(5) > div.col-lg-8-5.col-xs-10.content-page > div 
> div.col-xs-9 > table:nth-child(2) > tbody > tr:nth-child(1) > th
'''

values=soup(class_="table special award")
for value in values:
    value=value('tr')
    for val in value:
        results=val('th')
        for result in results:
            print(result.text)#ANS