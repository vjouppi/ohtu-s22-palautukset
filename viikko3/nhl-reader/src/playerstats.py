class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        allplayers = self.reader.get_players()
        players = []
        for player in allplayers:
            if player.nationality == nationality:
                players.append(player)

        players.sort(key=lambda x: x.points, reverse = True)

        return players
        
