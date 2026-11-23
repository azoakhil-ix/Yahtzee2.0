import csv

from src.scoring import calculate_player_total
from src.settings import ALL_CATEGORIES, RESULTS_FOLDER


def save_player_results(player: dict, folder: str) -> bool:
    """Save the scorecard if it beats the player's previous best."""
    name = player["name"]
    total = calculate_player_total(player["scores"])
    previous = load_player_results(name, folder)
    if previous and total <= previous["total"]:
        return False

    try:
        with open(f"{folder}/personal_bests.csv", "a", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["total", *ALL_CATEGORIES, "name"])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow({"total": total, **player["scores"], "name": name})
        return True
    except (OSError, csv.Error) as error:
        print(f"Could not save results: {error}")
        return False


def load_player_results(player_name: str, folder: str = RESULTS_FOLDER) -> dict:
    """Read the highest saved scorecard for the given name."""
    best = {}
    try:
        with open(f"{folder}/personal_bests.csv", encoding="utf-8", newline="") as file:
            for row in csv.DictReader(file):
                if row.get("name") != player_name:
                    continue
                try:
                    total = int(row["total"])
                    scores = {}
                    for category in ALL_CATEGORIES:
                        value = row[category]
                        scores[category] = None if value == "" else int(value)
                except (KeyError, TypeError, ValueError):
                    continue
                if not best or total > best["total"]:
                    best = {"name": player_name, "scores": scores, "total": total}
    except FileNotFoundError:
        return {}
    except (OSError, csv.Error) as error:
        print(f"Could not read results: {error}")
    return best


def retrieve_all_player_results(folder: str) -> list[dict]:
    """Return each player's best total, highest first."""
    best = {}
    try:
        with open(f"{folder}/personal_bests.csv", encoding="utf-8", newline="") as file:
            for row in csv.DictReader(file):
                name = row.get("name")
                if not name:
                    continue
                try:
                    total = int(row["total"])
                    for category in ALL_CATEGORIES:
                        if row[category] != "":
                            int(row[category])
                except (KeyError, TypeError, ValueError):
                    continue
                if name not in best or total > best[name]:
                    best[name] = total
    except FileNotFoundError:
        return []
    except (OSError, csv.Error) as error:
        print(f"Could not read results: {error}")

    return [
        {"name": name, "total": total}
        for total, name in sorted(
            ((total, name) for name, total in best.items()), reverse=True
        )
    ]
