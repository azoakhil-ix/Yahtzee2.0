def save_player_results(player: dict, folder: str) -> bool:
    """Save a player’s personal best in the results folder."""
    # TODO: Check CSVs in the folder for the same player name and highest saved total.
    # Overwrite that player’s best file only if the new total is greater; keep ties.
    # For a new name, write a separate CSV in this folder; create the folder if needed.
    # Save the scorecard and total; return True if saved, False if unchanged or saving fails.
    pass


def load_player_results(filename: str) -> dict:
    """Read one player’s scores from their CSV file."""
    # TODO: Read the player’s name, category scores, bonuses, and total from their CSV.
    # Convert empty categories to None and used scores to integers, including zero.
    # Return the player’s data, or an empty dictionary if the file cannot be read.
    pass


def retrieve_all_player_results(folder: str) -> list[dict]:
    """Read all saved player results directly from the results folder."""
    # TODO: Read every CSV in the folder; skip invalid files with a clear message.
    # For repeated names, keep the highest total; compare names exactly as written.
    # Return dictionaries like {"name": "Alex", "total": 180}, highest total first.
    # Return an empty list for a missing/empty folder; do not change saved files.
    pass
