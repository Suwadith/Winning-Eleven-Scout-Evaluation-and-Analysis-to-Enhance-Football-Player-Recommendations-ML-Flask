import pandas as pd
import re

combined_league_data_frame = pd.read_csv("static/datasets/League-Team.csv")
combined_player_data_frame = pd.read_csv("static/datasets/Preprocessed Player Data.csv")
forecasted_player_data_frame = pd.read_csv("static/datasets/Forecasted Ratings 2019-2022.csv")


def load_league_names():
    leagues = combined_league_data_frame.League.unique().tolist()
    league_dict = {}
    for i in leagues:
        league_dict[i] = re.sub(r"(\w)([A-Z])", r"\1 \2", i)
    return league_dict


def load_team_names(league):
    teams = combined_league_data_frame.loc[combined_league_data_frame.League == league]['Team'].tolist()
    return teams


def organize_young_player_data():
    young_players2018_df = forecasted_player_data_frame.loc[(forecasted_player_data_frame.Season == 2018)
                                                       & ((forecasted_player_data_frame.Age > 22)
                                                          & (forecasted_player_data_frame.Age < 29))]

    young_player_names = young_players2018_df.Name.tolist()

    young_players_ = {}

    for name in young_player_names:
        player_mean_rating = forecasted_player_data_frame.loc[(forecasted_player_data_frame.Name == name)]['Rating'].mean()
        player_df = combined_player_data_frame.loc[(combined_player_data_frame.Name == name)]
        player_df = player_df.sort_values(by='Age', ascending=True)
        player_df.loc['average'] = player_df.mean()
        player_df.loc['average', 'Name'] = name
        player_df.loc['average', 'Team'] = player_df['Team'][player_df.index[-2]]
        player_df.loc['average', 'Position'] = player_df['Position'][player_df.index[-2]]
        player_df.loc['average', 'League'] = player_df['League'][player_df.index[-2]]
        player_df.loc['average', 'Rating'] = player_mean_rating
        player_df = player_df.iloc[-1:]
        young_players_[name] = player_df

    position_young_players_ = {}

    midfielders = []
    forwards = []
    attacking_midfielders = []
    defenders = []
    goalkeepers = []
    defensive_midfielders = []

    for name in young_players_:
        position = young_players_[name].Position.tolist()[0]
        if position == 'Midfielder':
            midfielders.append(young_players_[name])
        if position == 'Forward':
            forwards.append(young_players_[name])
        if position == 'Attacking Midfielder':
            attacking_midfielders.append(young_players_[name])
        if position == 'Defender':
            defenders.append(young_players_[name])
        if position == 'Goalkeeper':
            goalkeepers.append(young_players_[name])
        if position == 'Defensive Midfielder':
            defensive_midfielders.append(young_players_[name])

    position_young_players_['Midfielder'] = pd.concat(midfielders)
    position_young_players_['Forward'] = pd.concat(forwards)
    position_young_players_['Attacking Midfielder'] = pd.concat(attacking_midfielders)
    position_young_players_['Defender'] = pd.concat(defenders)
    position_young_players_['Goalkeeper'] = pd.concat(goalkeepers)
    position_young_players_['Defensive Midfielder'] = pd.concat(defensive_midfielders)

    return position_young_players_


position_young_players_ = organize_young_player_data()


def predict_older_player_replacements(team):

    older_players_df = combined_player_data_frame.loc[(combined_player_data_frame.Team == team)
                                                 & (combined_player_data_frame.Season == 2018)
                                                 & (combined_player_data_frame.Age > 32)]

    older_players_ = {}

    for index, row in older_players_df.iterrows():
        current_df = combined_player_data_frame.loc[(combined_player_data_frame.Name == row['Name'])
                                                & (combined_player_data_frame.Age > 23)
                                                & (combined_player_data_frame.Age < 30)]
        
        current_df = current_df.sort_values(by='Age', ascending=True)
        current_df.loc['average'] = current_df.mean()
        current_df.loc['average', 'Name'] = row['Name']
        current_df.loc['average', 'Team'] = current_df['Team'][current_df.index[-2]]
        current_df.loc['average', 'Position'] = current_df['Position'][current_df.index[-2]]
        current_df.loc['average', 'League'] = current_df['League'][current_df.index[-2]]
        current_df = current_df.iloc[-1:]
        older_players_[row['Name']] = current_df

    li = []

    for name in older_players_:
        position = older_players_[name].Position.tolist()[0]
        li.append(older_players_[name])
        young_df = position_young_players_[position]
        young_df = young_df[young_df.Team != team]
        li.append(young_df)

        combined_df = pd.concat(li)

        stats = combined_df.copy(deep=True)
        stats.drop(['Name', 'Team', 'League', 'Position'], axis=1, inplace=True)

        stats_with_name = stats
        stats = stats.dropna()
        stats_with_name = stats_with_name.dropna()
        stats_with_name["Name"] = combined_df["Name"]

        stats_with_name = stats_with_name.reset_index(drop=True)

        from sklearn.preprocessing import StandardScaler
        from sklearn.neighbors import NearestNeighbors
        from sklearn.exceptions import DataConversionWarning

        import warnings
        warnings.filterwarnings(action="ignore", category=DataConversionWarning)

        scaler = StandardScaler()

        X = scaler.fit_transform(stats)

        knn = NearestNeighbors(n_neighbors=4, algorithm='ball_tree').fit(X)

        player_indexes = knn.kneighbors(X)[1]

        print("")
        print("Older Player: " + name)
        index = stats_with_name[stats_with_name["Name"] == name].index.tolist()[0]
        count = 1
        for i in player_indexes[index][1:]:
            print('Option ' + str(count) + ': ' + stats_with_name.iloc[i]["Name"])
            count += 1

        li = []


