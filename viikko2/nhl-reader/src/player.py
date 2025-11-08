import requests
class Player:
    def __init__(self, data):
        self.name = data.get('name')
        team = data.get('team')
        if isinstance(team, list):
            self.team = ', '.join(team)
        else:
            self.team = team
        self.nationality = data.get('nationality')
        self.goals = data.get('goals')
        self.assists = data.get('assists')
        self.points = self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.goals} + {self.assists} = {self.points}"
    
class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()
        self.players = [Player(p) for p in response]

    def get_players(self):
        return self.players
    
class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered = [p for p in self.players if p.nationality == nationality]
        filtered.sort(key=lambda p: p.points, reverse=True)
        return filtered

