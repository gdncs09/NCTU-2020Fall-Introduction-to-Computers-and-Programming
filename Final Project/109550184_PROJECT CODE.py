'''FINAL PROJECT OF RIN'''

try:
#Libraries
    import googlemaps
    from googlesearch import search
    import urllib.request, urllib.parse, urllib.error
    from urllib.request import Request,urlopen
    from bs4 import BeautifulSoup
    import re
    import json
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import time
    import random
    import sys
        
#Google
    api_key="AIzaSyCtkTTv1odVALjOAhRr9KhbasJDWsP28qE"
    gmaps=googlemaps.Client(key=api_key)
    driver=webdriver.Chrome(ChromeDriverManager().install()) #selenium
    print("*請不要關掉網站以免發生錯誤!*")
    def Init_Link_Place(location,radius,types,keyword,key): #URL
        serviceurl="https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
        if key=="find":
            url=serviceurl+urllib.parse.urlencode({'location':location,
                                                   'radius':radius,
                                                   'types':types,
                                                   'keyword':keyword})
        elif key=="nextpage": 
            url=serviceurl+urllib.parse.urlencode({'pagetoken':nextpage_key})     
        url+="&key="+api_key
        return url
        
    def Location(address): #Get Lat and Lng
        try:
            geocode_result=gmaps.geocode(address)
            lat=geocode_result[0]['geometry']['location']['lat'] #latitude
            lng=geocode_result[0]['geometry']['location']['lng'] #longitude
            return(str(lat)+','+str(lng),lat,lng)
        except ValueError:
            print("Location Error")
            sys.exit()
        
    def Database(url,restaurants,N): #Restaurants Database 
        uh=urllib.request.urlopen(url)
        data=uh.read().decode()
        try:
            js=json.loads(data)
        except:
            print("Jason Error")
            sys.exit()
                
        for restaurant in js["results"]:
            N+=1
            name=restaurant["name"] #Restaurant name
            address=restaurant["vicinity"] #Address
            rating=restaurant["rating"] #Rating
                
            #Dist
            restaurants[str(N)]={}
            restaurants[str(N)]['name']=name 
            restaurants[str(N)]['address']=address
            restaurants[str(N)]['rating']=rating 
        try:
            nextpage_key=js["next_page_token"]  
        except KeyError:
            nextpage_key=None
        return restaurants,N,nextpage_key
    
#Google search          
    def Search(query): 
        print("-------參考網頁-------")
        for web in search(query,tld='co.in',num=2,start=0,stop=2,pause=1):
            print(web,'\n')
            
#Food Panda
    def CheckCount(count,lenstr):
        if count < lenstr*50/100: #50%
            return False
        else:
            return True
                
    def CheckFoodpanda(name,foodpanda_name):
        if name in foodpanda_name: #Easy Check
            return True   
        
        values=[]
        arr=[]
        count=0
        n_values=-1
        name=name.replace(" ","")
        foodpanda_name=foodpanda_name.replace(" ","")
        for i in range(len(foodpanda_name)):
            arr.append(0)
            
        for word_name in name:
            x=foodpanda_name.find(word_name)
            if x!=-1:
                if arr[x]!=0:
                    if word_name==foodpanda_name[values[n_values]+1]:
                        x=values[n_values]+1
                arr[x]=1
            values.append(x)
            n_values+=1
        exist=False
        get=-1
        
        for value in values:
            if value!=-1:
                if exist and value==get+1:
                    get=value
                    count+=1
                elif exist and value!=get+1:
                    exist=CheckCount(count, len(name))
                    if exist:
                        return True
                elif not exist:
                    get=value
                    exist=True
            if value==-1:
                exist=CheckCount(count, len(name))
                if exist:
                    return True
                count=0
        exist=CheckCount(count,len(name))
        return exist
                 
    def FoodPanda(lat,lng,query): 
        homeurl="https://www.foodpanda.com.tw/restaurants/new?"
        url=homeurl+urllib.parse.urlencode({'lat':str(lat),
                                            'lng':str(lng),
                                            'vertical':'restaurants',
                                            'query':query})    
        html=urlopen(Request(url,headers={'User-Agent': 'Mozilla/5.0'})).read().decode("utf-8")
        soup=BeautifulSoup(html,"html.parser")
        webpages=re.findall('[0-9],"name":"(.*?)",.*?,"redirection_url":"(.*?)"',str(soup)) #Name and URL
        print("-------FOODPANDA------")
        print("Find in Foodpanda: ",webpages[0][0]) #Find in Foodpanda
        if CheckFoodpanda(query,webpages[0][0]): #Check name 
            driver.get(webpages[0][1]) #Open web
            print("已打開網站!")
        else:
            print("CAN'T FIND FOODPANDA SERVICE!")
    
