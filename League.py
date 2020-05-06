import requests
from .Team import Team

def get_teams(limit=100):
    response = requests.get('https://api.overwatchleague.com/v2/teams')
    teams = response.json()['data']

    if limit > len(teams):
        limit = len(teams)

    team_objects = []
    for team in teams:
        team_objects.append(Team(team['id']))
    
    return team_objects