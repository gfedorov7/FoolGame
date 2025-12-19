from typing import Self, TYPE_CHECKING

from src.schema.Card import CardCharacteristic

if TYPE_CHECKING:
    from src.rules.Rules import Rules


class Card:


    def __init__(
            self,
            card_characteristic: CardCharacteristic,
    ):
        self.suit = card_characteristic.suit
        self.value = card_characteristic.value
        self.notation = card_characteristic.notation
        self.is_trump = card_characteristic.is_trump

    def is_hitting(self, other: Self, rules: "Rules") -> bool:
        return rules.can_hit(other, self)

    def __str__(self) -> str:
        trump_out = "Да" if self.is_trump else "Нет"
        return f"Card(Масть: {self.suit.value}, Достоинство: {self.notation}, Это козырь: {trump_out})"