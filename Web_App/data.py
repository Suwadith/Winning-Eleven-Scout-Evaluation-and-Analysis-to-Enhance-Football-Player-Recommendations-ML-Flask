import pandas as pd
import re

combinedLeagueDataframe = pd.read_csv("static/datasets/League-Team.csv")
combinedPlayerDataframe = pd.read_csv("static/datasets/Preprocessed Player Data.csv")
forecastedPlayerDataframe = pd.read_csv("static/datasets/Forecasted Ratings 2019-2022.csv")


def load_leagueNames():
    leagues = combinedLeagueDataframe.League.unique().tolist()
    leagueDict = {}
    for i in leagues:
        leagueDict[i] = re.sub(r"(\w)([A-Z])", r"\1 \2", i)
    return leagueDict

def load_teamNames(league):
    teams = combinedLeagueDataframe.loc[combinedLeagueDataframe.League == league]['Team'].tolist()
    return teams