def predict_under_performing_player_replacements(team):
    active_club_players = combined_player_data_frame.loc[(combined_player_data_frame.Team == team)
                                                    & (combined_player_data_frame.Season == 2018)
                                                    & (combined_player_data_frame.Age > 27)
                                                    & (combined_player_data_frame.Age < 33)]

    active_player_names = active_club_players.Name.tolist()

    active_players_ = {}

    for name in active_player_names:
        previous_form_df = combined_player_data_frame.loc[(combined_player_data_frame.Name == name)
                                                      & (combined_player_data_frame.Age > 23)
                                                      & (combined_player_data_frame.Age < 28)]

        recent_form_df = combined_player_data_frame.loc[(combined_player_data_frame.Name == name)
                                                   & (combined_player_data_frame.Age > 27)
                                                   & (combined_player_data_frame.Age < 33)]

        previous_rating_avg = previous_form_df.Rating.mean()
        recent_rating_avg = recent_form_df.Rating.mean()
        decline = (previous_rating_avg - recent_rating_avg)

        if (recent_rating_avg < 8) & (decline >= 0.3):

            previous_form_df = previous_form_df.sort_values(by='Age', ascending=True)
            previous_form_df.loc['average'] = previous_form_df.mean()
            previous_form_df.loc['average', 'Name'] = name
            previous_form_df.loc['average', 'Team'] = previous_form_df['Team'][previous_form_df.index[-2]]
            previous_form_df.loc['average', 'Position'] = previous_form_df['Position'][previous_form_df.index[-2]]
            previous_form_df.loc['average', 'League'] = previous_form_df['League'][previous_form_df.index[-2]]
            previous_form_df = previous_form_df.iloc[-1:]
            active_players_[name] = previous_form_df

        elif (recent_rating_avg < 7) & (decline >= 0.2):

            previous_form_df = previous_form_df.sort_values(by='Age', ascending=True)
            previous_form_df.loc['average'] = previous_form_df.mean()
            previous_form_df.loc['average', 'Name'] = name
            previous_form_df.loc['average', 'Team'] = previous_form_df['Team'][previous_form_df.index[-2]]
            previous_form_df.loc['average', 'Position'] = previous_form_df['Position'][previous_form_df.index[-2]]
            previous_form_df.loc['average', 'League'] = previous_form_df['League'][previous_form_df.index[-2]]
            previous_form_df = previous_form_df.iloc[-1:]
            active_players_[name] = previous_form_df

    li = []

    for name in active_players_:
        position = active_players_[name].Position.tolist()[0]
        li.append(active_players_[name])
        young_df = position_young_players_[position]
        young_df = young_df[young_df.Team != team]
        li.append(young_df)

        combined_df = pd.concat(li)

        stats = combined_df.copy(deep=True)
        stats.drop(['Name', 'Team', 'League', 'Position'], axis=1, inplace=True)

        stats_with_name = stats
        stats = stats.dropna()
        stats_with_name = stats_with_name.dropna()
        stats_with_name["Name"] = combined_df["Name"]

        stats_with_name = stats_with_name.reset_index(drop=True)

        from sklearn.preprocessing import StandardScaler
        from sklearn.neighbors import NearestNeighbors
        from sklearn.exceptions import DataConversionWarning

        import warnings
        warnings.filterwarnings(action="ignore", category=DataConversionWarning)

        scaler = StandardScaler()

        X = scaler.fit_transform(stats)

        knn = NearestNeighbors(n_neighbors=4, algorithm='ball_tree').fit(X)

        player_indexes = knn.kneighbors(X)[1]

        print("")
        print("Active Underperfoming Player: " + name)
        index = stats_with_name[stats_with_name["Name"] == name].index.tolist()[0]
        count = 1
        for i in player_indexes[index][1:]:
            print('Option ' + str(count) + ': ' + stats_with_name.iloc[i]["Name"])
            count += 1

        li = []

