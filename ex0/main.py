from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")
    fire_dragon = CreatureCard(name="Fire Dragon", cost=5,
                               rarity="Legendary", attack=7, health=5)

    print("CreatureCard Info:")
    info = fire_dragon.get_card_info()
    print(info)

    mana = 6

    print(f"\nPlaying Fire Dragon with {mana} mana available:")
    print(f"Playable: {fire_dragon.is_playable(mana)}")
    print(f"Play result: {fire_dragon.play(info)}\n")

    print("Fire Dragon attacks Goblin Warrior:")
    print(f'Attack result: {fire_dragon.attack_target("Goblin Warrior")}\n')

    low_mana = 3
    print(f"Testing insufficient mana ({low_mana} available):")
    print(f"Playable: {fire_dragon.is_playable(low_mana)}\n")

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
