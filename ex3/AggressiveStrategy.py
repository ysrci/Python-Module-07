from typing import List, Dict
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        max_mana = 5

        for card in battlefield:
            damage_dealt += card.cost

        sorted_hand = sorted(hand, key=lambda c: c.cost)

        for card in sorted_hand:
            if mana_used + card.cost <= max_mana:
                cards_played.append(card.name)
                mana_used += card.cost
                damage_dealt += card.cost

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt,
            "hand": hand
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if "Enemy Player" in available_targets:
            prioritized = ["Enemy Player"]
            for target in available_targets:
                if target != "Enemy Player":
                    prioritized.append(target)
            return prioritized
        return available_targets

