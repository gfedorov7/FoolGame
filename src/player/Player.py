from src.hand.Hand import Hand


class Player:


    def __init__(self, name: str, hand: Hand):
        self.name = name
        self.hand = hand

    def get_hand(self):
        return self.hand

    def __str__(self):
        return f"Player(Игрок: {self.name}, Количество карт: {len(self.hand.get_cards())})"