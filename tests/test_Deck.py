from random import Random

import pytest

from src.card.Card import Card
from src.card.CardGenerator import CardGenerator
from src.card.CardTrumpChoicer import CardTrumpChoicer
from src.deck.Deck import Deck
from src.enum.Card.CardSuit import CardSuit

generator = CardGenerator(CardTrumpChoicer(Random()))
deck = Deck(generator, Random())
generated_deck = deck.get_or_create_deck()

def clear_deck():
    if deck.is_empty():
        return
    for i in range(35):
        deck.give_random_card()

def test_len_deck():
    assert len(generated_deck) == 36

def test_deck_full():
    assert deck.is_full() is True

def test_deck_empty():
    assert deck.is_empty() is False

def test_give_random_card():
    assert deck.give_random_card().__class__ is Card

def test_is_full_not_full():
    assert deck.is_full() is False

def test_is_empty_not_full():
    assert deck.is_empty() is False

def test_is_full_empty():
    clear_deck()
    assert deck.is_full() is False

def test_is_empty_empty():
    assert deck.is_empty() is True

def test_give_random_card_empty_deck():
    with pytest.raises(ValueError):
        deck.give_random_card()

def test_trump():
    assert deck.show_trump() in list(CardSuit)