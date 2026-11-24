# Working on Yahtzee2.0

Install Python 3.11 or newer with Tcl/Tk support. Install Git if you plan to clone the repository or share changes. [Download Python](https://www.python.org/downloads/)

## Get the project

If you already have the project folder or extracted it from a ZIP, open that folder in Terminal on Mac or PowerShell on Windows. Otherwise, run these commands in either shell:

```sh
git clone https://github.com/azoakhil-ix/Yahtzee2.0.git
cd Yahtzee2.0
```

Run the following commands from the folder containing `fun_game.py`. No pip packages are needed.

### Mac (Terminal)

```sh
python3 --version
python3 -m tkinter
python3 fun_game.py
```

### Windows (PowerShell)

```powershell
py -3 --version
py -3 -m tkinter
py -3 fun_game.py
```

Close the small Tkinter test window before running the final command. If Windows does not recognize `py`, try `python --version`. If it shows Python 3.11 or newer, replace `py -3` with `python` in the remaining commands. If the Tkinter check fails, see the troubleshooting steps in [README.md](README.md#if-the-window-does-not-open).

## Run automated checks

From the folder containing `fun_game.py`, run the command for your system:

- **Mac (Terminal)** · `python3 -B test/check_game.py`
- **Windows (PowerShell)** · `py -3 -B test/check_game.py`

If Windows uses `python` instead of `py`, run `python -B test/check_game.py`. The runner lists each check and prints an overall **PASS** or **FAIL**. The `-B` flag prevents Python from creating new bytecode cache files.

## Working together

`fun_game.py` launches the game. Implement game features in the appropriate `src/` module and keep function docstrings current. Coordinate shared dictionary keys and return values with your teammates before changing them.

- `src/settings.py` holds shared constants. Discuss changes to these settings with the team first.
- `src/game.py` tracks players, dice, holds, and turns in the game loop and passes those values to the UI.
- `src/scoring.py` calculates category previews and totals. Recording a category changes the scorecard.
- `src/results.py` reads and writes `results/personal_bests.csv`. A higher score adds a new row, and the results view shows only the highest total for each exact name. Keep the `results/` folder with the project.

Each teammate should independently run the finished game. See the [submission checklist](README.md#lab-submission) for the team-written plan, individual reflections, and files to include.

## Share your changes

The repository owner invites the other teammates as collaborators. Everyone works on `main`. Tell teammates which files you are editing to reduce merge conflicts.

Before making changes, run `git pull`. When ready to commit, check `git status`, stage the files you changed, then commit and push. For example:

```sh
git status
git add README.md CONTRIBUTING.md
git commit -m "Update setup instructions"
git push
```
