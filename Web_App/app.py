from flask import Flask, render_template, request, jsonify
# from data import load_league_names, load_team_names, \
#     predict_older_player_replacements, predict_under_performing_player_replacements, get_current_squad_df
from Recommendation import Recommendation
from Forecast import Forecast

app = Flask(__name__)

recommendation = Recommendation()

leagues = recommendation.load_league_names()


@app.route('/', methods=['GET', 'POST'])
def load_leagues():
    return render_template('select_league.html', leagues=leagues)


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)


@app.route('/select_team', methods = ['GET','POST'])
def load_teams():
    league = request.form['league']
    # print(league) #This is the posted value
    teams = recommendation.load_team_names(league)
    return render_template('select_team.html', teams=teams)


@app.route('/predict', methods = ['GET','POST'])
def load_prediction_data():
    team = request.form['team']
    current_squad = recommendation.get_current_squad_df(team)
    old_players_dict = recommendation.predict_older_player_replacements(team)
    active_players_dict = recommendation.predict_under_performing_player_replacements(team)
    return render_template('predict.html', team_name=team, current_squad=current_squad, old_players_dict=old_players_dict, active_players_dict=active_players_dict)


@app.route('/forecast', methods = ['GET','POST'])
def load_forecast_data():
    forecast = Forecast()
    forecast.forecast()
    return render_template('select_league.html', leagues=leagues)
