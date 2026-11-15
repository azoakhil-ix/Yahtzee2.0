from src.settings import (
    ALL_CATEGORIES,
    EXTRA_YAHTZEE_BONUS_POINTS,
    FULL_HOUSE_POINTS,
    LARGE_STRAIGHT_POINTS,
    SMALL_STRAIGHT_POINTS,
    UPPER_BONUS_POINTS,
    UPPER_BONUS_THRESHOLD,
    UPPER_CATEGORIES,
    YAHTZEE_POINTS,
)


# Each scoring function receives five dice and returns points without saving them.
# The UI previews these points only for unused categories after a roll.
# Repeat-Yahtzee/Joker adjustments depend on the player’s scorecard and agreed rules.


def score_ones(dice: list[int]) -> int:
    """Preview the points for the ones category."""
    # TODO: Return the sum of dice showing 1; return 0 if none match.
    pass


def score_twos(dice: list[int]) -> int:
    """Preview the points for the twos category."""
    # TODO: Return the sum of dice showing 2; return 0 if none match.
    pass


def score_threes(dice: list[int]) -> int:
    """Preview the points for the threes category."""
    # TODO: Return the sum of dice showing 3; return 0 if none match.
    pass


def score_fours(dice: list[int]) -> int:
    """Preview the points for the fours category."""
    # TODO: Return the sum of dice showing 4; return 0 if none match.
    pass


def score_fives(dice: list[int]) -> int:
    """Preview the points for the fives category."""
    # TODO: Return the sum of dice showing 5; return 0 if none match.
    pass


def score_sixes(dice: list[int]) -> int:
    """Preview the points for the sixes category."""
    # TODO: Return the sum of dice showing 6; return 0 if none match.
    pass


def score_three_of_a_kind(dice: list[int]) -> int:
    """Preview the points for the three of a kind category."""
    # TODO: Return the sum of all dice if at least three match; otherwise return 0.
    pass


def score_four_of_a_kind(dice: list[int]) -> int:
    """Preview the points for the four of a kind category."""
    # TODO: Return the sum of all dice if at least four match; otherwise return 0.
    pass


def score_full_house(dice: list[int]) -> int:
    """Preview the points for the full house category."""
    # TODO: Return 25 for exactly three matching dice and a separate pair; otherwise 0.
    pass


def score_small_straight(dice: list[int]) -> int:
    """Preview the points for the small straight category."""
    # TODO: Return 30 for at least four consecutive distinct faces; otherwise 0.
    # Allow duplicates if four consecutive faces are still present.
    pass


def score_large_straight(dice: list[int]) -> int:
    """Preview the points for the large straight category."""
    # TODO: Return 40 for five consecutive distinct faces; otherwise return 0.
    pass


def score_yahtzee(dice: list[int]) -> int:
    """Preview the points for the yahtzee category."""
    # TODO: Return 50 if all five dice match; otherwise return 0.
    pass


def score_chance(dice: list[int]) -> int:
    """Preview the points for the chance category."""
    # TODO: Return the sum of all five dice regardless of matching faces.
    pass


def calculate_all_category_scores(dice: list[int]) -> dict[str, int]:
    """Return the preview score for every category using the current dice."""
    # TODO: Call all thirteen score_ functions with the same five dice.
    # Return a dictionary using ALL_CATEGORIES names as keys and points as values.
    # Example: {"ones": 2, "twos": 4, ...}; do not change the player’s scorecard.
    # The UI should show these previews only for categories that are still unused.
    pass


def calculate_player_total(scores: dict[str, int | None]) -> int:
    """Calculate a player’s total, including earned bonuses."""
    # TODO: Add filled category scores, treating unused entries as zero.
    # Include the 35-point upper bonus at 63 upper points and agreed Yahtzee bonuses.
    # Return the total without changing the scorecard.
    pass
