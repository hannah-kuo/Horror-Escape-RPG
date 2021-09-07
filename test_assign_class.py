"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 26, 2021
"""

from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import game


class TextColors:
    PURPLE = '\033[95m'
    ENDC = '\033[0m'


class TestAssignClass(TestCase):

    def test_player_class_shrieking_stumbler(self):
        character_stats = {}
        game.assign_class(character_stats, "0")
        function_works = False
        if character_stats["player_class"] == "SHRIEKING STUMBLER" and character_stats["re-rolls"] == 1 and \
                character_stats["special_attack"] == "STICK STAB" and character_stats["class_level"] == "DAY TRIPPER":
            function_works = True
        self.assertTrue(function_works)

    def test_player_class_school_jock(self):
        character_stats = {"max_player_hp": 30, "player_hp": 30}
        game.assign_class(character_stats, "1")
        function_works = False
        if character_stats["player_class"] == "SCHOOL JOCK" and character_stats["re-rolls"] == 0 and \
                character_stats["special_attack"] == "HOCKEY STICK SWING" and character_stats["max_player_hp"] == 40\
                and character_stats["class_level"] == "FRESHMAN" and character_stats["player_hp"] == 40:
            function_works = True
        self.assertTrue(function_works)

    def test_player_class_computer_nerd(self):
        character_stats = {}
        game.assign_class(character_stats, "2")
        function_works = False
        if character_stats["player_class"] == "COMPUTER NERD" and character_stats["re-rolls"] == 0 and \
                character_stats["special_attack"] == "MECHANICAL KEYBOARD CLICKING" and character_stats["class_level"] \
                == "n00b" and character_stats["light_attack_critical_hit_chance"] == 10:
            function_works = True
        self.assertTrue(function_works)

    def test_player_class_the_natural(self):
        character_stats = {}
        game.assign_class(character_stats, "3")
        function_works = False
        if character_stats["player_class"] == "THE NATURAL" and character_stats["re-rolls"] == 0 and \
                character_stats["special_attack"] == "LUCKY STRIKE" and character_stats["class_level"] == "DAYDREAMER" \
                and character_stats["heavy_attack_hit_chance"] == 6:
            function_works = True
        self.assertTrue(function_works)

    @patch('builtins.input', side_effect=[''])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_player_description(self, mock_stdout, mock_input):
        character_stats = {}
        game.assign_class(character_stats, "0")
        expected = f"\nYou are now player class {TextColors.PURPLE}SHRIEKING STUMBLER{TextColors.ENDC}\n\n"

        self.assertEqual(mock_stdout.getvalue(), expected)
