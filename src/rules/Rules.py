from abc import ABC, abstractmethod

from src.card.Card import Card


class Rules(ABC):

    @abstractmethod
    def can_hit(self, attacker: Card, defender: Card) -> bool: ...