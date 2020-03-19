#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 08:17:36 2020

@author: suwadith
"""

#Importing Libraries
import numpy as np #To handle Mathematical calculations
import matplotlib.pyplot as plt #To plot charts
import pandas as pd #To import and manage datasets
import glob
import os



#Combining All Offensive Data
path = r'../Datasets/Whoscored/Player-Stats'
folder = glob.glob(path + "/*Offensive*.csv")

li = []

for file in folder:
    individualOffensivePlayerDataframe = pd.read_csv(file)
    league = os.path.basename(file).split('-')[0]
    season = os.path.basename(file).split('-')[2]
    individualOffensivePlayerDataframe['League'] = league
    individualOffensivePlayerDataframe['Season'] = season
    for index, row in individualOffensivePlayerDataframe.iterrows():
        age = int(row["Age"]) - (2018-int(row["Season"]))
        individualOffensivePlayerDataframe.set_value(index, 'Age', age)
        
        #Cleaning Apps column
        if '(' in row["Apps"] :
            apps = int(row["Apps"].split("(")[0])
            individualOffensivePlayerDataframe.set_value(index, 'Apps', apps)
        else :
            apps = int(row["Apps"])
            individualOffensivePlayerDataframe.set_value(index, 'Apps', apps)
    
    li.append(individualOffensivePlayerDataframe)

combinedOffensivePlayerDataframe = pd.concat(li)



#Combining All Defensive Data
path = r'../Datasets/Whoscored/Player-Stats'
folder = glob.glob(path + "/*Defensive*.csv")

li = []

for file in folder:
    individualOffensivePlayerDataframe = pd.read_csv(file)
    league = os.path.basename(file).split('-')[0]
    season = os.path.basename(file).split('-')[2]
    individualOffensivePlayerDataframe['League'] = league
    individualOffensivePlayerDataframe['Season'] = season
    for index, row in individualOffensivePlayerDataframe.iterrows():
        age = int(row["Age"]) - (2018-int(row["Season"]))
        individualOffensivePlayerDataframe.set_value(index, 'Age', age)
        
        #Cleaning Apps column
        if '(' in row["Apps"] :
            apps = int(row["Apps"].split("(")[0])
            individualOffensivePlayerDataframe.set_value(index, 'Apps', apps)
        else :
            apps = int(row["Apps"])
            individualOffensivePlayerDataframe.set_value(index, 'Apps', apps)
    
    li.append(individualOffensivePlayerDataframe)

combinedDefensivePlayerDataframe = pd.concat(li)



#Combining All Passing Data
path = r'../Datasets/Whoscored/Player-Stats'
folder = glob.glob(path + "/*Passing*.csv")

li = []

for file in folder:
    individualOffensivePlayerDataframe = pd.read_csv(file)
    league = os.path.basename(file).split('-')[0]
    season = os.path.basename(file).split('-')[2]
    individualOffensivePlayerDataframe['League'] = league
    individualOffensivePlayerDataframe['Season'] = season
    for index, row in individualOffensivePlayerDataframe.iterrows():
        age = int(row["Age"]) - (2018-int(row["Season"]))
        individualOffensivePlayerDataframe.set_value(index, 'Age', age)
        
        #Cleaning Apps column
        if '(' in row["Apps"] :
            apps = int(row["Apps"].split("(")[0])
            individualOffensivePlayerDataframe.set_value(index, 'Apps', apps)
        else :
            apps = int(row["Apps"])
            individualOffensivePlayerDataframe.set_value(index, 'Apps', apps)
    
    li.append(individualOffensivePlayerDataframe)

combinedPassingPlayerDataframe = pd.concat(li)



#Combining All Summary Data
path = r'../Datasets/Whoscored/Player-Stats'
folder = glob.glob(path + "/*Summary*.csv")

li = []

for file in folder:
    individualOffensivePlayerDataframe = pd.read_csv(file)
    league = os.path.basename(file).split('-')[0]
    season = os.path.basename(file).split('-')[2]
    individualOffensivePlayerDataframe['League'] = league
    individualOffensivePlayerDataframe['Season'] = season
    for index, row in individualOffensivePlayerDataframe.iterrows():
        age = int(row["Age"]) - (2018-int(row["Season"]))
        individualOffensivePlayerDataframe.set_value(index, 'Age', age)
        
        #Cleaning Apps column
        if '(' in row["Apps"] :
            apps = int(row["Apps"].split("(")[0])
            individualOffensivePlayerDataframe.set_value(index, 'Apps', apps)
        else :
            apps = int(row["Apps"])
            individualOffensivePlayerDataframe.set_value(index, 'Apps', apps)
    
    li.append(individualOffensivePlayerDataframe)

combinedSummaryPlayerDataframe = pd.concat(li)



#combining all the DFs'
combinedPlayerDataframe = pd.concat([combinedOffensivePlayerDataframe, combinedDefensivePlayerDataframe, combinedPassingPlayerDataframe, combinedSummaryPlayerDataframe], axis=1)

combinedPlayerDataframe = combinedPlayerDataframe.loc[:,~combinedPlayerDataframe.columns.duplicated()]




#Re-arranging the Dataframes to get sesasonal data of every attributes of players
nameSeasonOffensiveDF = combinedOffensivePlayerDataframe.pivot_table(index=['Name'], columns=['Season'], values=['Rating', 'Apps', 'Age', 'Team', 'League'], aggfunc='first').reset_index()
nameSeasonDefensiveDF = combinedDefensivePlayerDataframe.pivot_table(index=['Name'], columns=['Season'], values=['Rating', 'Apps', 'Age', 'Team', 'League'], aggfunc='first').reset_index()
nameSeasonPassingDF = combinedPassingPlayerDataframe.pivot_table(index=['Name'], columns=['Season'], values=['Rating', 'Apps', 'Age', 'Team', 'League'], aggfunc='first').reset_index()
nameSeasonOSummaryDF = combinedSummaryPlayerDataframe.pivot_table(index=['Name'], columns=['Season'], values=['Rating', 'Apps', 'Age', 'Team', 'League'], aggfunc='first').reset_index()

nameSeasonOffensiveDF.head()

#Switching the pivot table structure to a different form to analyse time series data 
seasonNameOffensiveDF = combinedOffensivePlayerDataframe.pivot_table(index=['Season'], columns=['Name'], values=['Rating', 'Apps', 'Age', 'Team', 'League'], aggfunc='first').reset_index()
seasonNameDefensiveDF = combinedDefensivePlayerDataframe.pivot_table(index=['Season'], columns=['Name'], values=['Rating', 'Apps', 'Age', 'Team', 'League'], aggfunc='first').reset_index()
seasonNamePassingDF = combinedPassingPlayerDataframe.pivot_table(index=['Season'], columns=['Name'], values=['Rating', 'Apps', 'Age', 'Team', 'League'], aggfunc='first').reset_index()
seasonNameSummaryDF = combinedSummaryPlayerDataframe.pivot_table(index=['Season'], columns=['Name'], values=['Rating', 'Apps', 'Age', 'Team', 'League'], aggfunc='first').reset_index()

seasonNameOffensiveDF.head()

#Testing the time series based dataset by plotting few players on a graph
ronaldoDf = combinedOffensivePlayerDataframe.loc[combinedOffensivePlayerDataframe['Name'] == 'Cristiano Ronaldo']
messiDf = combinedOffensivePlayerDataframe.loc[combinedOffensivePlayerDataframe['Name'] == 'Lionel Messi']
neymarDf = combinedOffensivePlayerDataframe.loc[combinedOffensivePlayerDataframe['Name'] == 'Neymar']
iniestaDF = combinedOffensivePlayerDataframe.loc[combinedOffensivePlayerDataframe['Name'] == 'Andrés Iniesta']

players = [ronaldoDf, messiDf, neymarDf, iniestaDF]

combinedPlayersDf = pd.concat(players)

tansformedCombinedPlayersDf = combinedPlayersDf.pivot_table(index=['Season'], columns=['Name'], values=['Rating', 'Apps', 'Age', 'Team', 'League'], aggfunc='first').reset_index()

tansformedCombinedPlayersDf.plot(x ='Season', y='Rating', kind = 'line')



##############Trying out regression

#list column names
#[(f"column {i+1} : {column}") for i, column in enumerate(combinedSummaryPlayerDataframe.columns)]
[(f"column {i+1} : {column}") for i, column in enumerate(combinedPlayerDataframe.columns)]

#Remove unwanted columns
#finalDf = combinedSummaryPlayerDataframe.drop(["Team", "Position", "League", "Season"], axis = 1)
finalDf = combinedPlayerDataframe.drop(["Team", "Position", "League", "Season"], axis = 1)

#replace - fields with 0
finalDf = finalDf.replace('-', 0)

#checks if duplicates exists
finalDf.duplicated().any()

#removes NaN values
finalDf = finalDf.dropna()

#check if null value exitst
finalDf.isnull().any()

#returns DF shape
finalDf.shape

#check column data types
finalDf.dtypes

#replace Name column with dummy data for each different player names
finalDf = pd.get_dummies(finalDf, columns=["Name"])

finalDf.dtypes

#conert object data types to flot (except for names)
cols = finalDf.select_dtypes(exclude=['uint8']).columns
finalDf[cols] = finalDf[cols].apply(pd.to_numeric, downcast='float', errors='coerce')

finalDf.dtypes

finalDf.head()


#Creating X, y datasets (X = everything except rating, y = just the rating)
X = finalDf.drop(['Rating'], axis = 1)
y = np.array(finalDf['Rating'])
y


#Splitting into training & test datasets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 10)


#Training with different regressors
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn import model_selection

seed = 7
kfold = model_selection.KFold(n_splits=10, random_state=seed)


dtm = DecisionTreeRegressor()
scoring = 'r2'
y_pred = dtm.fit(X_train,y_train).predict(X_train)
results = model_selection.cross_val_score(dtm, X_test, y_test, cv=kfold, scoring=scoring)
print("DecisionTreeRegressor")
print(results.mean(), results.std())

rfm = RandomForestRegressor()
scoring = 'r2'
y_pred = rfm.fit(X_train,y_train).predict(X_train)
results = model_selection.cross_val_score(rfm, X_test, y_test, cv=kfold, scoring=scoring)
print("RandomForestRegressor")
print(results.mean(), results.std())










#dummyName = pd.get_dummies(finalDf['Name'])
#finalDf.shape
#
#finalDf = pd.concat([finalDf, dummyName], axis=1)



#finalDf["Rating"].value_counts().plot(kind='bar', figsize=(20,10))

#from sklearn.svm import SVR
#clf7 = SVR(kernel = 'rbf')
#
#
#y_pred = clf7.fit(X_train,y_train).predict(X_train)
#scores = cross_val_score(clf7, X_test, y_test, cv=10)
#print(scores)
#print(scores.mean())

#finalDf = finalDf.merge(dummyName, left_index=True, right_index=True)

#finalDf["Rating"].value_counts().plot(kind='bar', figsize=(20,10))
#
#X = finalDf.drop(['Rating'], axis = 1)
#y = np.array(finalDf['Rating'])
#y
#
#from sklearn.model_selection import train_test_split
#
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 10)
#
#from sklearn.tree import DecisionTreeRegressor
#dtr = DecisionTreeRegressor(min_samples_split=10, random_state=55)
#dtr.fit(X_train, y_train)
#y_pred = dtr.predict(X_test)
#
#from sklearn.metrics import mean_squared_error
#
#score = mean_squared_error(y_test, y_pred)
#score
#
#finalDf.head()

#Creating DF for players who were active between 2009-2015
#path = r'../Datasets/Whoscored/Player-Stats'
#folder = glob.glob(path + "/*Summary*.csv")
#
#li = []
#
#for idx, file in enumerate(folder):
#    if(idx < 7):
#        individualOffensivePlayerDataframe = pd.read_csv(file)
#        league = os.path.basename(file).split('-')[0]
#        season = os.path.basename(file).split('-')[2]
#        individualOffensivePlayerDataframe['League'] = league
#        individualOffensivePlayerDataframe['Season'] = season
#        for index, row in individualOffensivePlayerDataframe.iterrows():
#            age = int(row["Age"]) - (2018-int(row["Season"]))
#            individualOffensivePlayerDataframe.set_value(index, 'Age', age)
#        
#        li.append(individualOffensivePlayerDataframe)
#
#sixSummaryPlayerDataframe = pd.concat(li)