#Output
    def Randomize(number,num_results): #Random
        return(random.sample(range(1,N+1),num_results))#Random from 1 to N
                
    def Footer():
        print("***[Q: Quit]  [B: Back]  [R:Random]***")
        print("_____________________________________________")
        
    def Output(No):
        print("餐廳名字: ",restaurants[No]['name'])
        print("地址: ",restaurants[No]['address'])
        print("評價: ",restaurants[No]['rating']) 
                 
    def CheckLayer(key,layer): #Check user input
        if key=='Q':
            sys.exit()
        elif key=='C' and layer==0:
            layer=0
        elif key=='B' and layer>0:
            layer-=1
        elif key=='R' and layer>0:
            layer=1
        elif layer<2 and layer>0:
            layer+=1
        return layer
        
#Layer
    def Layer1():
        try:
            for i in range(num_results):
                No=str(selects[i])
                print("-------------------",i+1,"-------------------")
                Output(No)     
        except:
            print("Error")
        Footer()
            
    def Layer2(i):
        try:    
            No=str(selects[int(i)-1])
            print("-------------------",i,"-------------------")
            Output(No)
            Search(restaurants[No]['name'])
            FoodPanda(lat,lng,restaurants[No]['name'])
        except:
            print("輸入錯誤!")
        print("-------------這是最後一頁-------------")
        Footer()

#Main
    layer=0
    key=''
    print("FINAL PROJECT: WHAT TO EAT TODAY? - 今天吃什麼?")
    while True:
        if layer==0:
            print("___________________Layer 0___________________")
            address=input("輸入你位置: ") #Address
            radius=input("想找的範圍 (meter): ")  #Radius
            keyword=input("你想吃的類型 (飯，麵...): ") #Keyword
            location,lat,lng=Location(address) #lat,lng
            types='restaurant'
        
            #Database GG Maps
            print("-----------準備資料庫中，請稍等-----------")
            restaurants={} #Dict
            N=0 #count restaurants
            url=Init_Link_Place(location, radius, types, keyword,"find") #Find
            restaurants,N,nextpage_key=Database(url, restaurants, N) #Database
            while True:
                url=Init_Link_Place(location, radius, types, keyword,"nextpage") #Next_page_token 
                time.sleep(2) #Wait next_page_token available
                restaurants,N,nextpage_key=Database(url, restaurants, N) #Database
                if N==99 or nextpage_key==None:
                    break
            if N>0: #Database not empty
                layer=1
            else:
                print("資料庫空")
                while True:
                    print("***[Q: Quit]  [C: Continue]***")
                    key=input("Continue?: ")
                    if key=='Q':
                        sys.exit()
                    elif key=='C':
                        break
                    else:
                        print("輸入錯誤!")
        
            print("總共找到",N,"餐廳") #Total
        
            if N>=3:
                num_results=3
            else:
                num_results=N
            selects=Randomize(N,num_results) #3 numbers
        
        if key=='R': #Random
            selects=Randomize(N,num_results)
    #Layer1
        if layer==1: 
            print("___________________Layer 1___________________")
            Layer1()
            
        if layer==1:
            key=input("請輸入餐廳號碼: ")
        elif layer==2:
            key=input("請輸入: ")
            if not (key=='Q' or key=='B' or key=='R'):
                print("輸入錯誤!")
                continue
        layer=CheckLayer(key,layer) #Check Layer 
        
     #Layer2  
        if layer==2: 
            print("___________________Layer 2___________________")
            Layer2(key)

        if layer==0 and N>0:
            while True:
                print("_____________________________________________")
                print("-----------------確定返回首頁-----------------")
                print("***[Q: Quit]  [C: Continue] [B: Back]***")
                key=input("Continue?: ")
                if key=='B':
                    layer=1
                    break
                elif key=='Q' or key=='C':
                    layer=CheckLayer(key, layer) #Check Layer
                    break
                else:
                    print("輸入錯誤!")
except ModuleNotFoundError: #Check Libraries
    print("Module Not Found")
except SystemExit: #Press Q
    print("THANK YOU!")