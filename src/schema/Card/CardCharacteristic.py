from dataclasses import dataclass

from src.enum.Card.CardSuit import CardSuit
from src.enum.Card.CardRank import CardRank


@dataclass(frozen=True)
class CardCharacteristic:
    suit: CardSuit
    rank: CardRank
    is_trump: bool = False

    @property
    def value(self):
        return self.rank.value_

    @property
    def notation(self):
        return self.rank.notation