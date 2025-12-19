from enum import Enum


class CardRank(Enum):
    SIX = (6, "6")
    SEVEN = (7, "7")
    EIGHT = (8, "8")
    NINE = (9, "9")
    TEN = (10, "10")
    JACK = (11, "Валет")
    QUEEN = (12, "Дама")
    KING = (13, "Король")
    ACE = (14, "Туз")

    def __init__(self, value: int, notation: str):
        self.value_ = value
        self.notation = notation