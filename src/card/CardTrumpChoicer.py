from random import Random

from src.enum.Card.CardSuit import CardSuit


class CardTrumpChoicer:

    def __init__(
            self,
            random: Random
    ):
        self.random = random

    def get_trump(self) -> CardSuit:
        return self._get_random_suit()

    def _get_random_suit(self) -> CardSuit:
        suits = list(CardSuit)
        return self.random.choice(suits)
