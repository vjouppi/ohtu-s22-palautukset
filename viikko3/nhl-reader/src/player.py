class Player:
    def __init__(self, name, nat, ass, goal, pen, team, games):
        self.name = name
        self.nationality = nat
        self.assists = ass
        self.goals = goal
        self.penalties = pen
        self.team = team
        self.games = games
        self.points = self.assists + self.goals
    
    def __str__(self):
        return self.name
