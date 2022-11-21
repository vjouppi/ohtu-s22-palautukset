import requests
from player import Player
from datetime import datetime

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        if player_dict['nationality'] == 'FIN':
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games']
            )

            players.append(player)

    print("Players from FIN " + str(datetime.now()) + "\n")

    for player in players:
        print(str(player) + " team " + player.team + " goals " + str(player.goals) + " assists " + str(player.assists))
if __name__ == "__main__":
    main()
