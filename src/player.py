from card import Card
from card_ranker import CardRanker
from card_ranks import CardRanks
from typing import List

class Player():

    def __init__(self, player_id: int, hand: List[str]):
        self.hand = [Card(c[0], c[1]) for c in hand]
        self.id = player_id
        self.hand_ranking = CardRanks.NO_RANK.value
        self.highest_card = None
        self.high_card_pair = None
        self.card_ranker = CardRanker()
    
    def __str__(self):
        return f'id: {self.id}, hand_rank: {self.hand_ranking}, highest: {self.highest_card}'

    def __repr__(self):
        return f'id: {self.id}, hand_rank: {self.hand_ranking}, highest: {self.highest_card}'
    
    def rank_hand(self):
        # sets hand_ranking to enum value based on hand type
        isStraight = True 
        isFlush = True
        #get highest card
        self.highest_card = self.card_ranker.highest_rank(self.hand)

        #check first if there is a straight and flush
        isStraight = self.card_ranker.check_straight(self.hand)
        isFlush = self.card_ranker.check_flush(self.hand)

        if isStraight and isFlush: 
            self.hand_ranking = CardRanks.STRAIGHT_FLUSH.value
            return

        #if not both then check if three of a kind    
        if self.card_ranker.check_three_of_a_kind(self.hand):
            self.hand_ranking = self.hand_ranking = CardRanks.THREE_OF_A_KIND.value
            return
        #if not three of a kind / straight / flush then check pair
        if isStraight:
            self.hand_ranking = CardRanks.STRAIGHT.value
        elif isFlush:
            self.hand_ranking = CardRanks.FLUSH.value
        else:
            isPair, pairRank = self.card_ranker.check_pair(self.hand)
            if isPair:
                self.hand_ranking = CardRanks.PAIR.value
                self.high_card_pair = pairRank # setting pair card in case of tie
                self.highest_card =  self.card_ranker.highest_remaining(self.hand, pairRank)# this has to set to the remaining card in case of tie
            else: #if its none of the above then there is no rank
                self.hand_ranking = CardRanks.NO_RANK.value
