# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from apscheduler.schedulers.blocking import BlockingScheduler

import urllib
from bs4 import BeautifulSoup
site_page = 'https://weather.com/weather/today/l/USCO0458:1:US'
page = urllib.request.urlopen(site_page)
script = BeautifulSoup(page,'html.parser')


    #%%Location
loc_descript = script.find('header', attrs ={ 'class': 'loc-container'})
location = loc_descript.text.strip()
location = location.split()
new_loc = location[1]
new_string = [0]*2

for k in range(0,1):
        
    new_string[k] = new_loc[k]
        
    new_string[1] = str(new_string[1])
    state = "".join(new_string)
    loc_string = [0]*2
    loc_string[0] = location[0]
    loc_string[1] = state
    location = "".join(loc_string)
    print(location)


    


        #%%Temperature
def weather():
    temp_descript = script.find('div', attrs ={ 'class': 'today_nowcard-temp'})
    temperature = temp_descript.text.strip()
    print(temperature)
        
        #%%weather
    day_descript = script.find('div', attrs ={ 'class': 'today_nowcard-phrase'})
    description = day_descript.text.strip()
    print(description)
    
scheduler = BlockingScheduler()
scheduler.add_job(weather, 'interval', seconds = 5)
scheduler.start()
    
    

    


    

