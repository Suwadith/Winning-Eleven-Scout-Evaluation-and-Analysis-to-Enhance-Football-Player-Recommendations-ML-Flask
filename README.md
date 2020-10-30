![1](https://github.com/Suwadith/Winning-Eleven-Scout-Evaluation-and-Analysis-to-Enhance-Football-Player-Recommendations-ML-Flask/blob/master/Web_App/static/images/logo.jpg)

# Scout-Evaluation-and-Analysis-to-Enhance-Football-Player-Recommendations-ML-Flask

This was my research project which was developed during my final year of my undergradute study. 

## Project Overview

* Every football club has a fair share of both youth and veteran players. 
* Every player’s development slows down after a certain age and then the club is forced to replace them with younger players. 
* The process of identifying suitable younger players for clubs is called scouting. 
* This process is hugely affected by human bias. There have been countless examples of questionable player transfers in the past.
* Furthermore, due to uncertainty in the economic climates like inflation and plagues like COVID-19 has forced clubs to spend money wisely and purchase players for the club based on statistics with the help of technology. 
* This project proposes an automated recommendation system that involves machine learning concepts to help clubs accurately identify aging and underperforming players who need to be replaced and recommends young players who can replace them. 
* The Winning Eleven (I'm so sorry PES. Had to steal both your original name & the logo :p) system analyses player performances using a decade of actual football data which is comprised of different technical aspects of a footballer. 
* The system uses a combination of multiple machine learning algorithms to analyze and make accurate predictions.

## Directories

1. Analysis
    1. Analyzing League Data.ipynb - Analyzing individual europe's top 5 league tabel data (2009-2018)
    2. Analyzing Player Performances.ipynb - Analyzing individual player performances (2009-2018)
    3. Data Preprocessing.ipynb
    4. Forecasting Active Player Ratings.ipynb - Forecasting future player ratings based on their yearly performance growth/drop (Linear regression + Rolling window approach)
    5. Identifying potential transfer targets.ipynb - Recommending 3 most suitable younger replacements from other clubs to replace underperforming/aging squad players (K Nearest Neighbors) 
2. Datasets
    1. Whoscored.com individual player stats (2009-2018)
    2. Whoscored.com league table stats (2009-2018)
3. Models
    1. Forecasting LR model file
    2. Player Recommendation KNN model file 
4. Pre_Processed_Datasets (Contains both Preprocessed datasets and a Predicted output dataset (Recommendation))
5. Visualization (Contains initial Tableau data visualization attempts (Not used))
6. Web_App (Python + Flask based web application)
7. Web_Scrapers (Python + Selenium based tools)
    1. Whoscored.com individual player stats scraper
    2. Whoscored.com league table stats scraper

## Demo
https://suwadith.pythonanywhere.com