from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())
    print()

    print("Simulating aggressive turn...")

    turn_result = engine.simulate_turn()

    hand = turn_result["hand"]
    hand_str = ", ".join(f"{card.name} ({card.cost})" for card in hand)
    print(f"Hand: [{hand_str}]\n")

    print("Turn execution:")
    print("Strategy:", strategy.get_strategy_name())
    print("Actions", {
        "cards_played": turn_result["cards_played"],
        "mana_used": turn_result["mana_used"],
        "targets_attacked": turn_result["targets_attacked"],
        "damage_dealt": turn_result["damage_dealt"]
        })
    print()

    print("Game Report:")
    print(engine.get_engine_status())
    print()

    print("Abstract Factory + Strategy Pattern:" +
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
