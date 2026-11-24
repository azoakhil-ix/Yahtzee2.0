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

"""Automated development checks for the Yahtzee game logic."""

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from src import dice, game, results, scoring
from src.settings import ALL_CATEGORIES


class ScoringChecks(unittest.TestCase):
    """Check scoring independently of the Tkinter interface."""

    def test_upper_categories(self):
        """Each number category sums only matching dice."""
        points = scoring.calculate_all_category_scores([1, 2, 2, 5, 6])
        self.assertEqual([points[key] for key in ALL_CATEGORIES[:6]], [1, 4, 0, 0, 5, 6])

    def test_combinations(self):
        """Matching groups earn points only when they meet the category."""
        cases = (
            ("three_of_a_kind", [3, 3, 3, 1, 6], 16),
            ("four_of_a_kind", [4, 4, 4, 4, 1], 17),
            ("four_of_a_kind", [3, 3, 3, 1, 6], 0),
            ("full_house", [2, 2, 5, 5, 5], 25),
            ("full_house", [5, 5, 5, 5, 5], 0),
            ("yahtzee", [6, 6, 6, 6, 6], 50),
            ("yahtzee", [6, 6, 6, 6, 5], 0),
            ("chance", [1, 1, 3, 4, 6], 15),
        )
        for category, roll, expected in cases:
            with self.subTest(category=category, roll=roll):
                self.assertEqual(scoring.calculate_all_category_scores(roll)[category], expected)

    def test_straights(self):
        """Order and duplicates affect straight scoring as expected."""
        cases = ([5, 3, 2, 4, 4], [6, 3, 2, 5, 4], [1, 2, 4, 5, 6])
        for roll, expected in zip(cases, ((30, 0), (30, 40), (0, 0))):
            with self.subTest(roll=roll):
                points = scoring.calculate_all_category_scores(roll)
                self.assertEqual((points["small_straight"], points["large_straight"]), expected)

    def test_bonus_threshold(self):
        """The upper bonus is awarded at 63 and excludes lower categories."""
        scores = dict(zip(ALL_CATEGORIES[:6], (3, 6, 9, 12, 15, 17)))
        scores["chance"] = 20
        self.assertEqual(scoring.calculate_player_total(scores), 82)
        scores["sixes"] = 18
        self.assertEqual(scoring.calculate_player_total(scores), 118)


class GameChecks(unittest.TestCase):
    """Check dice, turns, scorecards, and completed matches."""

    def test_first_roll(self):
        """The first roll draws five values between one and six."""
        with patch.object(dice, "randint", side_effect=[1, 6, 3, 4, 2]) as draw:
            self.assertEqual(dice.roll_five_dice(), [1, 6, 3, 4, 2])
        self.assertEqual([tuple(call.args) for call in draw.call_args_list], [(1, 6)] * 5)

    def test_reroll_preserves_holds(self):
        """Only loose dice take new values, and the input roll stays intact."""
        previous = [1, 2, 3, 4, 5]
        with patch.object(dice, "randint", side_effect=[6, 1]) as draw:
            self.assertEqual(dice.reroll_unheld_dice(previous, [True, False, True, False, True]),
                             [1, 6, 3, 1, 5])
        self.assertEqual(draw.call_count, 2)
        self.assertEqual(previous, [1, 2, 3, 4, 5])

    def test_setup_validation(self):
        """Setup accepts two to four players and rejects blank names."""
        for names in (["One"], ["One", " "], ["A", "B", "C", "D", "E"]):
            with self.subTest(names=names), self.assertRaises(ValueError):
                game.create_player_scorecards(names)
        self.assertEqual(len(game.create_player_scorecards(["A", "B", "C", "D"])), 4)

    def test_zero_is_recorded(self):
        """Zero fills a category once on only the current player's scorecard."""
        first, second = game.create_player_scorecards(["One", "Two"])
        game.record_category_score(first, "ones", 0)
        with self.assertRaises(ValueError):
            game.record_category_score(first, "ones", 1)
        self.assertEqual(first["scores"]["ones"], 0)
        self.assertIsNone(second["scores"]["ones"])
        self.assertFalse(game.are_all_scorecards_complete([first, second]))

    def test_full_match_and_saved_winner(self):
        """Run all 26 turns and verify the winner and reloaded totals."""
        players = game.create_player_scorecards(["One", "Two"])
        rolls = ([6, 6, 6, 6, 6], [1, 2, 3, 4, 5])
        active = 0
        for index, category in enumerate(ALL_CATEGORIES):
            for expected_active in range(2):
                self.assertEqual(active, expected_active)
                points = scoring.calculate_all_category_scores(rolls[active])
                game.record_category_score(players[active], category, points[category])
                self.assertEqual(game.are_all_scorecards_complete(players), (index, active) == (12, 1))
                active = game.get_next_player_index(active, players)
        self.assertEqual(game.find_winning_players(players), [players[0]])
        with TemporaryDirectory() as folder:
            for player in players:
                self.assertTrue(results.save_player_results(player, folder))
            self.assertEqual(results.retrieve_all_player_results(folder), [
                {"name": "One", "total": 170}, {"name": "Two", "total": 100}
            ])

    def test_ties(self):
        """Players with equal highest totals are both returned."""
        players = game.create_player_scorecards(["One", "Two", "Three"])
        for player in players[:2]:
            game.record_category_score(player, "chance", 15)
        self.assertEqual(game.find_winning_players(players), players[:2])


class ResultsChecks(unittest.TestCase):
    """Check CSV behavior in temporary folders."""

    def test_personal_bests(self):
        """Lower and tied scores are ignored and higher scores are reloaded."""
        name = 'Alex, "Ace"'
        first, second = game.create_player_scorecards([name, "Sam"])
        game.record_category_score(first, "ones", 0)
        game.record_category_score(first, "chance", 10)
        game.record_category_score(second, "chance", 15)
        with TemporaryDirectory() as folder:
            self.assertTrue(results.save_player_results(first, folder))
            self.assertFalse(results.save_player_results(first, folder))
            self.assertFalse(results.save_player_results({"name": name, "scores": {"chance": 9}}, folder))
            self.assertTrue(results.save_player_results(second, folder))
            game.record_category_score(first, "twos", 6)
            self.assertTrue(results.save_player_results(first, folder))
            saved = results.load_player_results(name, folder)
            self.assertEqual(saved["scores"], first["scores"])
            self.assertEqual(results.retrieve_all_player_results(folder),
                             [{"name": name, "total": 16}, {"name": "Sam", "total": 15}])

    def test_missing_and_malformed_results(self):
        """Missing files and invalid score rows produce no results."""
        with TemporaryDirectory() as folder:
            self.assertEqual(results.load_player_results("One", folder), {})
            self.assertEqual(results.retrieve_all_player_results(folder), [])
            path = Path(folder) / "personal_bests.csv"
            path.write_text("total,name\ninvalid,One\n", encoding="utf-8")
            self.assertEqual(results.load_player_results("One", folder), {})
            self.assertEqual(results.retrieve_all_player_results(folder), [])
