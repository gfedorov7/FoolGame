from src.card.Card import Card
from src.enum.Card.CardRank import CardRank
from src.enum.Card.CardSuit import CardSuit
from src.hand.Hand import Hand
from src.schema.Card.CardCharacteristic import CardCharacteristic

hand = Hand()

card1 = Card(
    CardCharacteristic(
        rank=CardRank.SEVEN,
        suit=CardSuit.DIAMONDS,
    )
)

card2 = Card(
    CardCharacteristic(
        rank=CardRank.EIGHT,
        suit=CardSuit.DIAMONDS,
    )
)

def test_add_card():
    assert len(hand.get_cards()) == 0
    hand.add_card(card1)
    assert len(hand.get_cards()) == 1

def test_remove_card():
    hand.add_card(card2)
    assert len(hand.get_cards()) == 2
    hand.play_card(card1)
    assert len(hand.get_cards()) == 1
    assert card1 not in hand.get_cards()
    assert card2 in hand.get_cards()
