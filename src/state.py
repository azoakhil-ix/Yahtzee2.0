
# Starting values only. The team will implement changes and resets in functions.
# Use: from src import state, then read/write state.current_player_index, etc.
# Avoid importing individual variables: reassignment would not update shared state.

# Player records will contain a name and their own scores dictionary.
# Use category keys from settings.ALL_CATEGORIES; None = unused, 0 = scored zero.
players: list[dict] = []

# Zero means the first player; only use this index after players are created.
current_player_index: int = 0

# No dice have been rolled yet; after rolling, store five values from 1 through 6.
dice: list[int] = []

# True means keep that position on the next roll; False means reroll it.
held: list[bool] = [False, False, False, False, False]

# Each turn begins with three rolls available.
rolls_remaining: int = 3

# True only after all players have completed their scorecards.
game_finished: bool = False

# Best saved result per name: dictionaries containing "name" and "total".
previous_results: list[dict] = []
