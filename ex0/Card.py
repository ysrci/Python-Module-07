from abc import ABC, abstractmethod


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Abstract Method To Play The Card"""
        pass

    def get_card_info(self) -> dict:
        """Return Basic Card Info"""
        return {
                "name": self.name,
                "cost": self.cost,
                "rarity": self.rarity
                }

    def is_playable(self, available_mana: int) -> bool:
        """Check If The Card Can Be Played With Mvailable Mana"""
        return available_mana >= self.cost
