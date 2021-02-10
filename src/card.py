class Card():
    # converts char ranks to numerical ranking
    ranks = {
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    def __init__(self, rank: str, suit: str):
        self.suit = suit
        self.rank = rank

    def __lt__(self, other)->bool:
        return self.get_rank_int() < other.get_rank_int()

    def get_rank_int(self, low: bool = False)->int:
        if self.rank.isnumeric(): return int(self.rank)

        if low: # returns low value of the ace else returns high value
            return self.ranks["Low"]
        return self.ranks[self.rank]