from random import Random

from src.card.CardGenerator import CardGenerator
from src.card.CardTrumpChoicer import CardTrumpChoicer
from src.enum.Card.CardRank import CardRank
from src.enum.Card.CardSuit import CardSuit


trump_choices = CardTrumpChoicer(Random())
cards = CardGenerator(trump_choices).generate()

MAX_LENGTH_DECK = 36
MAX_SUIT_DECK = 4
MAX_RANK_DECK = 9

def test_length_cards():
    assert len(cards) == MAX_LENGTH_DECK

def test_count_one_suit():
    suit = CardSuit.DIAMONDS
    count_suit = len(
        list(
            filter(
                lambda card:
                    card.suit == suit, cards
            )
        )
    )
    assert count_suit == MAX_RANK_DECK

def test_count_one_rank():
    rank = CardRank.QUEEN.value
    count_rank = len(
        list(
            filter(
                lambda card:
                    card.value == rank[0]
                    and card.notation == rank[1], cards
            )
        )
    )

    assert count_rank == MAX_SUIT_DECK

def test_count_trump():
    count_trump = len(
        list(
            filter(
                lambda card: card.is_trump, cards
            )
        )
    )

    assert count_trump == MAX_RANK_DECK

def test_trumps_one_suit():
    suits = []

    for card in cards:
        suits.append(card.suit)

    assert [suit == suits[0] for suit in suits].count(True) == MAX_RANK_DECK