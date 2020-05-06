import requests

class Player:
    stats_array = requests.get(f"https://api.overwatchleague.com/stats/players").json()['data']

    def __init__(self,id):
        try:
            self.id = id
            self.stats = []
            response = requests.get(f"https://api.overwatchleague.com/players/{ id }")
            self._player_data = response.json()['data']['player']
            self.name = self._player_data['name']
            for item in Player.stats_array:
                if item['playerId'] == id:
                    self.stats = item
        except:
            print("ERROR: Player invalid")
    
    def __repr__(self):
        return self.name