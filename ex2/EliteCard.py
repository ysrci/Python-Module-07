from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
import random


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, ):
        super().__init__(name, cost, rarity)
        self.health = 10
        self.attack_power = 5
        self.defense = 3
        self.mana = 0
        self.spells_cast = []

    def play(self, game_state: dict) -> dict:
        result = {
                "card": self.name,
                "played": True,
                "game_state": game_state
        }
        return result

    def attack(self, target) -> dict:
        damage = self.attack_power + random.randint(0, 3)
        result = {
                "attacker": self.name,
                "target": target,
                "damage": damage,
                "combat_type": "melee"
        }
        return result

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.defense + random.randint(0, 2), incoming_damage)
        damage_taken = incoming_damage - blocked
        self.health -= damage_taken
        result = {
                "defender": self.name,
                "damage_taken": damage_taken,
                "damage_blocked": blocked,
                "still_alive": self.health > 0
        }
        return result

    def get_combat_stats(self) -> dict:
        result = {
                "health": self.health,
                "attack_power": self.attack_power,
                "defense": self.defense
        }
        return result

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = len(targets)
        extra_mana = random.randint(0, 2)
        total_cost = mana_cost + extra_mana
        if self.mana < total_cost:
            mana_used = self.mana
            self.mana = 0
        else:
            mana_used = total_cost
            self.mana -= total_cost

        self.spells_cast.append(spell_name)
        result = {
                "caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "mana_used": mana_used
        }
        return result

    def channel_mana(self, amount: int) -> dict:
        bonus = random.randint(0, 2)
        self.mana += amount + bonus
        result = {
                "channeled": amount + bonus,
                "total_mana": self.mana
        }
        return result

    def get_magic_stats(self) -> dict:
        result = {
                "mana": self.mana,
                "spells_cast": self.spells_cast
        }
        return result
