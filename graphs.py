#import request, bokeh and json module
import requests 
import pandas as pd
import bokeh
import json

temp1= ""
temp2= ""
humid1= ""
humid2= ""


def kiev():
    global temp1
    global humid1

    #create a url for the request
    endpoint = 'https://api.darksky.net/forecast/'
    #required perameters 
    key = '3eaabd2fc578c75b938c87b208915869'
    lat = '50.4501'
    lon = '30.5234' 

    url = endpoint + key + '/' + lat + ',' + lon


    #make request 
    r =requests.get(url)

    #deal with information recieved 
    weather =r.json()

    #whats the current weather
    temp1 = weather['currently']['temperature']
    humid1 = weather['daily']['data'][0]['humidity']
    
    Kiev = ['Kiev', temp1, humid1]

    return Kiev

def wash():
    global temp2
    global humid2
    
    #create a url for the request
    endpoint = 'https://api.darksky.net/forecast/'
    #required perameters 
    key = '3eaabd2fc578c75b938c87b208915869'
    lat = '38.9072'
    lon = '-77.0369' 

    url = endpoint + key + '/' + lat + ',' + lon


    #make request 
    r =requests.get(url)

    #deal with information recieved 
    weather =r.json()

    #whats the current weather and humidity
    temp2 = weather['currently']['temperature']
    humid2= weather['daily']['data'][0]['humidity']
    
    #put the data under one variable
    Wash= ['Washington', temp2, humid2]

    return Wash

Kiev = kiev()
Wash = wash()

city = [Kiev[0],Wash[0]]
temp = [Kiev[1],Wash[1]]
humidity= [Kiev[2],Wash[2]]

#make data frame
df = pd.DataFrame({
    'cities': city,
    'temperature': temp,
    'humidity': humidity
})

#import needed for bokeh

from bokeh.models import Title
from bokeh.charts import Bar, save, output_file

#file where the bar graph of the weather will be shown
output_file('temperaturebar.html')

#size and title of graph
p = Bar(df,'cities',values= 'temperature', title = "Current Temperature in Kiev vs Washington", height= 500, width= 500, legend= False, color= 'blue')


#see the graph
save(p)


#file where the bar graph of the weather will be shown
output_file('humidity.html')

#size and title of graph
p2 = Bar(df,'cities',values= 'humidity', title = "Daily Humidity in Kiev vs Washington", height= 500, width= 500, legend= False, color= 'green')


#see the graph
save(p2)