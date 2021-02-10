from enum import Enum

class CardRanks(Enum): 
    STRAIGHT_FLUSH = 5
    THREE_OF_A_KIND = 4
    STRAIGHT = 3
    FLUSH = 2
    PAIR = 1
    NO_RANK = 0