from src.card.Card import Card
from src.rules.Rules import Rules


class ClassicRules(Rules):


    def can_hit(self, attacker: Card, defender: Card) -> bool:
        if attacker.is_trump and not defender.is_trump:
            return False
        if not attacker.is_trump and defender.is_trump:
            return True
        if attacker.is_trump and defender.is_trump:
            return attacker.value < defender.value
        return attacker.suit == defender.suit and attacker.value < defender.value
