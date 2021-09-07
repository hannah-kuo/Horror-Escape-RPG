"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 28, 2021
"""

from unittest import TestCase
import game


class Test(TestCase):

    def test_shrieking_stumbler_level_up_level_two(self):
        character_stats = {"player_hp": 30, "player_level": 1, "max_player_hp": 30, "light_damage": 6,
                           "medium_damage": 10, "heavy_damage": 15, "player_class": "SHRIEKING STUMBLER",
                           "re-rolls": 1, "special_attack": "STICK STAB", "class_level": "DAY TRIPPER",
                           "player_xp": 300}
        game.level_up(character_stats)
        actual = character_stats
        expected = {"player_hp": 40, "player_level": 2, "max_player_hp": 40, "light_damage": 16, "medium_damage": 20,
                    "heavy_damage": 25, "special_attack": "LEAF MIRAGE", "class_level": "FORAGER", "player_xp": 300,
                    "re-rolls": 1, "player_class": "SHRIEKING STUMBLER"}
        self.assertEqual(actual, expected)

    def test_school_jock_level_up_level_two(self):
        character_stats = {"player_class": "SCHOOL JOCK", "re-rolls": 0, "special_attack": "HOCKEY STICK SWING",
                           "class_level": "FRESHMAN", "player_hp": 40, "player_level": 1, "max_player_hp": 40,
                           "light_damage": 6, "medium_damage": 10, "heavy_damage": 15, "player_xp": 300}
        game.level_up(character_stats)
        actual = character_stats
        expected = {"player_hp": 50, "player_level": 2, "max_player_hp": 50, "light_damage": 16, "medium_damage": 20,
                    "heavy_damage": 25, "special_attack": "SCHOOL SPIRIT BLESSING", "class_level": "VARSITY",
                    "player_xp": 300, "re-rolls": 0, "player_class": "SCHOOL JOCK"}
        self.assertEqual(actual, expected)

    def test_computer_nerd_level_up_level_two(self):
        character_stats = {"player_class": "COMPUTER NERD", "re-rolls": 0,
                           "special_attack": "MECHANICAL KEYBOARD CLICKING", "class_level": "n00b", "player_hp": 30,
                           "player_level": 1, "max_player_hp": 30, "light_damage": 6, "medium_damage": 10,
                           "heavy_damage": 15, "player_xp": 300}
        game.level_up(character_stats)
        actual = character_stats
        expected = {"player_hp": 40, "player_level": 2, "max_player_hp": 40, "light_damage": 16, "medium_damage": 20,
                    "heavy_damage": 25, "special_attack": "MULTIPLE MONITOR LIGHT SHOW", "class_level": "pwnz0r",
                    "player_xp": 300, "re-rolls": 0, "player_class": "COMPUTER NERD"}
        self.assertEqual(actual, expected)

    def test_the_natural_level_up_level_two(self):
        character_stats = {"player_class": "THE NATURAL", "re-rolls": 0, "special_attack": "LUCKY STRIKE",
                           "class_level": "DAYDREAMER", "player_hp": 30, "player_level": 1, "max_player_hp": 30,
                           "light_damage": 6, "medium_damage": 10, "heavy_damage": 15, "player_xp": 300}
        game.level_up(character_stats)
        actual = character_stats
        expected = {"player_hp": 40, "player_level": 2, "max_player_hp": 40, "light_damage": 16, "medium_damage": 20,
                    "heavy_damage": 25, "special_attack": "STRATEGIC ATTACK", "class_level": "IDEALIST",
                    "player_xp": 300, "re-rolls": 0, "player_class": "THE NATURAL"}
        self.assertEqual(actual, expected)

    def test_shrieking_stumbler_level_up_level_three(self):
        character_stats = {"player_hp": 40, "player_level": 2, "max_player_hp": 40, "light_damage": 16,
                           "medium_damage": 20, "heavy_damage": 25, "special_attack": "LEAF MIRAGE",
                           "class_level": "FORAGER", "player_xp": 800, "re-rolls": 1, "player_class":
                           "SHRIEKING STUMBLER"}
        game.level_up(character_stats)
        actual = character_stats
        expected = {"class_level": "WOOD-WANDERER", "heavy_damage": 35, "light_damage": 26, "max_player_hp": 50,
                    "medium_damage": 30, "player_class": "SHRIEKING STUMBLER", "player_hp": 50, "player_level": 3,
                    "player_xp": 800, "re-rolls": 1, "special_attack": "FOREST BARRAGE"}
        self.assertEqual(actual, expected)

    def test_school_jock_level_up_level_three(self):
        character_stats = {"player_hp": 50, "player_level": 2, "max_player_hp": 50, "light_damage": 16,
                           "medium_damage": 20, "heavy_damage": 25, "special_attack": "SCHOOL SPIRIT BLESSING",
                           "class_level": "VARSITY", "player_xp": 800, "re-rolls": 0, "player_class": "SCHOOL JOCK"}
        game.level_up(character_stats)
        actual = character_stats
        expected = {"class_level": "CHAMPION", "heavy_damage": 35, "light_damage": 26, "max_player_hp": 60,
                    "medium_damage": 30, "player_class": "SCHOOL JOCK", "player_hp": 60, "player_level": 3,
                    "player_xp": 800, "re-rolls": 0, "special_attack": "FULL SCHOLARSHIP BLAST"}
        self.assertEqual(actual, expected)

    def test_computer_nerd_level_up_level_three(self):
        character_stats = {"player_hp": 40, "player_level": 2, "max_player_hp": 40, "light_damage": 16,
                           "medium_damage": 20, "heavy_damage": 25, "special_attack": "MULTIPLE MONITOR LIGHT SHOW",
                           "class_level": "pwnz0r", "player_xp": 800, "re-rolls": 0, "player_class": "COMPUTER NERD"}
        game.level_up(character_stats)
        actual = character_stats
        expected = {"class_level": "1337 h4x0r", "heavy_damage": 35, "light_damage": 26, "max_player_hp": 50,
                    "medium_damage": 30, "player_class": "COMPUTER NERD", "player_hp": 50, "player_level": 3,
                    "player_xp": 800, "re-rolls": 0, "special_attack": "BATTLESTATION SYMPHONY"}
        self.assertEqual(actual, expected)

    def test_the_natural_level_up_level_three(self):
        character_stats = {"player_hp": 40, "player_level": 2, "max_player_hp": 40, "light_damage": 16,
                           "medium_damage": 20, "heavy_damage": 25, "special_attack": "STRATEGIC ATTACK",
                           "class_level": "IDEALIST", "player_xp": 800, "re-rolls": 0, "player_class": "THE NATURAL"}
        game.level_up(character_stats)
        actual = character_stats
        expected = {"class_level": "SURVIVALIST", "heavy_damage": 35, "light_damage": 26, "max_player_hp": 50,
                    "medium_damage": 30, "player_class": "THE NATURAL", "player_hp": 50, "player_level": 3,
                    "player_xp": 800, "re-rolls": 0, "special_attack": "BLOODY MASSACRE"}
        self.assertEqual(actual, expected)
