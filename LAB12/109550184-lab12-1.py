#Class
class RegionWeather:
    def __init__(self,region_weather):
        self.region_weather=region_weather
        self._region_name="default"
        self._sunday_weather_description="default"
        self._minT_average="default"
        
    @property
    def region_name(self):
        return self._region_name
    
    @region_name.setter
    def region_name(self,place):
        self._region_name=place

    @property
    def sunday_weather_description(self):
        return self._sunday_weather_description
    
    @sunday_weather_description.setter
    def sunday_weather_description(self,weather_description):
        self._sunday_weather_description=weather_description 
        
    @property    
    def minT_average(self):
        return self._minT_average   
    
    @minT_average.setter
    def minT_average(self, temperature):  
        self._minT_average=temperature
    
    def find_region_name(self):
        return self.region_weather["locationName"]    

    def find_sunday_weather(self):
        week_weather=self.region_weather["weatherElements"]["Wx"]["daily"]
        for daily_weather in week_weather:
            if daily_weather["dataDate"] == "2019-12-08":
                return daily_weather["weather"]     
    
    def compute_minT_avg(self):
        week_temperature=self.region_weather["weatherElements"]["MinT"]["daily"]
        total=0
        count=0
        for day_temperature in week_temperature:
            total=total+int(day_temperature["temperature"])
            count=count+1
        return total/count
       
import json

#Main
'''INPUT'''
with open('One week weather.json', encoding="utf-8") as f:
    weather_data=json.load(f)
all_region_weather=weather_data["cwbdata"]["resources"]["resource"]["data"]["weatherForecasts"]["location"]

for region_weather in all_region_weather:
    weather=RegionWeather(region_weather)
    '''REGION NAME'''
    weather.region_name=weather.find_region_name() 
    #print(weather.region_name) 
    
    '''SUNDAY WEATHER DESCRIPTION'''
    weather.sunday_weather_description=weather.find_sunday_weather()
    #print(weather.sunday_weather_description)
    
    '''MINT AVERAGE'''
    weather.minT_average=weather.compute_minT_avg()
    #print(weather.minT_average)
   
    '''OUTPUT'''
    print(weather.region_name,"minT average is",round(weather.minT_average,2),\
          ", Sunday's weather is",weather.sunday_weather_description)
    
    
    