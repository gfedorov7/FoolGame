from src.card.Card import Card
from src.card.CardTrumpChoicer import CardTrumpChoicer
from src.enum.Card.CardSuit import CardSuit
from src.enum.Card.CardRank import CardRank
from src.schema.Card.CardCharacteristic import CardCharacteristic


class CardGenerator:


    def __init__(self, trump_choicer: CardTrumpChoicer):
        self.trump_choicer = trump_choicer
        self.trump = self.trump_choicer.get_trump()

    def get_trump(self):
        return self.trump

    def generate(self):
        return [
            self._create_card(
                self._create_characteristic(suit, rank, self._is_trump(suit))
            )
            for suit in CardSuit
            for rank in CardRank
        ]

    def _create_characteristic(self, suit: CardSuit, rank: CardRank, is_trump: bool):
        return CardCharacteristic(suit=suit, rank=rank, is_trump=is_trump)
    
    def _create_card(self, characteristic: CardCharacteristic):
        return Card(characteristic)

    def _is_trump(self, suit: CardSuit):
        return self.trump == suit
