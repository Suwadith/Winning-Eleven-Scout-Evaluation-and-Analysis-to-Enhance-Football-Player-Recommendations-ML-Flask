from flask import Flask, render_template, request, jsonify
from data import load_league_names, load_team_names, \
    predict_older_player_replacements, predict_under_performing_player_replacements, get_current_squad_df


app = Flask(__name__)

leagues = load_league_names()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', leagues=leagues)


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)


@app.route('/selectTeam', methods = ['GET','POST'])
def post_testing():
    league = request.form['league']
    # print(league) #This is the posted value
    teams = load_team_names(league)
    return render_template('team_select.html.', teams=teams)


@app.route('/displayResults', methods = ['GET','POST'])
def test():
    team = request.form['team']
    current_squad = get_current_squad_df(team)
    old_players_dict = predict_older_player_replacements(team)
    active_players_dict = predict_under_performing_player_replacements(team)
    print(current_squad)
    print(old_players_dict)
    print(active_players_dict)
    return render_template('displayResults.html', current_squad=current_squad, old_players_dict=old_players_dict, active_players_dict=active_players_dict)
