# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 15:05:20 2017

@author: Administrator
"""
##assuming you are using excel as database file
from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd
##setup environment
print ("set up your work environment now,please input your Chromedriver location: ")
driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
storepath = input("please input path for the output dataset: ")
url = r'https://a810-dobnow.nyc.gov/publish/#'
driver.get(url)
driver.refresh()
##Readin data
filepath = r"E:\gas leak project\webcr\sample.xlsx"
dataset = pd.read_excel(filepath)
primaryAddressList = []
cityWithZipcodeList = []
BINList=[]
detailinfolist=[]
for i in range(len(dataset)):
    housenum = int(dataset.iloc[i,1])
    streetnum = str(dataset.iloc[i,2])+" "+str(dataset.iloc[i,3])+" "+str(dataset.iloc[i,4])
#start with method 1:
#test passed:
    driver.find_element_by_id("housenumber").clear()
    driver.find_element_by_id("streetnumber").clear()
    driver.find_element_by_id("housenumber").send_keys(housenum)
    driver.find_element_by_id("streetnumber").send_keys(streetnum)
    sel = driver.find_element_by_xpath("//select[@id='sel1']")
    Select(sel).select_by_value("1")
    driver.find_element_by_tag_name('button').click()
#successfully obtained result

##ADDRESS obtain
    address = driver.find_element_by_xpath("//div[@class = 'col-xs-12 col-sm-12 col-md-8 build-block v-pad-20']")
    address = address.text.split('\n')
    primaryAddressList.append(address[0])
    cityWithZipcodeList.append(address[1])
    BINList.append(address[2])
    
##not clear if we need this, so we do not add it into our dataset
    for i in range(9):
        detailinfo= driver.find_element_by_xpath("//div[@class = 'col-xs-6 col-sm-6 col-md-3 portal-fonts top-pad-10']"+"["+str(i+1)+"]"+"//div[@class = 'form-group']")
        detailinfolist.append(detailinfo.text)
#Health Area,Tax Block,Census Tract,Tax Lot,Community Board,Condo,Buildings on tax Lot,Vacant in order
#stored in detailinfo
returndata = {'primaryAddress':primaryAddressList,'cityWithZipcode':cityWithZipcodeList,
              'BIN':BINList}
returndata = pd.DataFrame(returndata)
returndata.to_excel(storepath)
driver.quit()

