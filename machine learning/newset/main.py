# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 14:41:32 2017

@author: Admi nistrator
"""
import pandas as pd
pluto = pd.read_csv(r"E:\gas leak project\machine learning\newset\plutoup.csv")
mn = pd.read_csv(r"E:\gas leak project\machine learning\newset\MNOup.csv")
addlistmn = []
addlistpluto = []
#corx = []
#cory = []
#difference = []
def IsR(a1,a2,b1,b2):
    return (abs(a1-b1) < 9.009009009009009e-05) and (abs(a2-b2) < 9.009009009009009e-05)
for i in range(len(mn)):
    a1 = mn.iloc[i,-2]
    a2 = mn.iloc[i,-1]
    for j in range(len(pluto)):
        b1 = pluto.iloc[j,-2]
        b2 = pluto.iloc[j,-1] 
        if IsR(a1,a2,b1,b2) and mn.iloc[i,0] is not "":
            addlistmn.append(str(mn.iloc[i,0])+str(mn.iloc[i,1])+str(mn.iloc[i,2])+str(mn.iloc[i,3]))
            addlistpluto.append(str(pluto.iloc[j,0]))
            break
    