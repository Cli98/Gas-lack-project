# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 14:54:48 2017

@author: Changlin
"""
import pandas as pd
##This is a rudimentary file prepared for gas leak prediction project

##Task 1: import two csv and combine into one entire file.
##upload this file once finished
Noset = pd.read_csv(r"E:\gas leak project\machine learning\Nset.csv").iloc[:,2:]
Opset = pd.read_csv(r"E:\gas leak project\machine learning\Oset.csv").iloc[:,2:]
Noset['IsBopa'] = 0
Opset['IsBopa'] = 1
piece = [Noset,Opset]
dataset = pd.concat(piece)

##take care of geocode
geox = []
geoy = []
for i in range(len(dataset)):
    tep = dataset.iloc[i,-3].split(r'/')
    geox.append(float(tep[0]))
    geoy.append(float(tep[1]))
dataset = dataset.drop(dataset.columns[[-3]], axis=1)
dataset['geox'] = geox
dataset['geoy'] = geoy

##task2: DATA preparation
##Null check
import pandas as pd
from sklearn.preprocessing import LabelEncoder
dataset = pd.read_csv(r"E:\gas leak project\machine learning\comb.csv").iloc[:,1:]
nullrecord = dataset.isnull().sum()/len(dataset)
nullrecord.plot(kind = 'bar')

##After checking the plot we remove all missing info greater than 0.8

dataset = dataset.drop(dataset.columns[[3,5,6,7,8,9,10,13,14,33,39]], axis=1)
nullrecord = dataset.isnull().sum()/len(dataset)

##I use most common way to fill na, namely mean

dataset = dataset.fillna(dataset.mean()['LandUse'])
coder = LabelEncoder()
dataset['BldgClass'] = coder.fit_transform(dataset['BldgClass'])
coder = LabelEncoder()
dataset['ZoneDist1'] = coder.fit_transform(dataset['ZoneDist1'])
dataset.to_csv(r"E:\gas leak project\machine learning\comb.csv")

##task3 :feature engineering

import pandas as pd
dataset = pd.read_csv(r"E:\gas leak project\machine learning\comb.csv").iloc[:,1:]
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
y = dataset.iloc[:,-3]
trainset = dataset.drop(dataset.columns[[-3]], axis=1)
xTrain,xTest,yTrain,yTest = train_test_split(trainset,y,test_size = 0.20,random_state = 40)
sc = StandardScaler()
xTrain = sc.fit_transform(xTrain)
xTest = sc.transform(xTest)

##LR classifier
clf = LogisticRegression()
clf.fit(xTrain,yTrain)
print (clf.score(xTest,yTest))
name = trainset.columns
tep = pd.DataFrame(data = clf.coef_[0],index = name)
tep.plot(kind = 'bar')

##  rf classifier
rfc = RandomForestClassifier()
rfc.fit(xTrain,yTrain)
print (rfc.score(xTest,yTest))
ima = rfc.feature_importances_
tep = pd.DataFrame(data = ima,index = name)
tep.plot(kind = 'bar')

##SVC model
clfc = SVC()
clfc.fit(xTrain,yTrain)
print (clfc.score(xTest,yTest))
