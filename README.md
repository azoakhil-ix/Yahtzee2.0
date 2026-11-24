# Yahtzee2.0

Yahtzee2.0 is a Python and Tkinter game for 2–4 players sharing one computer.

**ENGR 102, Section 577 · Lab 13 Team**

Akhil Azemkouo, Chiemezie Akparu, William Bryla, and Lucas Baldwin

## Run the game

Install Python 3.11 or newer with Tcl/Tk support. The official Python downloads include Tcl/Tk, and the game requires no pip packages. [Download Python](https://www.python.org/downloads/)

If you received the project as a ZIP file, extract it first. Open Terminal on Mac or PowerShell on Windows, then use `cd` to enter the folder containing `fun_game.py`.

### Mac (Terminal)

```sh
python3 fun_game.py
```

### Windows (PowerShell)

```powershell
py -3 fun_game.py
```

If PowerShell does not recognize `py`, run `python fun_game.py` after checking that `python --version` shows Python 3.11 or newer.

### If the window does not open

Run `python3 -m tkinter` on Mac or `py -3 -m tkinter` on Windows. If you used `python` to launch the game, use `python -m tkinter` here too. A small test window confirms Tkinter is available. If the check reports a missing `tkinter` or `_tkinter` module, install Python with Tcl/Tk support and reopen your terminal. [Python Tkinter documentation](https://docs.python.org/3/library/tkinter.html)

## Play

Enter two to four player names and select **Start game**. On your turn, select **Roll Dice** to throw the dice into the center. Click a die to hold it by your name, or click it again to release it. Only loose dice move on a reroll.

The scorecard previews points for the active player's unused categories. Select a category and click **Record score** to end your turn. A recorded zero uses up the category. Use **Rules** to see the game instructions and **Previous results** to see saved personal bests.

See the [plain-language Yahtzee rules](RULES.md) for the scoring table and official bonus rules.

## Saved results

The game creates `results/personal_bests.csv` after the first completed game. Keep the `results/` folder in the project so the game can save there. The CSV stores each saved scorecard and total. A new result is added when it beats the best total for that exact player name. **Previous results** displays the highest saved total per name, highest first.

## Project files

| File | Purpose |
|---|---|
| `fun_game.py` | Launches the game |
| `src/game.py` | Handles player setup, turns, and the game loop |
| `src/ui.py` | Draws the Tkinter table, dice, and scorecard |
| `src/dice.py` | Rolls dice and preserves held values |
| `src/scoring.py` | Calculates score previews and totals |
| `src/results.py` | Reads and writes the personal-best CSV |
| `src/settings.py` | Defines game and interface settings |

See [CONTRIBUTING.md](CONTRIBUTING.md) for team setup and collaboration commands.

## Lab submission

Our instructor approved Yahtzee and the use of multiple Python files. Keep `fun_game.py`, `src/`, and `results/` together when submitting the game. Each teammate should independently verify the final game.

- **Canvas Part 1** · Each teammate submits the game files and the team-written `game_plan.pdf`, including the game-choice description, hierarchy, flow explanation, test cases, and user manual.
- **Canvas Part 2** · Each teammate submits their own `reflection_yourname.pdf`.

See the [official Lab 13 instructions](https://github.com/tamu-edu-students/engr-102-lab-13-team) for the full requirements and limits on AI assistance.
