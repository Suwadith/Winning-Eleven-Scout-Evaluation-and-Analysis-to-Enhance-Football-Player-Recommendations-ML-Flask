# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:10:17 2020

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

#combining all the DFs'

combinedPlayerDataframe = pd.concat([combinedOffensivePlayerDataframe, combinedDefensivePlayerDataframe, combinedPassingPlayerDataframe, combinedSummaryPlayerDataframe], axis=1)

combinedPlayerDataframe = combinedPlayerDataframe.loc[:,~combinedPlayerDataframe.columns.duplicated()]

#Removing all the goal keepers to test whether it improves the accuracy of the model.
#combinedFieldPlayersDf = combinedPlayerDataframe[combinedPlayerDataframe.Position != 'GK']

#Removing field players who have played less than 10 matches
#combinedProperFieldPlayersDf = combinedFieldPlayersDf[~(combinedFieldPlayersDf['Apps'] < 8)]  

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

idList = allPLayers.id.unique()

meanDf = pd.DataFrame(columns=['Mean'])

#idList = allPLayers.id

for idx in idList:
    mean = allPLayers.loc[allPLayers.id == idx]['Rating'].mean()
    length = len(allPLayers.loc[allPLayers.id == idx]['Rating'])
    growth = allPLayers.loc[allPLayers.id == idx]['Rating'].tolist()[length-1] - allPLayers.loc[allPLayers.id == idx]['Rating'].tolist()[0]
    meanDf.set_value(idx, 'id', idx)
    meanDf.set_value(idx, 'Mean', mean)
    meanDf.set_value(idx, 'Growth', growth)
    
df3 = pd.merge(allPLayers, meanDf, on=['id'])

allPLayers = df3

allPLayers['Mean'] = allPLayers['Mean'].astype(np.float64)

#allPLayers.loc[allPLayers.id == 3]['Rating']

from pandas import Series
from pandas import DataFrame
from pandas import concat

allPLayers = allPLayers.sort_values(['Season', 'id'])
allPLayers.head()

players_ratings_df2 = allPLayers.copy()
players_ratings_df2['Last_Season_Rating'] = players_ratings_df2.groupby(['id'])['Rating'].shift()
players_ratings_df2['Last_Season_Diff'] = players_ratings_df2.groupby('id')['Last_Season_Rating'].transform(Series.diff)
players_ratings_df2 = players_ratings_df2.dropna()
# players_ratings_df2 = players_ratings_df2.fillna(-99999, inplace=True)
players_ratings_df2.head()

 from sklearn.metrics import mean_squared_log_error

def rmsle(ytrue, ypred):
    return np.sqrt(mean_squared_log_error(ytrue, ypred))

from sklearn.ensemble import RandomForestRegressor

mean_error = []
for season in range(2018,2019):
    train = players_ratings_df2[players_ratings_df2['Season'] < season]
    val = players_ratings_df2[players_ratings_df2['Season'] == season]

    xtr, xts = train.drop(['Rating'], axis=1), val.drop(['Rating'], axis=1)
    ytr, yts = train['Rating'].values, val['Rating'].values
    

    mdl = RandomForestRegressor(n_estimators=500, n_jobs=-1, random_state=0, min_samples_split = 60,  
                                min_samples_leaf=5, max_depth = 30, max_features = 'sqrt')
    mdl.fit(xtr, ytr)
    

    p = mdl.predict(xts)

    error = rmsle(yts, p)
    print('Week %d - Error %.5f' % (season, error))
    mean_error.append(error)
print('Mean Error = %.5f' % np.mean(mean_error))


from sklearn.model_selection import cross_val_score
from sklearn import model_selection
scores = cross_val_score(mdl, xts, yts, cv=10)
print(scores)
print(scores.mean())


import xgboost as xgb

mean_error = []
for season in range(2016,2019):
    train = players_ratings_df2[players_ratings_df2['Season'] < season]
    val = players_ratings_df2[players_ratings_df2['Season'] == season]

    xtr, xts = train.drop(['Rating'], axis=1), val.drop(['Rating'], axis=1)
    ytr, yts = train['Rating'].values, val['Rating'].values

    reg = xgb.XGBRegressor(objective ='reg:squarederror', max_depth=2, subsample=1, n_estimators=70)
    
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



from sklearn import linear_model 

mean_error = []
for season in range(2016,2019):
    train = players_ratings_df2[players_ratings_df2['Season'] < season]
    val = players_ratings_df2[players_ratings_df2['Season'] == season]

    xtr, xts = train.drop(['Rating'], axis=1), val.drop(['Rating'], axis=1)
    ytr, yts = train['Rating'].values, val['Rating'].values

    reg = linear_model.LinearRegression(n_jobs=-1) 
    
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