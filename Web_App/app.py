from flask import Flask, render_template, request, jsonify
import numpy as np
import traceback
import pickle
import pandas as pd
import re

app = Flask(__name__)

combinedLeagueDataframe = pd.read_csv("static/datasets/League-Team.csv")
combinedPlayerDataframe = pd.read_csv("static/datasets/Preprocessed Player Data.csv")
forecastedPlayerDataframe = pd.read_csv("static/datasets/Forecasted Ratings 2019-2022.csv")

@app.route('/')
def index():
    leagues = load_leagueNames()
    return render_template('index.html', leagues=leagues)


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)

#
# def load_datasets():

def load_leagueNames():
    leagues = combinedLeagueDataframe.League.unique().tolist()
    leagueDict = {}
    for i in leagues:
        leagueDict[i] = re.sub(r"(\w)([A-Z])", r"\1 \2", i)
    return leagueDict