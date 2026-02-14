from typing import List
from ex0.Card import Card
import random
import math


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop(0)
        raise ValueError("Deck is empty")

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        total_cost = sum(card.cost for card in self.cards)

        creatures = sum(1 for card in self.cards if
                        card.__class__.__name__ == "CreatureCard")
        spells = sum(1 for card in self.cards if
                     card.__class__.__name__ == "SpellCard")
        artifacts = sum(1 for card in self.cards if
                        card.__class__.__name__ == "ArtifactCard")

        avg_cost = float(math.ceil(total_cost / total)) if total > 0 else 0

        return {
                "total_cards": total,
                "creatures": creatures,
                "spells": spells,
                "artifacts": artifacts,
                "avg_cost": avg_cost
        }
