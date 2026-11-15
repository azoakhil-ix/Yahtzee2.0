from random import randint

from src.settings import MAX_DIE_VALUE, MIN_DIE_VALUE, NUMBER_OF_DICE


#this function is only called once per games per user.
def roll_five_dice() -> list[int]:
    """Return the values of five newly rolled dice."""
    # TODO: Generate five random integers from 1 through 6.
    # Return them as a list in the same order they will appear on screen.
    pass

#after above function is called for the firstime only this one will be called.
def reroll_unheld_dice(dice: list[int], held: list[bool]) -> list[int]:
    """Return new dice values while preserving held positions."""
    # TODO: Accept five dice and five True/False values marking which dice are held.
    # Reroll only positions marked False and return a new list of five values.
    pass
