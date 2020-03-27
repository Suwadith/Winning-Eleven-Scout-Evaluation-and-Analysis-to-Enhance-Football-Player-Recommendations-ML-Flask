# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:26:34 2020

@author: Suwadith
"""

#Importing Libraries
import numpy as np #To handle Mathematical calculations
import matplotlib.pyplot as plt #To plot charts 
import pandas as pd #TO import and manage datasets
import glob
import os
# pd.set_option('display.max_columns', None)  
# pd.set_option('display.max_rows', None)

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
            
#     individualOffensivePlayerDataframe = individualOffensivePlayerDataframe.drop_duplicates(subset=['Name'], keep='first')
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
    
#     individualOffensivePlayerDataframe = individualOffensivePlayerDataframe.drop_duplicates(subset=['Name'], keep='first')
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
    
#     individualOffensivePlayerDataframe = individualOffensivePlayerDataframe.drop_duplicates(subset=['Name'], keep='first')
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
    
#     individualOffensivePlayerDataframe = individualOffensivePlayerDataframe.drop_duplicates(subset=['Name'], keep='first')
    li.append(individualOffensivePlayerDataframe)

combinedSummaryPlayerDataframe = pd.concat(li)


######################################



#combining all the DFs'

combinedPlayerDataframe = pd.concat([combinedOffensivePlayerDataframe, combinedDefensivePlayerDataframe, combinedPassingPlayerDataframe, combinedSummaryPlayerDataframe], axis=1)

combinedPlayerDataframe = combinedPlayerDataframe.loc[:,~combinedPlayerDataframe.columns.duplicated()]

#Removing all the goal keepers to test whether it improves the accuracy of the model.
combinedFieldPlayersDf = combinedPlayerDataframe[combinedPlayerDataframe.Position != 'GK']

#Removing field players who have played less than 10 matches
#combinedProperFieldPlayersDf = combinedFieldPlayersDf[~(combinedFieldPlayersDf['Apps'] < 8)]



##########################################

allPLayers = combinedPlayerDataframe[['Name', 'Season', 'Rating']]
#allPLayers = combinedPlayerDataframe
allPLayers = allPLayers.assign(id=(allPLayers['Name']).astype('category').cat.codes)
del allPLayers['Name']
#del allPLayers['Team']
#del allPLayers['League']
#del allPLayers['Position']
cols = allPLayers.columns.tolist()
cols.insert(0, cols.pop(cols.index('id')))
allPLayers = allPLayers.reindex(columns= cols)
allPLayers["Season"] = pd.to_numeric(allPLayers["Season"])
allPLayers['id'] = allPLayers['id'].astype(np.int16)
#allPLayers['Rating'] = allPLayers['Rating'].astype(np.int16)
#allPLayers["Rating"] = 10 * allPLayers["Rating"]
#allPLayers['Rating'] = allPLayers['Rating'].astype(np.int16)
allPLayers.dtypes
#allPLayers = allPLayers.replace('-', 0)
###############



#melt3 = allPLayers.copy()
#melt3["Season"] = pd.to_numeric(melt3["Season"])
#melt3['Last_Season_Rating'] = melt3.groupby(['id'])['Rating'].shift()
#melt3['Last_Season_Diff'] = melt3['Last_Season_Rating'].diff()
##melt3['Last_Season_Diff'] = melt3['Last_Season_Rating'] + melt3['Rating']
#melt3.dropna()
#melt3.dtypes

from pandas import Series

allPLayers = allPLayers.sort_values(['Season', 'id'])
allPLayers.head()

players_ratings_df2 = allPLayers.copy()
players_ratings_df2['Last_Season_Rating'] = players_ratings_df2.groupby(['id'])['Rating'].shift()
#players_ratings_df2['Last_Season_Diff'] = players_ratings_df2.groupby(['id'])['Last_Season_Rating'].diff()
players_ratings_df2['Last_Season_Diff'] = players_ratings_df2.groupby('id')['Last_Season_Rating'].transform(Series.diff)
#players_ratings_df2['Last_Season_Tiff'] = players_ratings_df2.groupby('id')['Last_Season_Rating'] * 5
#players_ratings_df2['Last_Season_Diff'] = players_ratings_df2['Last_Season_Rating'] - players_ratings_df2['Rating'] 
#players_ratings_df2['Last-1_Season_Rating'] = players_ratings_df2.groupby(['id'])['Rating'].shift(2)
#players_ratings_df2['Last-1_Season_Diff'] = players_ratings_df2.groupby('id')['Last-1_Season_Rating'].transform(Series.diff)
#players_ratings_df2['Last-2_Season_Rating'] = players_ratings_df2.groupby(['id'])['Rating'].shift(3)
#players_ratings_df2['Last-2_Season_Diff'] = players_ratings_df2.groupby('id')['Last-2_Season_Rating'].transform(Series.diff)
#players_ratings_df2['Last-3_Season_Rating'] = players_ratings_df2.groupby(['id'])['Rating'].shift(4)
#players_ratings_df2['Last-3_Season_Diff'] = players_ratings_df2.groupby('id')['Last-3_Season_Rating'].transform(Series.diff)
#players_ratings_df2['Last-4_Season_Rating'] = players_ratings_df2.groupby(['id'])['Rating'].shift(5)
#players_ratings_df2['Last-4_Season_Diff'] = players_ratings_df2.groupby('id')['Last-4_Season_Rating'].transform(Series.diff)
#players_ratings_df2['Last-5_Season_Rating'] = players_ratings_df2.groupby(['id'])['Rating'].shift(6)
#players_ratings_df2['Last-5_Season_Diff'] = players_ratings_df2.groupby('id')['Last-5_Season_Rating'].transform(Series.diff)
#players_ratings_df2['Last-6_Season_Rating'] = players_ratings_df2.groupby(['id'])['Rating'].shift(7)
#players_ratings_df2['Last-6_Season_Diff'] = players_ratings_df2.groupby('id')['Last-6_Season_Rating'].transform(Series.diff)
#players_ratings_df2['Last-7_Season_Rating'] = players_ratings_df2.groupby(['id'])['Rating'].shift(8)
#players_ratings_df2['Last-7_Season_Diff'] = players_ratings_df2.groupby('id')['Last-7_Season_Rating'].transform(Series.diff)
#players_ratings_df2['Last-8_Season_Rating'] = players_ratings_df2.groupby(['id'])['Rating'].shift(9)
#players_ratings_df2['Last-8_Season_Diff'] = players_ratings_df2.groupby('id')['Last-8_Season_Rating'].transform(Series.diff)
#mean_value=players_ratings_df2['Rating'].mean()
#players_ratings_df2 = players_ratings_df2.fillna(mean_value)
#players_ratings_df2['rolling_mean'] = players_ratings_df2['Rating'].rolling(window=3).mean()
#players_ratings_df2 = players_ratings_df2[['Datetime', 'rolling_mean', 'Count']]

players_ratings_df2 = players_ratings_df2.dropna()
players_ratings_df2.head()




def rmsle(ytrue, ypred):
    return np.sqrt(mean_squared_log_error(ytrue, ypred))

from sklearn.metrics import mean_squared_log_error

#mean_error = []
#for season in range(2017,2018):
#    train = players_ratings_df2[players_ratings_df2['Season'] < season]
#    val = players_ratings_df2[players_ratings_df2['Season'] == season]
#
#    p = val['Last_Season_Rating'].values
#
#    error = rmsle(val['Rating'].values, p)
#    print('Season %d - Error %.5f' % (season, error))
#    mean_error.append(error)
#print('Mean Error = %.5f' % np.mean(mean_error))

from sklearn.ensemble import RandomForestRegressor
from sklearn import linear_model 
from sklearn.tree import DecisionTreeRegressor


mean_error = []
for season in range(2016,2019):
    train = players_ratings_df2[players_ratings_df2['Season'] < season]
    val = players_ratings_df2[players_ratings_df2['Season'] == season]

    xtr, xts = train.drop(['Rating'], axis=1), val.drop(['Rating'], axis=1)
    ytr, yts = train['Rating'].values, val['Rating'].values

#    reg = linear_model.LinearRegression(n_jobs=-1) 
    
    reg = DecisionTreeRegressor()

#    mdl = RandomForestRegressor(n_estimators=1000, n_jobs=-1, random_state=0)
    reg.fit(xtr, ytr)
    

    p = reg.predict(xts)

    error = rmsle(yts, p)
    print('Week %d - Error %.5f' % (season, error))
    mean_error.append(error)
print('Mean Error = %.5f' % np.mean(mean_error))

from sklearn.model_selection import cross_val_score
from sklearn import model_selection
scores = cross_val_score(reg, xts, yts, cv=10)
print(scores)
print(scores.mean())
#melt2 = allPLayers.copy()
#melt2["Season"] = pd.to_numeric(melt3["Season"])
#melt2['Last_Week_Sales'] = melt2.groupby(['Product_Code'])['Sales'].shift()
#melt2['Last_Week_Diff'] = melt2.groupby(['Product_Code'])['Last_Week_Sales'].diff()
#melt2 = melt2.dropna()
#melt2.head()
