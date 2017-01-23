#import request, bokeh and json module
import requests 
import bokeh
import json

temp1= ""
temp2= ""

def kiev():
    global temp1

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
    return temp1
    
def wash():
    global temp2
    
    #create a url for the request
    endpoint = 'https://api.darksky.net/forecast/'
    #required perameters 
    key = '3eaabd2fc578c75b938c87b208915869'
    lat = '38.9072'
    lon = '77.0369' 

    url = endpoint + key + '/' + lat + ',' + lon


    #make request 
    r =requests.get(url)

    #deal with information recieved 
    weather =r.json()

    #whats the current weather
    temp2 = weather['currently']['temperature']
    return temp2

kiev()
wash()

#import needed for bokeh

from bokeh.models import Title
from bokeh.plotting import figure, show, output_file

#file where the bar graph of the weather will be shown
output_file('temperaturebar.html')

#size and title of graph
p = figure(title = "Kiev vs Washington", height= 500, width= 500)

#bar for Kiev 
p.vbar(x=[2], width= 0.5, bottom =0, top= [temp1], color= 'goldenyellow', ledgend= "kiev")

#bar for Washington
p.vbar(x=[2], width= 0.5, bottom =0, top= [temp2], color= 'darkblue', ledgend= "washington")

#customize the x and y axis
p.add_layout(Title(text= 'City', align= 'center'), 'below')
p.add_layout(Title(text='Temperature (F)', align='center'), 'left')

#see the graph
show(p)