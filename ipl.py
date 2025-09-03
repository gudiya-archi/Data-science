import pandas as pd
import numpy as np

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRj9eesx6RBBnFY1UiP0L2c7skH4n0Kw5_hbnVmwdPi7t7Je2T6aZBoRgMvbplWP4GmP4Bsa50yBQ2J/pub?output=csv"
matches = pd.read_csv(ipl_matches)

print(matches.head())

def teamsAPI():
    teams =  list(set(list(matches['Team1']) + list(matches['Team2'])))
    team_dict = {
        'teams': teams

    }
    return team_dict

def teamVteamAPI(team1,team2):
    
    valid_teams =  teams =  list(set(list(matches['Team1']) + list(matches['Team2'])))
    
    if team1 in valid_teams and team2 in valid_teams:
        
        temp_df = matches[(matches['Team1'] == team1) & (matches['Team2'] == team2) | (matches['Team1'] == team2) & (matches['Team2'] == team1) ]
        total_matches = temp_df.shape[0]

        matches_won_team1 = temp_df['WinningTeam'].value_counts()[team1]
        matches_won_team2 = temp_df['WinningTeam'].value_counts()[team2]

        draws = total_matches - (matches_won_team1 + matches_won_team2)

        response = {
      'total_matches': str(total_matches),
      team1: str(matches_won_team1),
      team2: str(matches_won_team2),
      'draws': str(draws)
  }

        return response
    else:
        return{'message': 'invalid team name'}