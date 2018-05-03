# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:17:56 2017

@author: Administrator
"""

import requests
import pprint
url = "https://api.cityofnewyork.us/geoclient/v1/address.json?houseNumber=&street=116 E 38 St&borough=Manhattan&app_id=29cbe1cd&app_key=b3596f71f877c9058efa6369295272ec"
wb_data = requests.get(url).json()
geo_code = str(wb_data['address']['latitude']) + "," + str(wb_data['address']['longitude'])
pprint.pprint(wb_data)