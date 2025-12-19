from random import Random
from typing import List

from src.card.Card import Card
from src.card.CardGenerator import CardGenerator


class Deck:
    MAX_LENGTH_DECK = 36

    def __init__(
            self,
            generator: CardGenerator,
            random: Random
    ):
        self.generator = generator
        self.random = random
        self.deck = []

    def get_or_create_deck(self) -> List[Card]:
        if not self.deck:
            self._create_mixed_deck()
        return self.deck

    def _create_mixed_deck(self) -> None:
        self._create_deck()
        self._mix_deck()

    def _create_deck(self):
        self.deck = self.generator.generate()

    def _mix_deck(self) -> None:
        self.random.shuffle(self.deck)

    def give_random_card(self) -> Card:
        if self.is_empty():
            raise ValueError('Колода пуста')

        index = self.random.randrange(len(self.deck))
        return self.deck.pop(index)

    def is_empty(self):
        return len(self.deck) == 0

    def is_full(self):
        return len(self.deck) == 36

    def show_trump(self):
        return self.generator.get_trump()
