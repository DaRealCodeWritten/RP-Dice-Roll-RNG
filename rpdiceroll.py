import random
def roll(players: dict):
    passes = len(players)
    currentpass = 0
    for _ in range(passes):
        current = list(players.keys())[currentpass]
        for _ in range(6):
            rolled = random.randint(0, 10)
            if rolled == 0:
                while rolled == 0:
                    rolled = random.randint(0, 10)
            playerlist = players.get(current)
            playerlist.append(rolled)
            players[current] = playerlist
        currentpass += 1
    print (players)
    return players

def parse_rolls(players: dict):
    players_successes = {}
    players_damage = {}
    players_total = {}
    for name in players.keys():
        players_successes[name] = 0
        players_damage[name] = 0
        players_total[name] = 0
    for player in players.keys():
        rolled_dmg = random.randint(1, 6)
        players_damage[player] = rolled_dmg
    for name, rolls in players.items():
        for i in rolls:
            if i >= 8:
                players_successes[name] += 1
    for player in players:
        print (f"{player} got {players_successes[player]} successes and a damage of {players_damage[player]}\n{player}'s damage totals out at {players_damage[player]*players_successes[player]}")
    
while True:
    player = input("Input the first player's name: ")
    isanother = input("Is there another player? (y/n)")
    if isanother == "y":
        player2 = input("Input the second player's name: ")
        isanother = input("Is there another player? (y/n)")
        if isanother == "y":
            player3 = input("Input the second third's name: ")
            player_names = [player, player2, player3]
            player_dict = {}
            for play in player_names:
                player_dict[play] = []
            ret = roll(player_dict)
            parse_rolls(ret)
        else:
            player_names = [player, player2]
            player_dict = {}
            for play in player_names:
                player_dict[play] = []
            ret = roll(player_dict)
            parse_rolls(ret)
    else:
        player_names = [player]
        player_dict = {}
        for play in player_names:
            player_dict[play] = []
        ret = roll(player_dict)
        parse_rolls(ret)
