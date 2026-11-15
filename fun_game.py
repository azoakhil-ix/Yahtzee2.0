from src.dice import reroll_unheld_dice, roll_five_dice
from src.game import (
    are_all_scorecards_complete,
    create_player_scorecards,
    find_winning_players,
    get_next_player_index,
    record_category_score,
)
from src.results import retrieve_all_player_results, save_player_results
from src.settings import MAX_ROLLS_PER_TURN, RESULTS_FOLDER
from src.ui import (
    confirm_and_quit_game,
    create_game_window,
    display_game_rules,
    display_player_scores,
    display_previous_results,
    update_game_display,
)


def start_game() -> None:
    """Connect the game functions and start the application."""
    # TODO: Collect 2–4 player names, create their scorecards, and open the window.
    # Connect the buttons to rolls, holds, scoring, rules, results, and quitting.
    # Track the active player and rolls remaining; allow at most three rolls per turn.
    pass


if __name__ == "__main__":
    start_game()
