# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 00:10:53 2020

@author: Suwadith
"""

#Importing Libraries

import numpy as np #To handle Mathematical calculations
import matplotlib.pyplot as plt #To plot charts 
import pandas as pd #TO import and manage datasets
import glob
import os
import warnings
from pandas import Series
from pandas import DataFrame
from pandas import concat
from statistics import mean 
from sklearn import linear_model 
# pd.set_option('display.max_columns', None)  
# pd.set_option('display.max_rows', None)  

#Disable warning messages
warnings.simplefilter(action='ignore', category=FutureWarning)



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
            
        #Cleaning Position column
        if ',' in row["Position"]:
            primary = row["Position"].split(",")[0]
            if '(' in primary:
                primary = primary.split("(")[0]
                individualOffensivePlayerDataframe.set_value(index, 'Position', primary)
            else:
                individualOffensivePlayerDataframe.set_value(index, 'Position', primary)
        elif '(' in row["Position"]:
            primary = row["Position"].split("(")[0]
            individualOffensivePlayerDataframe.set_value(index, 'Position', primary)
            
    li.append(individualOffensivePlayerDataframe)

combinedOffensivePlayerDataframe = pd.concat(li)


#Combining All Defensive Data
path = r'../Datasets/Whoscored/Player-Stats'
folder = glob.glob(path + "/*Defensive*.csv")

li = []

for file in folder:
    individualDefensivePlayerDataframe = pd.read_csv(file)
    league = os.path.basename(file).split('-')[0]
    season = os.path.basename(file).split('-')[2]
    individualDefensivePlayerDataframe['League'] = league
    individualDefensivePlayerDataframe['Season'] = season
    for index, row in individualDefensivePlayerDataframe.iterrows():
        age = int(row["Age"]) - (2018-int(row["Season"]))
        individualDefensivePlayerDataframe.set_value(index, 'Age', age)
        
        #Cleaning Apps column
        if '(' in row["Apps"] :
            apps = int(row["Apps"].split("(")[0])
            individualDefensivePlayerDataframe.set_value(index, 'Apps', apps)
        else :
            apps = int(row["Apps"])
            individualDefensivePlayerDataframe.set_value(index, 'Apps', apps)
            
        #Cleaning Position column  
        if ',' in row["Position"]:
            primary = row["Position"].split(",")[0]
            if '(' in primary:
                primary = primary.split("(")[0]
                individualDefensivePlayerDataframe.set_value(index, 'Position', primary)
            else:
                individualDefensivePlayerDataframe.set_value(index, 'Position', primary)
        elif '(' in row["Position"]:
            primary = row["Position"].split("(")[0]
            individualDefensivePlayerDataframe.set_value(index, 'Position', primary)
    
    li.append(individualDefensivePlayerDataframe)

combinedDefensivePlayerDataframe = pd.concat(li)


#Combining All Passing Data
path = r'../Datasets/Whoscored/Player-Stats'
folder = glob.glob(path + "/*Passing*.csv")

li = []

for file in folder:
    individualPassingPlayerDataframe = pd.read_csv(file)
    league = os.path.basename(file).split('-')[0]
    season = os.path.basename(file).split('-')[2]
    individualPassingPlayerDataframe['League'] = league
    individualPassingPlayerDataframe['Season'] = season
    for index, row in individualPassingPlayerDataframe.iterrows():
        age = int(row["Age"]) - (2018-int(row["Season"]))
        individualPassingPlayerDataframe.set_value(index, 'Age', age)
        
        #Cleaning Apps column
        if '(' in row["Apps"] :
            apps = int(row["Apps"].split("(")[0])
            individualPassingPlayerDataframe.set_value(index, 'Apps', apps)
        else :
            apps = int(row["Apps"])
            individualPassingPlayerDataframe.set_value(index, 'Apps', apps)
           
        #Cleaning Position column
        if ',' in row["Position"]:
            primary = row["Position"].split(",")[0]
            if '(' in primary:
                primary = primary.split("(")[0]
                individualPassingPlayerDataframe.set_value(index, 'Position', primary)
            else:
                individualPassingPlayerDataframe.set_value(index, 'Position', primary)
        elif '(' in row["Position"]:
            primary = row["Position"].split("(")[0]
            individualPassingPlayerDataframe.set_value(index, 'Position', primary)
    
    li.append(individualPassingPlayerDataframe)

combinedPassingPlayerDataframe = pd.concat(li)

#Combining All Summary Data
path = r'../Datasets/Whoscored/Player-Stats'
folder = glob.glob(path + "/*Summary*.csv")

li = []

for file in folder:
    individualSummaryPlayerDataframe = pd.read_csv(file)
    league = os.path.basename(file).split('-')[0]
    season = os.path.basename(file).split('-')[2]
    individualSummaryPlayerDataframe['League'] = league
    individualSummaryPlayerDataframe['Season'] = season
    for index, row in individualSummaryPlayerDataframe.iterrows():
        age = int(row["Age"]) - (2018-int(row["Season"]))
        individualSummaryPlayerDataframe.set_value(index, 'Age', age)
        
        #Cleaning Apps column
        if '(' in row["Apps"] :
            apps = int(row["Apps"].split("(")[0])
            individualSummaryPlayerDataframe.set_value(index, 'Apps', apps)
        else :
            apps = int(row["Apps"])
            individualSummaryPlayerDataframe.set_value(index, 'Apps', apps)
            
        #Cleaning Position column    
        if ',' in row["Position"]:
            primary = row["Position"].split(",")[0]
            if '(' in primary:
                primary = primary.split("(")[0]
                individualSummaryPlayerDataframe.set_value(index, 'Position', primary)
            else:
                individualSummaryPlayerDataframe.set_value(index, 'Position', primary)
        elif '(' in row["Position"]:
            primary = row["Position"].split("(")[0]
            individualSummaryPlayerDataframe.set_value(index, 'Position', primary)
            
    
    li.append(individualSummaryPlayerDataframe)

combinedSummaryPlayerDataframe = pd.concat(li)


#combining all the DFs'
combinedPlayerDataframe = pd.concat([combinedOffensivePlayerDataframe, combinedDefensivePlayerDataframe, combinedPassingPlayerDataframe, combinedSummaryPlayerDataframe], axis=1)

#Removing suplicates
combinedPlayerDataframe = combinedPlayerDataframe.loc[:,~combinedPlayerDataframe.columns.duplicated()]

#Removing players who have played less than 10 games in last season
minimum_number_of_games_played = 10
combinedPlayerDataframe = combinedPlayerDataframe[combinedPlayerDataframe.Apps >= minimum_number_of_games_played]

#Replace '-' with 0
combinedPlayerDataframe = combinedPlayerDataframe.replace('-', 0)


#Selecting only the needed columns for the forecasting process

allPlayers = combinedPlayerDataframe[['Name', 'Season', 'Rating', 'Age']]
allPlayers = allPlayers[allPlayers['Season'].notnull()].copy()
allPlayers['Season'] = allPlayers['Season'].astype(str).astype(int)
allPlayers


nameList = allPlayers.Name.unique()

meanDf = pd.DataFrame(columns=['Mean'])

#idList = allPLayers.id

for name in nameList:
    mean = allPlayers.loc[allPlayers.Name == name]['Rating'].mean()
    length = len(allPlayers.loc[allPlayers.Name == name]['Rating'])
    growth = allPlayers.loc[allPlayers.Name == name]['Rating'].tolist()[length-1] - allPlayers.loc[allPlayers.Name == name]['Rating'].tolist()[0]
    meanDf.set_value(name, 'Name', name)
    meanDf.set_value(name, 'Mean', mean)
    meanDf.set_value(name, 'Growth', growth)
    
df3 = pd.merge(allPlayers, meanDf, on=['Name'])

allPlayers = df3

allPlayers['Mean'] = allPlayers['Mean'].astype(np.float64)


allPlayers = allPlayers.sort_values(['Season', 'Name'])
# allPlayers.head()

transformedPlayerDf = allPlayers.copy()
transformedPlayerDf['Last_Season_Rating'] = transformedPlayerDf.groupby(['Name'])['Rating'].shift()
transformedPlayerDf['Last_Season_Diff'] = transformedPlayerDf.groupby('Name')['Last_Season_Rating'].transform(Series.diff)
transformedPlayerDf = transformedPlayerDf.dropna()
transformedPlayerDf.head()

accuracy = []


for season in range(2015,2019):
    train = transformedPlayerDf[transformedPlayerDf['Season'] == season-1]
    val = transformedPlayerDf[transformedPlayerDf['Season'] == season]

    xtr, xts = train.drop(['Rating', 'Name', 'Season'], axis=1), val.drop(['Rating', 'Name', 'Season'], axis=1)
    ytr, yts = train['Rating'].values, val['Rating'].values

    reg = linear_model.LinearRegression(n_jobs=-1) 
    
    reg.fit(xtr, ytr)
    

    p = reg.predict(xts)


    from sklearn.model_selection import cross_val_score
    from sklearn import model_selection
    scores = cross_val_score(reg, xts, yts, cv=10)
    accuracy.append(scores.mean())
    
print(accuracy)    
mean(accuracy)


#Let's automate

for season in range(2018, 2019):
    
    previousPlayers = allPlayers.loc[allPlayers.Season == season].copy()
    currentPlayers = allPlayers.loc[allPlayers.Season == season+1].copy()
    futurePlayers = currentPlayers.copy()
    
#     print(previousPlayers)
#     print(currentPlayers)

    futurePlayers['Season'] = currentPlayers['Season'].values+1
    futurePlayers['Age'] = currentPlayers['Age'].values+1

    futurePlayers.drop(['Rating'], axis=1)

    li = []
    li.append(previousPlayers)
    li.append(currentPlayers)
    li.append(futurePlayers)

    combinedDf = pd.concat(li)
    
    combinedDf = combinedDf.sort_values(['Season', 'Name'])

    transformedPlayerDf = combinedDf.copy()
    transformedPlayerDf['Last_Season_Rating'] = transformedPlayerDf.groupby(['Name'])['Rating'].shift()
    transformedPlayerDf['Last_Season_Diff'] = transformedPlayerDf.groupby('Name')['Last_Season_Rating'].transform(Series.diff)
    transformedPlayerDf = transformedPlayerDf.dropna()
    
#     transformedPlayerDf = transformedPlayerDf[transformedPlayerDf['Season'] != season+1]
    transformedPlayerDf = transformedPlayerDf.loc[transformedPlayerDf['Season'] == season+2]
    print(transformedPlayerDf)
    
    xts = transformedPlayerDf.drop(['Rating', 'Name', 'Season'], axis=1)
    p = reg.predict(xts)

    ratings = ["{:.2f}".format(value) for value in p.tolist()]
    transformedPlayerDf['Rating'] = ratings
    transformedPlayerDf = transformedPlayerDf[['Name', 'Season', 'Rating', 'Age', 'Mean', 'Growth']]
    allPlayers = allPlayers.append(transformedPlayerDf)
    print(transformedPlayerDf)
#     print(allPlayers)
    
allPlayers = allPlayers[allPlayers['Rating'].notnull()].copy()
allPlayers['Rating'] = allPlayers['Rating'].astype(float)