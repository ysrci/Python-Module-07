from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and Health must be positive integers")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """Play The Creature Card"""
        return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        """Attack Another Creature Or Target"""
        return {
                "attacker": self.name,
                "target": target,
                "damage_dealt": self.attack,
                "combat_resolved": True
        }

    def get_card_info(self) -> dict:
        """Method Extension"""
        info = super().get_card_info()
        info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return info
