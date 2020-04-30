#Importing Libraries
import numpy as np
import pandas as pd
import warnings
#Disable warning messages
warnings.simplefilter(action='ignore', category=FutureWarning)

class Forecast:

    # importing datatset
    combined_player_data_frame = pd.read_csv("static/datasets/Preprocessed Player Data.csv")

    def __init__(self):
        output = self.feature_engineering()
        self.all_players_data_frame = output[0]
        self.transformed_players_data_frame = output[1]


    def feature_engineering(self):
        # selecting relevant columns needed to forecast player ratings.
        all_players_data_frame = self.combined_player_data_frame[['Name', 'Season', 'Rating', 'Age']]
        all_players_data_frame = all_players_data_frame[all_players_data_frame['Season'].notnull()].copy()
        all_players_data_frame['Season'] = all_players_data_frame['Season'].astype(int)
        all_players_data_frame
        # Store a list of all the players
        name_list = all_players_data_frame.Name.unique()

        # creating a dataframe just to store the mean values of player rating's
        mean_data_frame = pd.DataFrame(columns=['Mean'])

        # Calculating career growth and rating average of every player (Feature engineering)
        for name in name_list:
            # getting all the mean values of the attributes
            mean = all_players_data_frame.loc[all_players_data_frame.Name == name]['Rating'].mean()
            length = len(all_players_data_frame.loc[all_players_data_frame.Name == name]['Rating'])
            # calculating overall player rating growth (current - beginning)
            growth = all_players_data_frame.loc[all_players_data_frame.Name == name]['Rating'].tolist()[length - 1] - \
                     all_players_data_frame.loc[all_players_data_frame.Name == name]['Rating'].tolist()[0]
            mean_data_frame.set_value(name, 'Name', name)
            mean_data_frame.set_value(name, 'Mean', mean)
            mean_data_frame.set_value(name, 'Growth', growth)

        # Merging all the data together
        all_players_data_frame = pd.merge(all_players_data_frame, mean_data_frame, on=['Name'])

        # Converting column type
        all_players_data_frame['Mean'] = all_players_data_frame['Mean'].astype(np.float64)

        # Another portion of feature engineering
        from pandas import Series

        all_players_data_frame = all_players_data_frame.sort_values(['Season', 'Name'])

        # Creating 2 new features for every player by combining both the last season rating
        # and the difference between that and the previous season rating
        transformed_players_data_frame = all_players_data_frame.copy()
        transformed_players_data_frame['Last_Season_Rating'] = transformed_players_data_frame.groupby(['Name'])['Rating'].shift()
        transformed_players_data_frame['Last_Season_Diff'] = transformed_players_data_frame.groupby('Name')['Last_Season_Rating'].transform(Series.diff)
        transformed_players_data_frame = transformed_players_data_frame.dropna()
        transformed_players_data_frame.head()

        data_frame_array = []
        data_frame_array.append(all_players_data_frame)
        data_frame_array.append(transformed_players_data_frame)

        return data_frame_array

    def forecast(self):
        from pandas import Series
        from sklearn import linear_model

        lin_reg = linear_model.LinearRegression(n_jobs=-1)

        # For every season using previous season data to forecast current season rating
        for season in range(2015, 2019):
            training_set = self.transformed_players_data_frame[self.transformed_players_data_frame['Season'] == season - 1]

            X_train = training_set.drop(['Rating', 'Name', 'Season'], axis=1)
            y_train = training_set['Rating'].values

            lin_reg.fit(X_train, y_train)

        # Forecasting player ratings between 2019-2022
        for season in range(2017, 2021):
            previousPlayers = self.all_players_data_frame.loc[self.all_players_data_frame.Season == season].copy()
            currentPlayers = self.all_players_data_frame.loc[self.all_players_data_frame.Season == season + 1].copy()
            futurePlayers = currentPlayers.copy()

            futurePlayers['Season'] = currentPlayers['Season'].values + 1
            futurePlayers['Age'] = currentPlayers['Age'].values + 1

            futurePlayers.drop(['Rating'], axis=1)

            li = []
            li.append(previousPlayers)
            li.append(currentPlayers)
            li.append(futurePlayers)

            combined_player_data_frame = pd.concat(li)

            combined_player_data_frame = combined_player_data_frame.sort_values(['Season', 'Name'])

            self.transformed_players_data_frame = combined_player_data_frame.copy()
            self.transformed_players_data_frame['Last_Season_Rating'] = self.transformed_players_data_frame.groupby(['Name'])['Rating'].shift()
            self.transformed_players_data_frame['Last_Season_Diff'] = self.transformed_players_data_frame.groupby('Name')[
                'Last_Season_Rating'].transform(Series.diff)
            self.transformed_players_data_frame = self.transformed_players_data_frame.dropna()

            self.transformed_players_data_frame = self.transformed_players_data_frame.loc[self.transformed_players_data_frame['Season'] == season + 2]

            current_season_data_frame = self.transformed_players_data_frame.drop(['Rating', 'Name', 'Season'], axis=1)
            y_pred = lin_reg.predict(current_season_data_frame)

            # Attaching the predicted values to the original DF so that the cycle can continue until
            # the forecasting range comes to an end
            ratings = ["{:.2f}".format(value) for value in y_pred.tolist()]
            self.transformed_players_data_frame['Rating'] = ratings
            self.transformed_players_data_frame = self.transformed_players_data_frame[['Name', 'Season', 'Rating', 'Age', 'Mean', 'Growth']]
            self.all_players_data_frame = self.all_players_data_frame.append(self.transformed_players_data_frame)
            self.all_players_data_frame = self.all_players_data_frame[self.all_players_data_frame['Rating'].notnull()].copy()
            self.all_players_data_frame['Rating'] = self.all_players_data_frame['Rating'].astype(float)

        self.all_players_data_frame.to_csv('static/datasets/Forecasted Ratings 2019-2022.csv', index=False)
