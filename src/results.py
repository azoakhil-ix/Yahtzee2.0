from src.settings import RESULTS_FOLDER


# this function writes into a file.
# use read and write mode to read if current score is higher than the max(stored) score and write it into the file.
def save_player_results(player: dict, folder: str) -> bool:
    """Save a player’s personal best in the results folder."""
    # TODO: Check CSVs in the folder for the same player name and highest saved total.
    # Overwrite that player’s best file only if the new total is greater; keep ties.
    # Use the player name for the CSV filename, matching load_player_results; create the folder if needed.
    # Save the scorecard and total; return True if saved, False if unchanged or saving fails.
    pass


def load_player_results(player_name: str) -> dict:
    """Find and read a player’s CSV using their name."""
    # TODO: Build the CSV path from RESULTS_FOLDER and the player name, e.g. Alex.csv.
    # Use the same filename rule as saving; handle names with invalid filename characters consistently.
    # Read the scorecard; convert empty categories to None and numeric scores to integers.
    # Return the player’s data, or an empty dictionary if the file cannot be read.
    pass


def retrieve_all_player_results(folder: str) -> list[dict]:
    """Read all saved player results directly from the results folder."""
    # TODO: Read every CSV in the folder; skip invalid files with a clear message.
    # For repeated names, keep the highest total; compare names exactly as written.
    # Return dictionaries like {"name": "Alex", "total": 180}, highest total first.
    # Return an empty list for a missing/empty folder; do not change saved files.
    pass
