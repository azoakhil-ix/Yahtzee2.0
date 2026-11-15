
def calculate_category_score(dice: list[int], category: str) -> int:
    """Calculate the points earned in one scoring category."""
    # TODO: Use the five dice and selected category to calculate its Yahtzee score.
    # Return zero if the dice do not satisfy the category; do not save the score.
    # Split category calculations into small helpers as your team implements them.
    pass


def calculate_player_total(scores: dict[str, int | None]) -> int:
    """Calculate a player’s total, including earned bonuses."""
    # TODO: Add filled category scores, treating unused entries as zero.
    # Include the 35-point upper bonus at 63 upper points and agreed Yahtzee bonuses.
    # Return the total without changing the scorecard.
    pass
