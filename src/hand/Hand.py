from src.card.Card import Card


class Hand:


    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def play_card(self, card: Card):
        if card in self.cards:
            self.cards.remove(card)
        return card

    def get_cards(self):
        return self.cards