from random import Random

from src.card.CardTrumpChoicer import CardTrumpChoicer
from src.enum.Card.CardSuit import CardSuit

trump = CardTrumpChoicer(Random()).get_trump()
suits = list(CardSuit)

def test_trump_in_suits():
    assert (trump in suits) is True

def test_trump_not_in_suits():
    assert (trump not in suits) is False

def test_trump_is_null():
    assert (None in suits) is False