import selenium
from selenium import webdriver
from selenium import *
from selenium.webdriver.common import actions
from selenium.webdriver.common.actions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import pandas as pd
import numpy as np
import openpyxl
from openpyxl import *
p=input("name the player")
d= webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
d.get("https://www.basketball-reference.com/")
searchbar= d.find_element_by_xpath('//*[@id="header"]/div[3]/form/div/div/input[2]')
searchbar.click()
searchbar.send_keys(p)
searchbar.send_keys(Keys.RETURN)
time.sleep(5)
players=[]
players= d.find_elements_by_class_name('search-item')
playernames=[]
print(len(players))
for player in players:
    name= player.find_element_by_class_name('search-item-name')
    i=(input)("is this the player you are looking for: "+name.text+" ? (y or n)")
    if(i=="y"):
        player.find_element_by_tag_name('a').click()
        break
gl=d.find_element_by_xpath('//*[@id="inner_nav"]/ul/li[3]/span')
actions=ActionChains(d)
actions.move_to_element(gl).perform()
season=d.find_element_by_link_text('2021-22')
runs=0
count=0
d.maximize_window()
while(count!=100):
    try:
        actions.move_to_element(gl).move_to_element(season).click().perform()
    except:
        runs+=1
    count+=1
if(runs==count):
    print("did not work")
stats=d.find_element_by_xpath('/html/body/div[2]/div[5]/div[4]/div/div[2]/table/tbody')
o=stats.find_elements_by_tag_name('tr')
print(len(o))
data=[]

yt=[]
for i in range(1,len(o)):
    if(i>0 and ((i%21)!=0)):
        yt=[]
        xp6='/html/body/div[2]/div[5]/div[4]/div/div[2]/table/tbody/tr['+str(i)+']/td[6]/a'
        xp2='/html/body/div[2]/div[5]/div[4]/div/div[2]/table/tbody/tr['+str(i)+']/td[2]/a'
        yt.append(d.find_element_by_xpath(xp2).text)
        yt.append(d.find_element_by_xpath(xp6).text)
        xp8='/html/body/div[2]/div[5]/div[4]/div/div[2]/table/tbody/tr['+str(i)+']/td[8]'
        check=d.find_element_by_xpath(xp8).text
        if((check!="Inactive")):
            xp21='/html/body/div[2]/div[5]/div[4]/div/div[2]/table/tbody/tr['+str(i)+']/td[21]'
            xp22='/html/body/div[2]/div[5]/div[4]/div/div[2]/table/tbody/tr['+str(i)+']/td[22]'
            xp27='/html/body/div[2]/div[5]/div[4]/div/div[2]/table/tbody/tr['+str(i)+']/td[27]'
            
            yt.append(d.find_element_by_xpath(xp21).text)
            yt.append(d.find_element_by_xpath(xp22).text)
            yt.append(d.find_element_by_xpath(xp27).text)
        else:
            yt.append("Inactive")
            yt.append("n/a")
            yt.append('n/a')
        data.append(yt)
totalstats=[]
for i in range(len(data)):
    playerstats={
        'date':data[i][0],
        'opponent':data[i][1],
        'rebounds':data[i][2],
        'assists':data[i][3],
        'points':data[i][4]
    }
    totalstats.append(playerstats)
playerdf=pd.DataFrame(totalstats)
print(playerdf)
playerdf.to_excel(p+".xlsx")




