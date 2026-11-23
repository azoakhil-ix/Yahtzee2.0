from tkinter import Tk, messagebox

from src.scoring import calculate_all_category_scores, calculate_player_total
from src.settings import ALL_CATEGORIES, WINDOW_SIZE, WINDOW_TITLE


def create_game_window() -> Tk:
    """Create the Tkinter game window."""
    window = Tk()
    window.title(WINDOW_TITLE)
    window.geometry(WINDOW_SIZE)
    return window


def update_game_display(
    window: Tk,
    players: list[dict],
    dice: list[int],
    held: list[bool],
    current_player_index: int,
    rolls_remaining: int,
) -> None:
    """Show the dice, active player, recorded scores and available previews."""
    player = players[current_player_index]
    window.turn.configure(text=f"{player['name']}'s turn · {rolls_remaining} rolls left")
    window.roll.configure(state="normal" if rolls_remaining else "disabled")
    for index, button in enumerate(window.dice_buttons):
        text = str(dice[index]) if dice else "-"
        if held[index]:
            text += " (held)"
        button.configure(text=text, state="normal" if dice and rolls_remaining else "disabled")
    previews = calculate_all_category_scores(dice) if dice else {}
    rows = window.scorecard.get_children()
    if rows:
        window.scorecard.delete(*rows)
    for category in ALL_CATEGORIES:
        values = [category.replace("_", " ").title()]
        for entry in players:
            score = entry["scores"][category]
            values.append("-" if score is None else score)
        if player["scores"][category] is None:
            values.append(previews.get(category, "-"))
        window.scorecard.insert("", "end", iid=category, values=values)
    totals = [calculate_player_total(entry["scores"]) for entry in players]
    window.scorecard.insert("", "end", iid="total", values=["Total", *totals])
    window.record.configure(state="normal" if dice else "disabled")


def display_game_rules(window: Tk) -> None:
    """Explain how to take a turn and win."""
    messagebox.showinfo(
        "Rules",
        "Roll up to three times per turn. Click dice to hold or release them.\n\n"
        "Select an unused category after any roll and click Record score. "
        "A zero still uses up the category. A dash marks an unused score.\n\n"
        "Score at least 63 points in Ones through Sixes for a 35-point bonus. "
        "The highest total after everyone fills the scorecard wins.",
        parent=window,
    )


def display_player_scores(window: Tk, players: list[dict]) -> None:
    """Show the total for every player alongside the main scorecard."""
    lines = [f"{player['name']}: {calculate_player_total(player['scores'])}"
             for player in players]
    messagebox.showinfo("Current totals", "\n".join(lines), parent=window)


def display_previous_results(window: Tk, results: list[dict]) -> None:
    """Show saved personal bests."""
    lines = [f"{result['name']}: {result['total']}" for result in results]
    messagebox.showinfo("Previous results", "\n".join(lines) or "No results saved yet.", parent=window)


def confirm_and_quit_game(window: Tk) -> bool:
    """Confirm before closing the window."""
    if messagebox.askyesno("Quit game", "Close the game?", parent=window):
        window.destroy()
        return True
    return False
