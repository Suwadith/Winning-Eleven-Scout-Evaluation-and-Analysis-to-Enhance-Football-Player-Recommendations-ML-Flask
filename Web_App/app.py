from flask import Flask, render_template, request, jsonify
import numpy as np
import traceback
import pickle
import pandas as pd
import re
from data import load_leagueNames, load_teamNames

app = Flask(__name__)

leagues = load_leagueNames()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', leagues=leagues)


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)

@app.route('/selectTeam', methods = ['GET','POST'])
def postTesting():
    league = request.form['league']
    print(league) #This is the posted value
    teams = load_teamNames(league)
    return render_template('team_select.html.', teams=teams)
