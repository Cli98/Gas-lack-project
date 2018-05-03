# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 15:05:20 2017

@author: Administrator
"""
##assuming you are using excel as database file
from selenium import webdriver
import pandas as pd
import time
##setup environment
driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
#storepath = input("please input path for the output dataset: ")
##Readin data
filepath = r"E:\gas leak project\nyc_pluto_16v2_\BORO_zip_files_csv\MN.csv"
col = 2
city = r"+Manhattan,"
state = r"+Newyork"
API_KEY = r"AIzaSyC8YxtZ_LBD_n-28XOXzKHWlF37_ck4jXU"
FormattedAddressList = []
latlst = []
lonlst = []
dataset = pd.read_csv(filepath).iloc[:,[1,2,15]]
for i in range(5):
    flag = 0
    if str(dataset.iloc[i,col]) == "nan":
        FormattedAddressList.append("Not found")
        latlst.append("Not found")
        lonlst.append("Not found")
        flag = -1
    if flag == 0:
        address = "+".join(dataset.iloc[i,col].split(" "))+","
        url = r'https://maps.googleapis.com/maps/api/geocode/json?address='+address+city+state+'&key='+API_KEY
        driver.get(url)
        time.sleep(10)
        raw = driver.find_element_by_tag_name("pre").text
        addressstart = raw.index('formatted_address')
        addressend = raw.index('geometry')
        FormattedAddressList.append(raw[addressstart+20:addressend-12])
        
        locstart = raw.index("location")
        locend = raw.index("location_type")
        location = raw[locstart:locend]
        latstart = location.index("lat")
        latend = location.index("lng")
        latlst.append(location[latstart+7:latend].split(",")[0])
        lonlst.append(location[latend+7:-1].split("\n")[0])
        driver.quit()

result = pd.DataFrame(FormattedAddressList,latlst,lonlst)