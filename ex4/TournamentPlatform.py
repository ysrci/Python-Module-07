
from typing import Dict, List
from ex4.TournamentCard import TournamentCard

class TournamentPlatform:
    def __init__(self):

        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard, short_name: str = None) -> str:

        if short_name is None:
            short_name = card.name.lower().replace(" ", "_")
        card_id = f"{short_name}_{len(self.cards)+1:03d}"
        self.cards[card_id] = card
        return card_id
    def create_match(self, card1_id: str, card2_id: str) -> Dict:

        if card1_id not in self.cards or card2_id not in self.cards:
            raise ValueError("One or both card IDs not registered")

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        rating1 = card1.calculate_rating()
        rating2 = card2.calculate_rating()

        if rating1 >= rating2:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> List[Dict]:

        leaderboard = sorted(
            self.cards.items(),
            key=lambda item: item[1].calculate_rating(),
            reverse=True
        )
        return [
            {
                "card_name": card.name,
                "rating": card.calculate_rating(),
                "record": f"{card.wins}-{card.losses}"
            }
            for card_id, card in leaderboard
        ]

    def generate_tournament_report(self) -> Dict:

        total_cards = len(self.cards)
        avg_rating = int(
            sum(card.calculate_rating() for card in self.cards.values()) / total_cards
        ) if total_cards > 0 else 0

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }

