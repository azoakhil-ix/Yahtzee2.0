# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Akhil Azemkouo
# Chiemezie Akparu
# William Bryla
# Lucas Baldwin
# Section: 577
# Assignment: Lab 13 Team
# Date: November 23, 2026

from tkinter import PhotoImage, Tk, messagebox, ttk

from src.scoring import calculate_all_category_scores, calculate_player_total
from src.settings import (
    ALL_CATEGORIES, UPPER_BONUS_POINTS, UPPER_BONUS_THRESHOLD,
    UPPER_CATEGORIES, WINDOW_SIZE, WINDOW_TITLE,
)

FELT = "#174b3a"
INK = "#172d24"
PAPER = "#faf5e9"
MUTED_GREEN = "#d3e8db"
GOLD = "#f0cb78"


def create_game_window() -> Tk:
    """Create the Tkinter game window."""
    window = Tk()
    window.title(WINDOW_TITLE)
    window.geometry(WINDOW_SIZE)
    window.minsize(1060, 650)
    window.configure(background=PAPER)

    style = ttk.Style(window)
    style.theme_use("clam")
    style.configure("Game.TButton", padding=(12, 7), foreground=INK)
    style.configure("Roll.TButton", padding=(26, 12), font=("TkDefaultFont", 15, "bold"),
                    background=GOLD, foreground=INK)
    style.map("Roll.TButton", background=[("disabled", "#e3dfd4"), ("active", "#f7dc9e")])
    style.configure("Die.TButton", padding=1, background=FELT, borderwidth=0)
    style.map("Die.TButton", background=[("active", "#29634e"), ("focus", "#29634e")])
    style.configure("Score.Treeview", rowheight=25, background=PAPER, fieldbackground=PAPER,
                    foreground=INK)
    style.configure("Score.Treeview.Heading", padding=5, background="#e4dccb", foreground=INK)
    style.map("Score.Treeview", background=[("selected", "#b9dfc9")],
              foreground=[("selected", INK)])

    # Paint each die face once and keep the images alive on the window.
    pips = ((), (4,), (0, 8), (0, 4, 8), (0, 2, 6, 8),
            (0, 2, 4, 6, 8), (0, 2, 3, 5, 6, 8))
    window.die_faces = {}
    for held in (False, True):
        for value, positions in enumerate(pips):
            image = PhotoImage(master=window, width=52, height=52)
            image.put(GOLD if held else "#d6d2c6", to=(0, 0, 52, 52))
            image.put("#fff6dc" if held else PAPER, to=(2, 2, 50, 50))
            for position in positions:
                x = 13 + (position % 3) * 13
                y = 13 + (position // 3) * 13
                for offset in range(-4, 5):
                    radius = int((16 - offset * offset) ** 0.5)
                    image.put("#933c36", to=(x - radius, y + offset, x + radius + 1, y + offset + 1))
            window.die_faces[value, held] = image
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
    window.turn.configure(text=f"{player['name']}'s turn")
    for index, label in enumerate(window.player_labels):
        active = index == current_player_index and (rolls_remaining or dice)
        label.configure(background=GOLD if active else MUTED_GREEN)
    window.roll.configure(state="normal" if rolls_remaining and not all(held) else "disabled")
    if not dice:
        instruction = "Roll five dice to start your turn." if rolls_remaining else "Game complete."
    elif rolls_remaining and all(held):
        instruction = "Release a die to roll again, or choose a category."
    elif rolls_remaining:
        instruction = f"Click dice to hold them. Rolls left: {rolls_remaining}"
    else:
        instruction = "Choose a category on the scorecard."
    window.instruction.configure(text=instruction)
    for index, button in enumerate(window.dice_buttons):
        value = dice[index] if dice else 0
        position = window.dice_seats[current_player_index] if held[index] or not dice else window.dice_center
        x, y = position[index]
        button.place_configure(x=x, y=y)
        button.configure(
            image=window.die_faces[value, held[index]],
            text="Held" if held[index] else ("Keep" if value and rolls_remaining else " "),
            state="normal" if dice and rolls_remaining else "disabled",
        )
    previews = calculate_all_category_scores(dice) if dice else {}
    rows = window.scorecard.get_children()
    if rows:
        window.scorecard.delete(*rows)
    for index, category in enumerate(ALL_CATEGORIES):
        values = [category.replace("_", " ").title()]
        for entry in players:
            score = entry["scores"][category]
            values.append("-" if score is None else score)
        if player["scores"][category] is None:
            values.append(previews.get(category, "-"))
        tag = "stripe" if index % 2 else ""
        window.scorecard.insert("", "end", iid=category, values=values, tags=(tag,))
        if category == UPPER_CATEGORIES[-1]:
            subtotals = [
                sum(entry["scores"][upper] or 0 for upper in UPPER_CATEGORIES)
                for entry in players
            ]
            bonuses = [UPPER_BONUS_POINTS if total >= UPPER_BONUS_THRESHOLD else 0
                       for total in subtotals]
            window.scorecard.insert("", "end", values=["Upper subtotal", *subtotals], tags=("total",))
            window.scorecard.insert("", "end", values=["Upper bonus", *bonuses], tags=("total",))
    totals = [calculate_player_total(entry["scores"]) for entry in players]
    window.scorecard.insert("", "end", iid="total", values=["Total", *totals], tags=("total",))
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
