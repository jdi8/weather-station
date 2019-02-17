from guizero import *
import certifi
from apscheduler.schedulers.blocking import BlockingScheduler

import urllib.request
from bs4 import BeautifulSoup

site_page = 'https://weather.com/weather/today/l/USNC0192:1:US'
page = urllib.request.urlopen(site_page)
script = BeautifulSoup(page,'html.parser')

loc_descript = script.find('header', attrs ={ 'class': 'loc-container'})
location = loc_descript.text.strip()
location = location.split()
new_loc = location[1]
new_string = [0]*2

for k in range(0,1):
        
    new_string[k] = new_loc[k]
        
    new_string[1] = str(new_string[1])
    state = "NC"                        #Alter this for numerous locations
    loc_string = [0]*2
    loc_string[0] = location[0]
    loc_string[1] = state
    location = "".join(loc_string)



def temp_sensor():
    temp_descript = script.find('div', attrs ={ 'class': 'today_nowcard-temp'})
    temperature = temp_descript.text.strip()
    return temperature

def day_descript():
    day_descript = script.find('div', attrs ={ 'class': 'today_nowcard-phrase'})
    description = day_descript.text.strip()
    return description

def img_descript():
    day_descript = script.find('div', attrs ={ 'class': 'today_nowcard-phrase'})
    description = day_descript.text.strip()
    if description =="Cloudy" or description =="Partly Cloudy" or description =="Mostly Cloudy" or description =="Partly Clear":
        image = Picture(app, image="/Users/jdinge/Desktop/Weather Icons/cloudy.gif")
    elif description =="Sun" or description =="Sunny" or description =="Clear" or description =="Mostly Clear" or description =="Fair":
        image = Picture(app, image="/Users/jdinge/Desktop/Weather Icons/day.gif")
    elif description =="Rain" or description =="Rainy" or description =="Showers": 
        image = Picture(app, image="/Users/jdinge/Desktop/Weather Icons/rainy-6.gif")
    elif description =="Night": 
        image = Picture(app, image="/Users/jdinge/Desktop/Weather Icons/night.gif")
    elif description =="Snow" or description =="Snowy" or description =="Blizzard":
        image = Picture(app, image="/Users/jdinge/Desktop/Weather Icons/snowy-6.gif")
    elif description =="Thunder" or description =="Storm" or description =="Stormy" or description =="Thunderstorms" or description =="Thundershowers" or description =="Lightning":
        image = Picture(app, image="/Users/jdinge/Desktop/Weather Icons/thunder.gif")
    elif description =="Wind" or description =="Windy" or description =="Gusts" or description =="Gusty": 
        image = Picture(app, image="/Users/jdinge/Desktop/Weather Icons/wind.gif")
    else:
        image = Picture(app, image="/Users/jdinge/Desktop/Weather Icons/duke.gif", height=100, width=100)
    return image




def update_label():
    text.set(temp_sensor())
    text2.set(day_descript())
    # recursive call
    text.after(1000, update_label)
    



if __name__ == '__main__':
    app = App(title='Weather Station')

    title = Text(app, location, size = 90, font = "Times New Roman")
    text = Text(app, "xx", size = 70,font = "Times New Roman" )
    text2 = Text(app, 'xx', size = 70,font = "Times New Roman")
    picture = img_descript()
    image = picture.repeat(1000,picture)
    text.after(1000, update_label)
    app.display()
