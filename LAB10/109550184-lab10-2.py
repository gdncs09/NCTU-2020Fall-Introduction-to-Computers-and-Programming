from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import re

url='https://www.goldenhorse.org.tw/awards/nw'
html=urllib.request.urlopen(url).read().decode()
soup=BeautifulSoup(html,'html.parser') 

'''
content > div:nth-child(5) > div.col-lg-8-5.col-xs-10.content-page > div 
> div.col-xs-9 > table:nth-child(22) > tbody > tr:nth-child(2) 
> td:nth-child(2) > a
'''

values=soup(class_="table special award")
for value in values:
    if value.find('th').string == "最佳原創電影歌曲 ":#find
        details=value
        break

detail1=[]#詞
detail2=[]#曲
detail3=[]#唱

def Init(a):
    detail=[]
    for tmp in a:
        tmp=tmp.split(" : ")[1]
        tmp=tmp.replace('<u>','')
        tmp=tmp.replace('<br/>','')
        detail.append(tmp)
    return detail
    
ci=re.findall("詞<\/u>\s:\s.+?<u>",str(details))#詞
detail1=Init(ci)

qu=re.findall("曲<\/u>\s:\s.+?<u>",str(details))#曲
detail2=Init(qu)

chang=re.findall("唱<\/u>\s:\s.+?<br\/>",str(details))#唱
detail3=Init(chang)

movie_names=re.findall("\(.+?\)",str(details))

for i in range(5):
    print(movie_names[i])
    print(detail1[i])
    print(detail2[i])
    print(detail3[i])
    
    '''
( Movie name )
詞: ________
曲: ________
唱: ________'''