from src.scoring import calculate_player_total
from src.settings import ALL_CATEGORIES, MAX_PLAYERS, MIN_PLAYERS


# names will come from state.py's var players.
# Example after adding two players (the other 11 categories are omitted here):
# [
#     {
#         "name": "Alex",
#         "scores": {
#             "ones": None,
#             "twos": None,
#             # ...the other 11 categories
#         },
#     },
#     {
#         "name": "Sam",
#         "scores": {
#             "ones": None,
#             "twos": None,
#             # ...the other 11 categories
#         },
#     },
# ]
def create_player_scorecards(names: list[str]) -> list[dict]:
    """Create a player record and empty scorecard for each name."""
    # TODO: Accept 2–4(inclusive) nonblank names and return player records using dictionaries.
    # Give each player all thirteen categories; use None for an unused score.
    pass


def record_category_score(player: dict, category: str, score: int) -> None:
    """Store points in one unused category of a player’s scorecard."""
    # TODO: Raise ValueError if the category does not exist or is already filled.
    # A score of 0 counts as filled; only None means unused.
    # Leave the original score unchanged when raising the exception.
    # Otherwise, save the supplied score, including zero.
    pass


def get_next_player_index(current_player_index: int, players: list[dict]) -> int:
    """Return the index of the player whose turn comes next."""
    # TODO: Move to the next player in the list, returning to index zero after the last.
    # The caller must reset held dice and rolls remaining for the new turn.
    pass


def are_all_scorecards_complete(players: list[dict]) -> bool:
    """Check whether every player has completed their scorecard."""
    # TODO: Check all thirteen categories for every player.
    # Return True only when none are unused; zero is a completed score.
    pass


def find_winning_players(players: list[dict]) -> list[dict]:
    """Return all players tied for the highest final total."""
    # TODO: Calculate each player’s final total after the game is complete.
    # Return a list of every player sharing the highest score, including ties.
    pass


# Each player is a dictionary containing their name and scorecard, not just a name.
# The names input is a list of strings, such as ["Alex", "Sam"]. Only one having strings of anmes of each player and not dictionary
# state.players is a list of player dictionaries, not a list of name strings.
