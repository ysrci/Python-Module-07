from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    deck = Deck()

    creature = CreatureCard(
            name="Fire Dragon",
            cost=5,
            rarity="Legendary",
            attack=7,
            health=5
    )

    spell = SpellCard(
            name="Lightning Bolt",
            cost=3,
            rarity="Rare",
            effect_type="damage"
    )

    artifact = ArtifactCard(
            name="Mana Crystal",
            cost=2,
            rarity="Common",
            durability=3,
            effect="Permanent: +1 mana per turn"
    )

    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)

    print("Deck stats:", deck.get_deck_stats(), "\n")
    print("Drawing and playing cards:\n")

    while True:
        try:
            card = deck.draw_card()
            print(f"Drew: {card.name}",
                  f"({card.__class__.__name__.replace('Card','')})")
            print("Play result:", card.play({}), "\n")
        except ValueError:
            break

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
