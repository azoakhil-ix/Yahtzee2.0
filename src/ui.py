from tkinter import Tk, messagebox, ttk

from src.scoring import calculate_all_category_scores, calculate_player_total
from src.settings import ALL_CATEGORIES, WINDOW_SIZE, WINDOW_TITLE


def create_game_window() -> Tk:
    """Build the Tkinter window and its game controls."""
    # TODO: Create five clickable dice, player scorecards, totals, and a current-player label.
    # Add Roll, Rules, Scores, Previous Results, and Quit controls.
    pass


def update_game_display(
    window: Tk,
    players: list[dict],
    dice: list[int],
    held: list[bool],
    current_player_index: int,
    rolls_remaining: int,
) -> None:
    """Refresh the window to match the current game state."""
    # TODO: Show current dice, held positions, scorecards, player turn, and rolls remaining.
    # After a roll, use calculate_all_category_scores to preview unused category points.
    # Save points only when selected; keep filled categories unchanged and unavailable.
    # Distinguish previews, unused scores, and recorded zero scores.
    pass


def display_game_rules(window: Tk) -> None:
    """Show the game rules and explain the controls."""
    # TODO: Open a readable rules panel explaining turns, holds, categories, and bonuses.
    # Explain how to roll, choose a category, view scores, and quit.
    pass


def display_player_scores(window: Tk, players: list[dict]) -> None:
    """Show each player’s scorecard and current total."""
    # TODO: Display entered category scores and totals for all players.
    # Label unused categories clearly so they are not confused with zero scores.
    pass


def display_previous_results(window: Tk, results: list[dict]) -> None:
    """Display the saved best score for each player name."""
    # TODO: Display each result’s "name" and "total" returned by retrieve_all_player_results.
    # Show a helpful message when there are no previous results.
    pass


def confirm_and_quit_game(window: Tk) -> None:
    """Let the player confirm before closing the game."""
    # TODO: Ask whether the player wants to quit the current game early.
    # Close the window only after confirmation; otherwise continue playing.
    pass
