# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 13:35:45 2017

@author: Administrator
"""
import pandas as pd
pluto = pd.read_csv(r"E:\gas leak project\BOPA primary set\PLUTO_MN_GeoClient.csv").iloc[:,[5,-2]]

corx = []
cory = []
for i in range(len(pluto)):
    pluto.iloc[i,0] = str(pluto.iloc[i,0]).strip()
    if len(str(pluto.iloc[i,1]))>3:
        ind = pluto.iloc[i,1].index(',')
        corx.append(pluto.iloc[i,1][:ind])
        cory.append(pluto.iloc[i,1][ind+1:])
    else:
        corx.append(0)
        cory.append(0)
pluto = pluto.iloc[:,:-1]
pluto['corx'] = corx
pluto['cory'] = cory

pluto.to_csv(r"E:\gas leak project\machine learning\newset\PLUTO_MN_GeoClientf.csv")