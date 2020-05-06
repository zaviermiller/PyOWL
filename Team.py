import requests
from .Player import Player

class Team:
    def __init__(self,id):
        self.id = id
        response = requests.get(f"https://api.overwatchleague.com/v2/teams/{ id }")
        self.__team_data = response.json()['data']
        self.placement = self.__team_data['placement']
        self.name = self.__team_data['name']

    def __repr__(self):
        return self.name