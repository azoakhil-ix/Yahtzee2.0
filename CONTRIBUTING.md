<!-- Contributors: TODO: Add all contributing team members. Section: TODO. -->
# Working on the project

Install Python 3.11 or newer and Git. The Python installer from python.org includes
Tkinter; on Windows, include the Python launcher and Tcl/Tk options.

## Mac setup

Open Terminal:

```sh
git clone https://github.com/azoakhil-ix/Yahtzee2.0.git
cd Yahtzee2.0
python3 -m venv .venv
source .venv/bin/activate
python -m tkinter
```

## Windows setup

Open PowerShell:

```powershell
git clone https://github.com/azoakhil-ix/Yahtzee2.0.git
cd Yahtzee2.0
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m tkinter
```

If activation is blocked, use `.\.venv\Scripts\python.exe` instead of `python`.
For example: `.\.venv\Scripts\python.exe fun_game.py`.

## After setup

Close the small Tkinter test window. No pip packages are needed.
If you already cloned the project, skip cloning and open its folder instead.
If Tkinter is missing, repair/reinstall Python with Tcl/Tk support.

Each time you open a terminal, enter the project folder and activate `.venv`
using your platform’s activation command above. Then run:

```sh
python fun_game.py
```

Nothing opens until we implement the game and connect it in `fun_game.py`.

## Working together

Write your own required plan and test cases before implementation. Agree as a team
on responsibilities using your own hierarchy. AI may help with code, but cannot
write your hierarchy, planning descriptions, test cases, or reflection.

The instructor approved Yahtzee and multiple files. Implement functions in `src`,
then connect them in `fun_game.py`. Each function has a short TODO explaining
its inputs and expected behavior. Replace `pass` with code and keep its docstring accurate.
Agree on shared dictionary keys and function return values before connecting files.
Split the work between dice, scoring, game rules, and UI; assign results-file work
and final integration together. Coordinate edits so two people do not change the same file at the same time.
Each person must independently check the finished game.

Read the submission checklist in README.md. Submit `fun_game.py` and the whole
`src` folder together. No planning documents or real tests have been generated here.

## Share your changes

Everyone works on `main`. The owner must invite the other three people as
GitHub collaborators.

Before working:

```sh
git pull
```

After working:

```sh
git add .
git commit -m "message"
git push
```

Replace `message` with a short description of what you changed.
Tell teammates which file you are editing. If Git reports an error or conflict,
ask a teammate for help.

## Shared variables

**Do not edit `src/settings.py`.** If a setting needs to change, discuss it with the team first.

`src/settings.py` contains values that stay the same, such as the number of dice
and category names. `src/state.py` contains the changing game values.

Use `from src import state`, then access values like `state.rolls_remaining`.
Pass those values to the existing functions. Keep score and dice calculations
using their parameters instead of directly changing shared state.
The team still needs to implement updating/resetting state when a turn or game starts.

## Saved results

Keep every player’s CSV in the folder specified by `settings.RESULTS_FOLDER`
(currently `results`). Pass that folder to `save_player_results` and
`retrieve_all_player_results`; no filename list is stored.
Keep one CSV per player name; replace a saved result only for a strictly higher
score. New names get separate files in the same folder. Match names exactly.
Retrieval reads all CSVs in the folder and returns dictionaries containing `name`
and `total`, highest first, ready for `display_previous_results`.
`load_player_results(player_name)` takes a name, not a filename, and uses
`settings.RESULTS_FOLDER`. Name files consistently when saving and loading
(e.g. Alex → `results/Alex.csv`), including handling invalid filename characters.
Saving and retrieval are still TODOs for the team to implement.

## Scoring functions

Implement each of the thirteen `score_...` functions in `src/scoring.py` separately.
Each receives five dice and returns points without changing the scorecard.
Implement `calculate_all_category_scores(dice)` to call all thirteen and return
a dictionary of category names and points. The UI uses that dictionary to preview
unused categories after a roll; only the selected
category gets recorded. Keep previews visually separate from saved scores.

## Imports

Functions and fixed settings are imported directly where needed. Call them without
a file prefix, for example `roll_five_dice()` or `NUMBER_OF_DICE`.
Changing game values still travel through function parameters. Importing an
individual state variable and assigning it a new value does not update `state.py`.
