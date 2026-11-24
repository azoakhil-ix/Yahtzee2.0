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

from random import randint

from src.settings import MAX_DIE_VALUE, MIN_DIE_VALUE, NUMBER_OF_DICE


# Called once at the start of a turn to throw all five dice fresh.
def roll_five_dice() -> list[int]:
    """Return the values of five newly rolled dice."""
    # Build a list of five random faces, each from 1 through 6.
    new_dice = []
    for _ in range(NUMBER_OF_DICE):
        new_dice.append(randint(MIN_DIE_VALUE, MAX_DIE_VALUE))
    return new_dice


# Called on the second and third rolls of a turn to reroll only the loose dice.
def reroll_unheld_dice(dice: list[int], held: list[bool]) -> list[int]:
    """Return new dice values while preserving held positions."""
    # Walk through each of the five positions in order.
    new_dice = []
    for position in range(NUMBER_OF_DICE):
        if held[position]:
            # The player is keeping this die, so copy its current value.
            new_dice.append(dice[position])
        else:
            # This die is loose, so roll a new random face for it.
            new_dice.append(randint(MIN_DIE_VALUE, MAX_DIE_VALUE))
    return new_dice
