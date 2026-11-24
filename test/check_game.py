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

"""Run the team's test_*.py files with python3 test/check_game.py."""

import sys
import unittest
from pathlib import Path


if __name__ == "__main__":
    test_folder = Path(__file__).resolve().parent
    sys.path.insert(0, str(test_folder.parent))
    checks = unittest.defaultTestLoader.discover(str(test_folder))

    if checks.countTestCases() == 0:
        print("No checks found. Add your team's test_*.py files to the test folder.")
        sys.exit(1)

    result = unittest.TextTestRunner(stream=sys.stdout, verbosity=2).run(checks)
    if result.wasSuccessful():
        print("PASS - all checks completed without failures.")
    else:
        print("FAIL - see the failed checks above.")
    sys.exit(0 if result.wasSuccessful() else 1)
