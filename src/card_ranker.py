from typing import List
from card import Card

class CardRanker():
    def check_straight(self, hand: List[Card])->bool:
        #if all cards ordered by rank are only +1 away then it is a straight
        if not hand: return False

        ranks = [c.get_rank_int() for c in hand if c.rank != "A"]

        #get number of aces
        ace_cnt = len(hand) - len(ranks)

        # if there is more than one ace cant be a straight
        if ace_cnt > 1: 
            return False

        # sort ranks
        ranks.sort()

        prev = None
        # checks to see if the cards follow the n+1 pattern
        for c in ranks:
            if not prev:
                prev = c
                continue
            
            if c != prev + 1:
                return False

            prev = c
        
        # if there was one ace and the sequence of ranks is valid, then we need to check
        # then we need to check if either the first card is a 2 or the last card is a king\
        if ace_cnt == 1:
            return ranks[0] == 2 or ranks[len(ranks)-1] == 13

        # sequence without aces is valid
        return True

    def check_flush(self, hand: List[Card])->bool:
        if not hand: return False

        # converts the hand to a set of suits
        # there should only be one suit if it is a flush
        return len(set([c.suit for c in hand])) == 1

    def check_three_of_a_kind(self, hand: List[Card])->bool:
        # checks to see if the same rank shows up 2 times
        return self.check_n_of_a_kind(hand, 3) > -1

    def check_pair(self, hand: List[Card])->(bool, int):
        # checks to see if the same rank shows up 2 times
        pairRank = self.check_n_of_a_kind(hand, 2)

        #returns both the status and rank value to later check high pair for ties
        return pairRank != -1, pairRank

    # return rank if rank was found n times, else return -1
    def check_n_of_a_kind(self, hand: List[Card], n: int)->int:
        if not hand: return False

        freq = dict()
        # creates a frequency count of all the ranks
        for c in hand:
            if c.get_rank_int() in freq:
                freq[c.get_rank_int()] = freq[c.get_rank_int()] + 1
            else:
                freq[c.get_rank_int()] = 1
        
        # the same rank showed up n times
        for rank, f in freq.items():
            if f == n:
                return rank

        return -1
    
    def highest_rank(self, hand: List[Card])->int:
        max_rank = 0

        for c in hand:
            max_rank = max(max_rank, c.get_rank_int())
        
        return max_rank

    def highest_remaining(self, hand: List[Card], pairRank: int)->int:
        max_rank = 0
        if len(hand) > 2: # we only want to filter out the pair if the hand has more than two cards
            filtered_hand = [card for card in hand if card.get_rank_int() != pairRank] 
        else:
            filtered_hand = hand
        
        return self.highest_rank(filtered_hand)