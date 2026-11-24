# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Akhil Azemkouo
# Chiemezie Akparu
# William Bryla
# Lucas Baldwin
# Section: 577
# Assignment: Lab 13 Team
# Date: November 23, 2026

from src.settings import (
    ALL_CATEGORIES,
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
    # Add up only the dice that show a 1 (five 1s scores 5).
    return sum(die for die in dice if die == 1)


def score_twos(dice: list[int]) -> int:
    """Preview the points for the twos category."""
    # Add up only the dice that show a 2.
    return sum(die for die in dice if die == 2)


def score_threes(dice: list[int]) -> int:
    """Preview the points for the threes category."""
    # Add up only the dice that show a 3.
    return sum(die for die in dice if die == 3)


def score_fours(dice: list[int]) -> int:
    """Preview the points for the fours category."""
    # Add up only the dice that show a 4.
    return sum(die for die in dice if die == 4)


def score_fives(dice: list[int]) -> int:
    """Preview the points for the fives category."""
    # Add up only the dice that show a 5.
    return sum(die for die in dice if die == 5)


def score_sixes(dice: list[int]) -> int:
    """Preview the points for the sixes category."""
    # Add up only the dice that show a 6.
    return sum(die for die in dice if die == 6)


def score_three_of_a_kind(dice: list[int]) -> int:
    """Preview the points for the three of a kind category."""
    # If any face appears at least three times, the score is the sum of all dice.
    for face in range(1, 7):
        if dice.count(face) >= 3:
            return sum(dice)
    return 0


def score_four_of_a_kind(dice: list[int]) -> int:
    """Preview the points for the four of a kind category."""
    # If any face appears at least four times, the score is the sum of all dice.
    for face in range(1, 7):
        if dice.count(face) >= 4:
            return sum(dice)
    return 0


def score_full_house(dice: list[int]) -> int:
    """Preview the points for the full house category."""
    # Count how many times each face appears.
    counts = [dice.count(face) for face in range(1, 7)]
    # A full house needs one face appearing exactly 3 times and a different
    # face appearing exactly twice (so five of a kind does NOT count here).
    if 3 in counts and 2 in counts:
        return FULL_HOUSE_POINTS
    return 0


def score_small_straight(dice: list[int]) -> int:
    """Preview the points for the small straight category."""
    # Look at which faces are present, ignoring duplicates and order.
    faces = set(dice)
    # A small straight is any run of four consecutive faces.
    possible_runs = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
    for run in possible_runs:
        if run.issubset(faces):
            return SMALL_STRAIGHT_POINTS
    return 0


def score_large_straight(dice: list[int]) -> int:
    """Preview the points for the large straight category."""
    # A large straight is all five faces in one unbroken run.
    faces = set(dice)
    if faces == {1, 2, 3, 4, 5} or faces == {2, 3, 4, 5, 6}:
        return LARGE_STRAIGHT_POINTS
    return 0


def score_yahtzee(dice: list[int]) -> int:
    """Preview the points for the yahtzee category."""
    # All five dice match when there is only one distinct face.
    if len(dice) == 5 and len(set(dice)) == 1:
        return YAHTZEE_POINTS
    return 0


def score_chance(dice: list[int]) -> int:
    """Preview the points for the chance category."""
    # Chance always scores the sum of all five dice, whatever they show.
    return sum(dice)


def calculate_all_category_scores(dice: list[int]) -> dict[str, int]:
    """Return the preview score for every category using the current dice."""
    # Call each scoring function once and label its result with the category name.
    # This dictionary is only a preview; it never changes a player's scorecard.
    return {
        "ones": score_ones(dice),
        "twos": score_twos(dice),
        "threes": score_threes(dice),
        "fours": score_fours(dice),
        "fives": score_fives(dice),
        "sixes": score_sixes(dice),
        "three_of_a_kind": score_three_of_a_kind(dice),
        "four_of_a_kind": score_four_of_a_kind(dice),
        "full_house": score_full_house(dice),
        "small_straight": score_small_straight(dice),
        "large_straight": score_large_straight(dice),
        "yahtzee": score_yahtzee(dice),
        "chance": score_chance(dice),
    }


def calculate_player_total(scores: dict[str, int | None]) -> int:
    """Calculate a player’s total, including earned bonuses."""
    total = 0
    upper_subtotal = 0
    # Walk every category on the scorecard. None means the category is unused,
    # which counts as zero; a real number (including 0) is a recorded score.
    for category, points in scores.items():
        if points is None:
            continue
        total += points
        if category in UPPER_CATEGORIES:
            upper_subtotal += points
    # Award the 35-point upper-section bonus once the six number categories
    # (ones through sixes) reach the 63-point threshold.
    if upper_subtotal >= UPPER_BONUS_THRESHOLD:
        total += UPPER_BONUS_POINTS
    # NOTE: The repeat-Yahtzee bonus is intentionally left out. The scorecard
    # stores one value per category, so it cannot tell how many Yahtzees a
    # player rolled. Add it here only after the team settles the repeat-Yahtzee
    # rule flagged in settings.py (EXTRA_YAHTZEE_BONUS_POINTS).
    return total
