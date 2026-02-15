from typing import Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, attack_power: int, initial_rating: int = 1200, rarity: str = "Common"):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.wins = 0
        self.losses = 0
        self.rating = initial_rating

    def attack(self, target) -> Dict:
        damage = self.attack_power
        return {"attacker": self.name, "target": target.name, "damage": damage}

    def play(self, game_state: dict) -> Dict:
        return {"card_played": self.name, "mana_used": self.cost}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += wins * 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= losses * 16

    def get_rank_info(self) -> Dict:
        return {"rating": self.rating,
                "wins": self.wins,
                "losses": self.losses
                }

    def get_tournament_stats(self) -> Dict:
        return {
                "name": self.name,
                "rarity": self.rating,
                "record": f"{self.wins}-{self.losses}",
                "attack_power": self.attack_power
                }

    def defend(self, attacker) -> Dict:
        damage_taken = max(attacker.attack_power - self.attack_power // 2, 0)
        return {"defender": self.name, "attacker": attacker.name, "damage_taken": damage_taken}

    def get_combat_stats(self) -> Dict:
        return {
            "name": self.name,
            "attack_power": self.attack_power,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.rating
        }
