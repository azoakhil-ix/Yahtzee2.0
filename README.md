<!-- Contributors: TODO: Add all contributing team members. Section: TODO. -->
# Yahtzee

A planned Python/Tkinter game for 2–4 players sharing one computer.
**Scaffold only:** functions contain docstrings, short TODOs, and `pass`.
Nothing is playable yet.

## Assignment

Follow the [official Lab 13 instructions](https://github.com/tamu-edu-students/engr-102-lab-13-team/blob/main/README.md).
Our instructor has approved **Yahtzee** and **multiple Python files**.

- `fun_game.py`: connect the functions and launch the game.
- `src/settings.py`: shared game settings, categories, and scoring constants.
- `src/state.py`: starting values for players, dice, holds, and turns.
- `src/dice.py`: roll dice and keep held dice.
- `src/scoring.py`: calculate category scores and totals.
- `src/game.py`: manage players, scorecards, turns, and winners.
- `src/ui.py`: Tkinter window, rules, scores, and quitting.
- `src/results.py`: save and read previous game results.
- `CONTRIBUTING.md`: Mac/Windows setup and collaboration commands.

## Run

With Python and Tkinter installed:

```sh
python fun_game.py
```

This currently exits without opening a window.

## Required before submission

- Implement rules/instructions, player options, scores, quitting, and file reading/writing.
- Use if/elif/else, loops, dictionaries, functions with docstrings, try/except, and comments.
- Finish and independently verify a working UI/game; identify something learned beyond class.
- Add every contributing member’s name to each submitted file’s team header.

## Documents your team must write

AI is allowed for coding, but not the planning hierarchy, descriptions, test cases,
or reflections. This scaffold is coding assistance, not your submitted design plan.

- `game_plan.pdf`: game choice (~100 words), team-drawn hierarchy (leaves about
  10 lines of code or less), flow explanation (~200 words), at least 10 team-written
  test cases, and a user manual added after completion with launch steps and input/output examples.
- `reflection_yourname.pdf`: each member answers all eight assignment questions,
  50–100 words each; use first initial and last name in the filename.

Include `fun_game.py` and the entire `src` folder together.
Every member submits the game, plan, and any required supporting files to Canvas
part 1, and their individual reflection to part 2. See the linked assignment for details.

TODO: Add team names and final project details.

## CSV scorecards

Each player gets a separate CSV file, such as `results/player_1.csv` and
`results/player_2.csv`. Each file contains that player’s scores and total.
An empty category cell means it is still available; `0` means it was used for zero
points. Python uses `None` for empty categories. Saving/loading is still a TODO.

Saved results keep each player’s personal best. For the same exact name, overwrite
only when the new total is greater than the highest saved total. Equal or lower
scores leave the files unchanged. New names get separate CSVs.

All CSVs are stored in the `results` folder, configured by `RESULTS_FOLDER` in
`src/settings.py`. No filename list is stored. `retrieve_all_player_results(folder)`
reads the folder directly and returns one best result per name, highest score first:
`[{"name": "Alex", "total": 180}]`. The UI displays those two fields.
These functions remain unimplemented TODOs.
