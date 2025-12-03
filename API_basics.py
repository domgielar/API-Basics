from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import matplotlib.pyplot as pyplot
import pandas as pd

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key,value in dict_.items():
            out_dict[key].append(value)
    return out_dict

nba_teams = teams.get_teams()
#print(nba_teams[0:3])

dict_nba_teams=one_dict(nba_teams)
df_teams = pd.DataFrame(dict_nba_teams)

df_celtics = df_teams[df_teams["nickname"]=="Celtics"]
print(df_celtics)

id_celtics = df_celtics[["id"]].values[0][0]
print(id_celtics)

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_celtics)
gamefinder.get_json()
games = gamefinder.get_data_frames()[0]
print(games.head())