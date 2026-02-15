from typing import Dict
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        deck_data = self.factory.create_themed_deck(3)
        hand = deck_data["cards"]
        battlefield = []

        self.cards_created += len(hand)

        turn_result = self.strategy.execute_turn(hand, battlefield)

        self.turns_simulated += 1
        self.total_damage += turn_result["damage_dealt"]

        return {
            "hand": hand,
            "cards_played": turn_result["cards_played"],
            "mana_used": turn_result["mana_used"],
            "targets_attacked": turn_result["targets_attacked"],
            "damage_dealt": turn_result["damage_dealt"]
            }

    def get_engine_status(self) -> Dict:
        return {
                "turns_simulated": self.turns_simulated,
                "strategy_used": self.strategy.get_strategy_name(),
                "total_damage": self.total_damage,
                "cards_created": self.cards_created
        }
