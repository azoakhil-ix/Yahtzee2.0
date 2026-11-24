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

from functools import partial
from tkinter import Canvas, Entry, Frame, Label, StringVar, messagebox, ttk
from tkinter.font import Font

from src.dice import reroll_unheld_dice, roll_five_dice
from src.results import retrieve_all_player_results, save_player_results
from src.scoring import calculate_all_category_scores, calculate_player_total
from src.settings import (
    ALL_CATEGORIES, MAX_PLAYERS, MAX_ROLLS_PER_TURN, MIN_PLAYERS, NUMBER_OF_DICE, RESULTS_FOLDER,
)
from src.ui import (
    FELT, INK, MUTED_GREEN, PAPER,
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
    toolbar = Frame(window, background=PAPER, padx=20, pady=10)
    toolbar.pack(fill="x")
    Label(toolbar, text="Yahtzee2.0", background=PAPER, foreground=INK,
          font=("Georgia", 22, "bold")).pack(side="left")
    ttk.Button(toolbar, text="Quit", style="Game.TButton",
               command=partial(action.set, "quit")).pack(side="right")
    ttk.Button(toolbar, text="Previous results", style="Game.TButton",
               command=partial(action.set, "previous")).pack(side="right", padx=4)
    ttk.Button(toolbar, text="Rules", style="Game.TButton",
               command=partial(display_game_rules, window)).pack(side="right", padx=4)
    window.tabs.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    setup = Frame(window.game_tab, background=FELT, padx=32, pady=32)
    setup.pack(fill="both", expand=True)
    Label(setup, text="Set up your game", background=FELT, foreground=PAPER,
          font=("Georgia", 28, "bold")).pack(anchor="w")
    Label(setup, text="Enter names for two to four players.", background=FELT,
          foreground=MUTED_GREEN).pack(anchor="w", pady=(2, 18))
    entries = []
    for index in range(MAX_PLAYERS):
        row = Frame(setup, background=FELT)
        row.pack(anchor="w", pady=5)
        label = f"Player {index + 1}" if index < MIN_PLAYERS else f"Player {index + 1} (optional)"
        Label(row, text=label, background=FELT, foreground=PAPER,
              width=18, anchor="w").pack(side="left")
        entry = Entry(row, width=26)
        entry.pack(side="left")
        entries.append(entry)
    entries[0].focus_set()
    ttk.Button(setup, text="Start game", style="Roll.TButton",
               command=partial(action.set, "start")).pack(anchor="w", pady=20)

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
        elif choice == "previous":
            display_previous_results(window, retrieve_all_player_results(RESULTS_FOLDER))
        elif choice == "quit":
            if confirm_and_quit_game(window):
                return

    setup.destroy()
    ttk.Button(toolbar, text="Scores", style="Game.TButton",
               command=partial(action.set, "scores")).pack(side="right", padx=4)
    board = Frame(window.game_tab, background=FELT, padx=16, pady=10)
    board.pack(fill="both", expand=True)
    score_panel = Frame(board, background=PAPER, padx=10, pady=10)
    score_panel.pack(side="right", fill="y")
    Label(score_panel, text="Scorecard", background=PAPER, foreground=INK,
          font=("Georgia", 20, "bold")).pack(anchor="w", pady=(0, 7))
    window.record = ttk.Button(score_panel, text="Record score", style="Game.TButton",
                               command=partial(action.set, "record"))
    window.record.pack(side="bottom", anchor="e", pady=(8, 0))

    table = Frame(score_panel, background=PAPER)
    table.pack(fill="both", expand=True)
    columns = ["category", *[str(index) for index in range(len(players))], "preview"]
    headings = ["Category", *[player["name"] for player in players], "Preview"]
    window.scorecard = ttk.Treeview(table, columns=columns, show="headings", selectmode="browse",
                                    height=16, style="Score.Treeview")
    for column, heading in zip(columns, headings):
        anchor = "w" if column == "category" else "center"
        window.scorecard.heading(column, text=heading, anchor=anchor)
        window.scorecard.column(column, width=128 if column == "category" else 58,
                                anchor=anchor, stretch=False)
    window.scorecard.tag_configure("stripe", background="#f1eadc")
    window.scorecard.tag_configure("total", background="#e4dccb")
    scroll = ttk.Scrollbar(table, command=window.scorecard.yview)
    window.scorecard.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")
    window.scorecard.pack(side="left", fill="both", expand=True)

    tabletop = Frame(board, background=FELT, padx=8)
    tabletop.pack(side="left", fill="both", expand=True)
    tabletop.grid_columnconfigure(0, weight=1)
    tabletop.grid_rowconfigure(5, weight=1)
    window.turn = Label(tabletop, background=FELT, foreground=PAPER,
                        font=("Georgia", 25, "bold"), wraplength=350)
    window.turn.grid(row=1, column=0)
    window.instruction = Label(tabletop, background=FELT, foreground=MUTED_GREEN,
                               wraplength=350)
    window.instruction.grid(row=2, column=0, pady=(2, 10))
    dice_row = Frame(tabletop, background=FELT, width=500, height=366)
    dice_row.grid(row=3, column=0)
    columns = (126, 188, 250, 312, 374)
    rows = (22, 85, 148, 211, 274)
    window.dice_center = [(x, 146) for x in columns]
    window.dice_seats = [
        [(x, 0) for x in columns],        # Top
        [(x, 283) for x in columns],      # Bottom
        [(30, y) for y in rows],          # Left
        [(470, y) for y in rows],         # Right
    ]
    name_positions = ((250, 82), (250, 251), (78, 183), (422, 183))
    name_font = Font(root=window, font="TkDefaultFont")
    name_font.configure(size=11, weight="bold")
    side_fonts = []
    window.player_labels = []
    for index, player in enumerate(players):
        x, y = name_positions[index]
        name = player["name"]
        if index < 2:
            if name_font.measure(name) > 180:
                while name and name_font.measure(name + "…") > 180:
                    name = name[:-1]
                name += "…"
            label = Label(dice_row, text=name, padx=12, pady=6, anchor="center",
                          borderwidth=0, background=MUTED_GREEN, foreground=INK,
                          font=name_font)
            label.place(x=x, y=y, anchor="n")
        else:
            side_font = name_font.copy()
            for size in range(11, 0, -1):
                side_font.configure(size=size)
                if side_font.measure(name) <= 332:
                    break
            side_fonts.append(side_font)
            box_depth = name_font.metrics("linespace") + 12
            box_length = min(side_font.measure(name) + 24, 356)
            label = Canvas(dice_row, width=box_depth, height=box_length,
                           background=MUTED_GREEN, highlightthickness=0, borderwidth=0)
            label.create_text(box_depth / 2, box_length / 2, text=name,
                              angle=90 if index == 2 else 270, fill=INK, font=side_font)
            label.place(x=x, y=y, anchor="center")
        window.player_labels.append(label)
    window.dice_buttons = []
    for index, (x, y) in enumerate(window.dice_seats[0]):
        button = ttk.Button(dice_row, style="Die.TButton", compound="top", width=5,
                            command=partial(action.set, str(index)))
        button.place(x=x, y=y, anchor="n")
        window.dice_buttons.append(button)
    window.roll = ttk.Button(tabletop, text="Roll Dice", style="Roll.TButton",
                             command=partial(action.set, "roll"))
    window.roll.grid(row=4, column=0, pady=8)

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
        elif choice == "scores":
            display_player_scores(window, players)
        elif choice == "previous":
            display_previous_results(window, retrieve_all_player_results(RESULTS_FOLDER))
        elif choice == "roll" and rolls_remaining:
            if all(held):
                continue
            origins = window.dice_center if dice else window.dice_seats[current_player]
            dice = reroll_unheld_dice(dice, held) if dice else roll_five_dice()
            # Throw from the active player's end on the first roll.
            slide = (0, 0.13, 0.29, 0.50, 0.71, 0.87, 1, 1, 1, 1)
            bounce = (0, 9, 16, 22, 24, 17, 0, 9, 4, 0)
            for frame in range(len(slide) + 2):
                for index, button in enumerate(window.dice_buttons):
                    delay = index % 3
                    if held[index] or frame < delay:
                        continue
                    step = min(frame - delay, len(slide) - 1)
                    start_x, start_y = origins[index]
                    center_x, center_y = window.dice_center[index]
                    x = round(start_x + (center_x - start_x) * slide[step]
                              + (columns[2] - center_x) * bounce[step] / 200)
                    y = round(start_y + (center_y - start_y) * slide[step]) - bounce[step]
                    face = dice[index]
                    if step < 7:
                        face = (face + step + index) % 6 + 1
                    button.configure(image=window.die_faces[face, False])
                    button.place_configure(x=x, y=y)
                window.update_idletasks()
                window.after(29)
            rolls_remaining -= 1
        elif choice.isdigit() and dice and rolls_remaining:
            index = int(choice)
            held[index] = not held[index]
            seat = window.dice_seats[current_player][index]
            center = window.dice_center[index]
            start, end = (center, seat) if held[index] else (seat, center)
            button = window.dice_buttons[index]
            button.lift()
            for step in range(1, 7):
                x = round(start[0] + (end[0] - start[0]) * step / 6)
                y = round(start[1] + (end[1] - start[1]) * step / 6)
                button.place_configure(x=x, y=y)
                window.update_idletasks()
                window.after(18)
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