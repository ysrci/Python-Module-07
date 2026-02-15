from typing import Dict
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory
from ex1.SpellCard import SpellCard
from ex0.Card import Card


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power) -> Card:
        if name_or_power == "dragon":
            return SpellCard("Fire Dragon", 5, "Legendary", "Fire")
        elif name_or_power == "goblin":
            return SpellCard("Goblin Warrior", 2, "Common", "Melee")
        else:
            return SpellCard("Unknown Creature", 1, "Common", "None")

    def create_spell(self, name_or_power) -> Card:
        if name_or_power == "fireball":
            return SpellCard("Lightning Bolt", 3, "Rare", "Lightning")
        else:
            return SpellCard("Unknown Spell", 1, "Common", "None")

    def create_artifact(self, name_or_power) -> Card:
        if name_or_power == "mana_ring":
            return ArtifactCard("Mana Ring", 1, "Rare", 3, "Gain Mana")
        else:
            return ArtifactCard("Unknown artifact", 1, "Common", 1, "None")

    def create_themed_deck(self, size: int) -> Dict:
        deck = []

        deck.append(self.create_creature("dragon"))
        deck.append(self.create_creature("goblin"))
        deck.append(self.create_spell("fireball"))

        return {
            "deck_size": len(deck),
            "cards": deck
        }

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
