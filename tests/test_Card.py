from io import StringIO
import sys

from src.card.Card import Card
from src.enum.Card.CardSuit import CardSuit
from src.enum.Card.CardRank import CardRank
from src.rules.ClassicRules import ClassicRules
from src.schema.Card.CardCharacteristic import CardCharacteristic


card_ace_diamond = Card(
    CardCharacteristic(
        suit=CardSuit.DIAMONDS,
        rank=CardRank.ACE,
        is_trump=False
    )
)

card_trump = Card(
    CardCharacteristic(
        suit=CardSuit.CLUBS,
        rank=CardRank.SEVEN,
        is_trump=True
    )
)

card_king_diamond = Card(
    CardCharacteristic(
        suit=CardSuit.DIAMONDS,
        rank=CardRank.KING,
        is_trump=False
    )
)

card_king_spades = Card(
    CardCharacteristic(
        suit=CardSuit.SPADES,
        rank=CardRank.QUEEN,
        is_trump=False
    )
)



def test_trump_hit_default():
    assert card_trump.is_hitting(card_ace_diamond, ClassicRules()) is True

def test_default_hit_trump():
    assert card_ace_diamond.is_hitting(card_trump, ClassicRules()) is False

def test_default_greater_hit_default_lower():
    assert card_ace_diamond.is_hitting(card_king_diamond, ClassicRules()) is True

def test_default_lower_hit_default_greater():
    assert card_king_diamond.is_hitting(card_ace_diamond, ClassicRules()) is False

def test_default_suit1_hit_default_suit2():
    assert card_king_spades.is_hitting(card_ace_diamond, ClassicRules()) is False

def test_default_suit2_hit_default_suit1():
    assert card_ace_diamond.is_hitting(card_king_spades, ClassicRules()) is False

def test_show_card():
    temp = sys.stdout
    sys.stdout = StringIO()

    print(card_ace_diamond)

    assert sys.stdout.getvalue() == "Card(Масть: ♦, Достоинство: Туз, Это козырь: Нет)\n"
    sys.stdout = temp

def test_show_trump_card():
    temp = sys.stdout
    sys.stdout = StringIO()

    print(card_trump)

    assert sys.stdout.getvalue() == "Card(Масть: ♣, Достоинство: 7, Это козырь: Да)\n"
    sys.stdout = temp