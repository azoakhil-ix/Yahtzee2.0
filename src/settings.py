
# Game settings: uppercase names are values that should stay the same.
MIN_PLAYERS: int = 2
MAX_PLAYERS: int = 4
NUMBER_OF_DICE: int = 5
MIN_DIE_VALUE: int = 1
MAX_DIE_VALUE: int = 6
MAX_ROLLS_PER_TURN: int = 3

# Category names are shared dictionary keys, not player-entered text.
UPPER_CATEGORIES: tuple[str, ...] = (
    "ones", "twos", "threes", "fours", "fives", "sixes",
)
LOWER_CATEGORIES: tuple[str, ...] = (
    "three_of_a_kind", "four_of_a_kind", "full_house",
    "small_straight", "large_straight", "yahtzee", "chance",
)
ALL_CATEGORIES: tuple[str, ...] = (
    "ones", "twos", "threes", "fours", "fives", "sixes",
    "three_of_a_kind", "four_of_a_kind", "full_house",
    "small_straight", "large_straight", "yahtzee", "chance",
)

# Fixed scoring values; a category that does not qualify scores zero.
FULL_HOUSE_POINTS: int = 25
SMALL_STRAIGHT_POINTS: int = 30
LARGE_STRAIGHT_POINTS: int = 40
YAHTZEE_POINTS: int = 50
UPPER_BONUS_THRESHOLD: int = 63
UPPER_BONUS_POINTS: int = 35
EXTRA_YAHTZEE_BONUS_POINTS: int = 100
# TODO: Agree on repeat-Yahtzee eligibility and Joker rules before using this bonus.

# Interface and file settings.
WINDOW_TITLE: str = "Yahtzee"
WINDOW_SIZE: str = "1000x700"
# Store a separate CSV for each player, such as player_1.csv and player_2.csv.
RESULTS_FOLDER: str = "results"
