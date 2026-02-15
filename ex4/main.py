from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard

def main():
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...")

    platform = TournamentPlatform()

    card1 = TournamentCard("Fire Dragon", cost=5, attack_power=8, initial_rating=1200)
    card2 = TournamentCard("Ice Wizard", cost=4, attack_power=7, initial_rating=1150)


    id1 = platform.register_card(card1, short_name="dragon")
    id2 = platform.register_card(card2, short_name="wizard")


    for card_id, card in [(id1, card1), (id2, card2)]:
        interfaces = ["Card", "Combatable", "Rankable"]
        print(f"{card.name} (ID: {card_id}):")
        print(f"- Interfaces: {interfaces}")
        print(f"- Rating: {card.calculate_rating()}")
        print(f"- Record: {card.wins}-{card.losses}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(id1, id2)
    print("Match result:", match_result)

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, entry in enumerate(leaderboard, start=1):
        print(f"{i}. {entry['card_name']} - Rating: {entry['rating']} ({entry['record']})")

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")

if __name__ == "__main__":
    main()
