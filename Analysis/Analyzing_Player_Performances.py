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
    
    li.append(individualOffensivePlayerDataframe)

combinedSummaryPlayerDataframe = pd.concat(li)

#Re-arranging the Dataframes to get sesasonal data of every attributes of players
nameSeasonOffensiveDF = combinedOffensivePlayerDataframe.pivot_table(index=['Name'], columns=['Season'], values=['Rating', 'Age', 'Team', 'League'], aggfunc='first').reset_index()
nameSeasonDefensiveDF = combinedDefensivePlayerDataframe.pivot_table(index=['Name'], columns=['Season'], values=['Rating', 'Age', 'Team', 'League'], aggfunc='first').reset_index()
nameSeasonPassingDF = combinedPassingPlayerDataframe.pivot_table(index=['Name'], columns=['Season'], values=['Rating', 'Age', 'Team', 'League'], aggfunc='first').reset_index()
nameSeasonOSummaryDF = combinedSummaryPlayerDataframe.pivot_table(index=['Name'], columns=['Season'], values=['Rating', 'Age', 'Team', 'League'], aggfunc='first').reset_index()

nameSeasonOffensiveDF.head()

#Switching the pivot table structure to a different form to analyse time series data 
seasonNameOffensiveDF = combinedOffensivePlayerDataframe.pivot_table(index=['Season'], columns=['Name'], values=['Rating', 'Age', 'Team', 'League'], aggfunc='first').reset_index()
seasonNameDefensiveDF = combinedDefensivePlayerDataframe.pivot_table(index=['Season'], columns=['Name'], values=['Rating', 'Age', 'Team', 'League'], aggfunc='first').reset_index()
seasonNamePassingDF = combinedPassingPlayerDataframe.pivot_table(index=['Season'], columns=['Name'], values=['Rating', 'Age', 'Team', 'League'], aggfunc='first').reset_index()
seasonNameSummaryDF = combinedSummaryPlayerDataframe.pivot_table(index=['Season'], columns=['Name'], values=['Rating', 'Age', 'Team', 'League'], aggfunc='first').reset_index()

seasonNameOffensiveDF.head()

#Testing the time series based dataset by plotting few players on a graph
ronaldoDf = combinedOffensivePlayerDataframe.loc[combinedOffensivePlayerDataframe['Name'] == 'Cristiano Ronaldo']
messiDf = combinedOffensivePlayerDataframe.loc[combinedOffensivePlayerDataframe['Name'] == 'Lionel Messi']
neymarDf = combinedOffensivePlayerDataframe.loc[combinedOffensivePlayerDataframe['Name'] == 'Neymar']
iniestaDF = combinedOffensivePlayerDataframe.loc[combinedOffensivePlayerDataframe['Name'] == 'Andrés Iniesta']

players = [ronaldoDf, messiDf, neymarDf, iniestaDF]

combinedPlayersDf = pd.concat(players)

tansformedCombinedPlayersDf = combinedPlayersDf.pivot_table(index=['Season'], columns=['Name'], values=['Rating', 'Age', 'Team', 'League'], aggfunc='first').reset_index()

tansformedCombinedPlayersDf.plot(x ='Season', y='Rating', kind = 'line')




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