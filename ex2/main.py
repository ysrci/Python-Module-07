from ex2.EliteCard import EliteCard


def main():
    print("\n=== DataDeck Ability System ===\n")

    arcane_warrion = EliteCard(name="Arcane Warrior", cost=5, rarity="Elite")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying {arcane_warrion.name} (Elite Card):\n")

    print("Combat phase:")
    attack_result = arcane_warrion.attack("Enemy")
    print("attack result:", attack_result)

    defense_result = arcane_warrion.defend(4)
    print("Defense result:", defense_result)

    print("\nMagic phase:")
    spell_result = arcane_warrion.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print("Spell cast:", spell_result)

    mana_result = arcane_warrion.channel_mana(3)
    print("Mana channel:", mana_result)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
