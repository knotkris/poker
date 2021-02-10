from player import Player
from typing import List
from card_ranks import CardRanks

def parse_player(inp: str, hand_len: int)->Player:
    if inp:
        inputs = inp.split()

        if len(inputs) != hand_len + 1:
            raise ValueError # failed to give sufficient values for given hand size
            
        return Player(inputs[0], inputs[1:])

    raise ValueError

def parse_input(hand_len: int)->List[Player]:
    users_cnt = 0
    players = []
    #parse user input
    while True:
        try:
            line = input()
            if not line: break
            if users_cnt == 0: #first line should be number of players
                users_cnt = int(line)
            else:
                p = parse_player(line, hand_len) # get player from input
                p.rank_hand() # ranking user hand
                players.append(p)
        except EOFError: #breaks loop when reaching input end
            break
        except ValueError:
            raise ValueError
    
    if users_cnt != len(players):
        raise ValueError #incorrect input for number of players

    return players

def determine_winner(hand_len: int)->str:
    players = parse_input(hand_len)

    winner = []
    max_rank = -1
    curr_highest_card = 0
    curr_high_pair = 0
    print(players)
    for p in players:
        if p.hand_ranking > max_rank: # save the higher hand
            max_rank = p.hand_ranking
            winner = [str(p.id)]
            curr_highest_card = p.highest_card
            curr_high_pair = p.high_card_pair
        elif p.hand_ranking == max_rank: # in case of tie we check the highest card
            # special case for pairs where the highest pair takes the win
            if p.hand_ranking == CardRanks.PAIR.value:
                if p.high_card_pair > curr_high_pair:
                    winner = [str(p.id)]
                    curr_high_pair = p.high_card_pair
                    continue # more to next player 
            # if the pairs tie then check highest card
            if (p.highest_card == curr_highest_card): # if its a tie then there are more than one winners
                winner.append(str(p.id))
            elif p.highest_card > curr_highest_card: # overwrite winner with new highest card player
                winner = [str(p.id)]
                curr_highest_card = p.highest_card
    print(" ".join(winner))


if __name__ == "__main__":
    hand_len = 3 # used to determine the amount of cards for each player
    determine_winner(hand_len)



