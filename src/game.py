from functools import partial
from tkinter import Button, Entry, Frame, Label, StringVar, messagebox, ttk

from src.dice import reroll_unheld_dice, roll_five_dice
from src.results import retrieve_all_player_results, save_player_results
from src.scoring import calculate_all_category_scores, calculate_player_total
from src.settings import (
    ALL_CATEGORIES, MAX_PLAYERS, MAX_ROLLS_PER_TURN, MIN_PLAYERS, NUMBER_OF_DICE, RESULTS_FOLDER,
)
from src.ui import (
    confirm_and_quit_game,
    create_game_window,
    display_game_rules,
    display_player_scores,
    display_previous_results,
    update_game_display,
)


def create_player_scorecards(names: list[str]) -> list[dict]:
    """Make an empty scorecard for each player."""
    if not MIN_PLAYERS <= len(names) <= MAX_PLAYERS or any(not name.strip() for name in names):
        raise ValueError("Enter two to four player names.")
    return [{"name": name, "scores": dict.fromkeys(ALL_CATEGORIES)} for name in names]


def record_category_score(player: dict, category: str, score: int) -> None:
    """Record points in an unused category."""
    scores = player["scores"]
    if category not in scores or scores[category] is not None:
        raise ValueError("Choose an unused category.")
    scores[category] = score


def get_next_player_index(current_player_index: int, players: list[dict]) -> int:
    """Move to the next player, wrapping back to the first."""
    return (current_player_index + 1) % len(players)


def are_all_scorecards_complete(players: list[dict]) -> bool:
    """Check whether every player has filled every category."""
    return bool(players) and all(
        player["scores"][category] is not None
        for player in players
        for category in ALL_CATEGORIES
    )


def find_winning_players(players: list[dict]) -> list[dict]:
    """Return every player with the highest total."""
    totals = [calculate_player_total(player["scores"]) for player in players]
    highest = max(totals, default=0)
    return [player for player, total in zip(players, totals) if total == highest]


def start_game() -> None:
    """Set up the controls and respond to player actions."""
    window = create_game_window()
    action = StringVar(window)
    # Each button writes its action. wait_variable lets Tk handle events while waiting.
    window.protocol("WM_DELETE_WINDOW", partial(action.set, "quit"))
    toolbar = Frame(window, pady=8)
    toolbar.pack(side="bottom", fill="x")
    for text, choice in (("Rules", "rules"), ("Previous results", "previous"), ("Quit", "quit")):
        Button(toolbar, text=text, command=partial(action.set, choice)).pack(side="left", padx=4)

    setup = Frame(window, padx=20, pady=20)
    setup.pack(anchor="w")
    Label(setup, text="Enter names for two to four players").pack(anchor="w")
    entries = []
    for index in range(MAX_PLAYERS):
        row = Frame(setup)
        row.pack(anchor="w")
        Label(row, text=f"Player {index + 1}").pack(side="left")
        entry = Entry(row)
        entry.pack(side="left", padx=8, pady=4)
        entries.append(entry)
    entries[0].focus_set()
    Button(setup, text="Start game", command=partial(action.set, "start")).pack(anchor="w")

    players = []
    while not players:
        window.wait_variable(action)
        choice = action.get()
        if choice == "start":
            try:
                names = [entry.get().strip() for entry in entries if entry.get().strip()]
                players = create_player_scorecards(names)
            except ValueError as error:
                messagebox.showerror("Player names", str(error), parent=window)
        elif choice == "rules":
            display_game_rules(window)
        elif choice == "previous":
            display_previous_results(window, retrieve_all_player_results(RESULTS_FOLDER))
        elif choice == "quit":
            if confirm_and_quit_game(window):
                return

    setup.destroy()
    Button(toolbar, text="Scores", command=partial(action.set, "scores")).pack(side="left")
    window.turn = Label(window, pady=8, font=("TkDefaultFont", 16))
    window.turn.pack()

    dice_row = Frame(window)
    dice_row.pack(pady=6)
    window.dice_buttons = []
    for index in range(NUMBER_OF_DICE):
        button = Button(dice_row, width=9, command=partial(action.set, str(index)))
        button.pack(side="left")
        window.dice_buttons.append(button)
    window.roll = Button(dice_row, text="Roll dice", command=partial(action.set, "roll"))
    window.roll.pack(side="left", padx=8)

    window.record = Button(window, text="Record score", command=partial(action.set, "record"))
    window.record.pack(side="bottom", pady=8)
    columns = ["category", *[str(index) for index in range(len(players))], "preview"]
    headings = ["Category", *[player["name"] for player in players], "If selected"]
    window.scorecard = ttk.Treeview(window, columns=columns, show="headings", selectmode="browse")
    for column, heading in zip(columns, headings):
        window.scorecard.heading(column, text=heading)
        window.scorecard.column(column, width=140, anchor="center")
    scroll = ttk.Scrollbar(window, command=window.scorecard.yview)
    window.scorecard.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")
    window.scorecard.pack(fill="both", expand=True, padx=12)

    current_player = 0
    dice = []
    held = [False] * NUMBER_OF_DICE
    rolls_remaining = MAX_ROLLS_PER_TURN
    finished = False
    while True:
        if not finished:
            update_game_display(window, players, dice, held, current_player, rolls_remaining)
        window.wait_variable(action)
        choice = action.get()
        if choice == "quit":
            if confirm_and_quit_game(window):
                return
        elif choice == "rules":
            display_game_rules(window)
        elif choice == "scores":
            display_player_scores(window, players)
        elif choice == "previous":
            display_previous_results(window, retrieve_all_player_results(RESULTS_FOLDER))
        elif choice == "roll" and rolls_remaining:
            dice = reroll_unheld_dice(dice, held) if dice else roll_five_dice()
            rolls_remaining -= 1
        elif choice.isdigit() and dice and rolls_remaining:
            index = int(choice)
            held[index] = not held[index]
        elif choice == "record" and dice:
            selection = window.scorecard.selection()
            previews = calculate_all_category_scores(dice)
            if not selection or selection[0] not in previews:
                messagebox.showinfo("Record score", "Select a category first.", parent=window)
                continue
            category = selection[0]
            try:
                record_category_score(players[current_player], category, previews[category])
            except ValueError as error:
                messagebox.showinfo("Record score", str(error), parent=window)
                continue
            dice = []
            held = [False] * NUMBER_OF_DICE
            if are_all_scorecards_complete(players):
                finished = True
                rolls_remaining = 0
                update_game_display(window, players, dice, held, current_player, rolls_remaining)
                winners = find_winning_players(players)
                names = ", ".join(player["name"] for player in winners)
                total = calculate_player_total(winners[0]["scores"])
                result = "Tie" if len(winners) > 1 else "Winner"
                window.turn.configure(text=f"{result}: {names} ({total} points)")
                for player in players:
                    save_player_results(player, RESULTS_FOLDER)
            else:
                current_player = get_next_player_index(current_player, players)
                rolls_remaining = MAX_ROLLS_PER_TURN
