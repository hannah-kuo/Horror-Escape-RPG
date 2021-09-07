"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 28, 2021
"""

from unittest import TestCase
import unittest.mock
import io
import game


class TextColors:
    BLACK = '\033[30m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[37m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    NEGATIVE = '\033[3m'


class Test(TestCase):

    def test_shrieking_stumbler_level_up_level_three(self):
        character_stats = {"player_hp": 40, "player_level": 2, "max_player_hp": 40, "light_damage": 16,
                           "medium_damage": 20, "heavy_damage": 25, "special_attack": "LEAF MIRAGE",
                           "class_level": "FORAGER", "player_xp": 800, "re-rolls": 1, "player_class":
                           "SHRIEKING STUMBLER"}
        actual = game.class_level_3(character_stats)
        expected = {"player_hp": 40, "player_level": 2, "max_player_hp": 40, "light_damage": 16, "medium_damage": 20,
                    "heavy_damage": 25, "special_attack": "FOREST BARRAGE", "class_level": "WOOD-WANDERER",
                    "player_xp": 800, "re-rolls": 1, "player_class": "SHRIEKING STUMBLER"}
        self.assertEqual(actual, expected)

    def test_school_jock_level_up_level_three(self):
        character_stats = {"player_hp": 50, "player_level": 2, "max_player_hp": 50, "light_damage": 16,
                           "medium_damage": 20, "heavy_damage": 25, "special_attack": "SCHOOL SPIRIT BLESSING",
                           "class_level": "VARSITY", "player_xp": 800, "re-rolls": 0, "player_class": "SCHOOL JOCK"}
        game.class_level_3(character_stats)
        actual = character_stats
        expected = {"player_hp": 50, "player_level": 2, "max_player_hp": 50, "light_damage": 16, "medium_damage": 20,
                    "heavy_damage": 25, "special_attack": "FULL SCHOLARSHIP BLAST", "class_level": "CHAMPION",
                    "player_xp": 800, "re-rolls": 0, "player_class": "SCHOOL JOCK"}
        self.assertEqual(actual, expected)

    def test_computer_nerd_level_up_level_three(self):
        character_stats = {"player_hp": 40, "player_level": 2, "max_player_hp": 40, "light_damage": 16,
                           "medium_damage": 20, "heavy_damage": 25, "special_attack": "MULTIPLE MONITOR LIGHT SHOW",
                           "class_level": "pwnz0r", "player_xp": 800, "re-rolls": 0, "player_class": "COMPUTER NERD"}
        game.class_level_3(character_stats)
        actual = character_stats
        expected = {"player_hp": 40, "player_level": 2, "max_player_hp": 40, "light_damage": 16, "medium_damage": 20,
                    "heavy_damage": 25, "special_attack": "BATTLESTATION SYMPHONY", "class_level": "1337 h4x0r",
                    "player_xp": 800, "re-rolls": 0, "player_class": "COMPUTER NERD"}
        self.assertEqual(actual, expected)

    def test_the_natural_level_up_level_three(self):
        character_stats = {"player_hp": 40, "player_level": 2, "max_player_hp": 40, "light_damage": 16,
                           "medium_damage": 20, "heavy_damage": 25, "special_attack": "STRATEGIC ATTACK",
                           "class_level": "IDEALIST", "player_xp": 800, "re-rolls": 0, "player_class": "THE NATURAL"}
        game.class_level_3(character_stats)
        actual = character_stats
        expected = {"player_hp": 40, "player_level": 2, "max_player_hp": 40, "light_damage": 16, "medium_damage": 20,
                    "heavy_damage": 25, "special_attack": "BLOODY MASSACRE", "class_level": "SURVIVALIST", "player_xp":
                        800, "re-rolls": 0, "player_class": "THE NATURAL"}
        self.assertEqual(actual, expected)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_Level_2_level_up_print_message(self, mock_output):
        character_stats = {"player_hp": 40, "player_level": 2, "max_player_hp": 40, "light_damage": 16,
                           "medium_damage": 20, "heavy_damage": 25, "special_attack": "STRATEGIC ATTACK",
                           "class_level": "IDEALIST", "player_xp": 800, "re-rolls": 0, "player_class": "THE NATURAL"}
        game.class_level_3(character_stats)
        the_function_printed_this = mock_output.getvalue()
        expected_output = f"\n{TextColors.YELLOW}~~~~You have leveled up to level 3. Congratulations!~~~~\n\n\n" \
                          f"{TextColors.PURPLE}CLASS: {character_stats['player_class']}\n\n{TextColors.YELLOW}" \
                          f"::LEVEL GAINS::\n{TextColors.BLUE}SUBCLASS: {character_stats['class_level']}\n" \
                          f"{TextColors.RED}SPECIAL ATTACK: {character_stats['special_attack']}\nDAMAGE +10\n" \
                          f"{TextColors.CYAN}+10 HP{TextColors.ENDC}\n"
        self.assertEqual(expected_output, the_function_printed_this)
