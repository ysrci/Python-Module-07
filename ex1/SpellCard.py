from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        effect_data = self.resolve_effect([])

        return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": effect_data["description"]
        }

    def resolve_effect(self, targets: list) -> dict:
        return {"description": "Deal 3 damage to target"}
