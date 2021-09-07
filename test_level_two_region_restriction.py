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

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_at_gate_but_underleveled_print_message(self, mock_output):
        user_input = "2"
        character_stats = {"x_coordinate": 11, "player_level": 2, "y_coordinate": 14}
        game.level_two_region_restriction(user_input, character_stats)
        the_function_printed_this = mock_output.getvalue()
        expected_output = f"\n{TextColors.RED}You have arrived at the gate! \nHowever, the next region is locked " \
                          f"until you reach level 3! \nGo kill more enemies then come back!{TextColors.ENDC}\n"
        self.assertEqual(expected_output, the_function_printed_this)

    def test_at_gate_but_underleveled_y_coordinate_change(self):
        user_input = "2"
        character_stats = {"x_coordinate": 11, "player_level": 2, "y_coordinate": 14}
        game.level_two_region_restriction(user_input, character_stats)
        actual = character_stats["y_coordinate"]
        expected = 13
        self.assertEqual(actual, expected)

    def test_at_gate_but_overleveled(self):
        user_input = "2"
        character_stats = {"x_coordinate": 11, "player_level": 3, "y_coordinate": 8}
        actual = game.level_two_region_restriction(user_input, character_stats)
        expected = None
        self.assertEqual(actual, expected)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_at_wall_print_message(self, mock_output):
        user_input = "2"
        character_stats = {"x_coordinate": 9, "player_level": 2, "y_coordinate": 14}
        game.level_two_region_restriction(user_input, character_stats)
        the_function_printed_this = mock_output.getvalue()
        expected_output = f"\n{TextColors.RED}You think you can just walk past me?! \nNope! I'm a wall that " \
                          f"separates you and the next zone. \nPlease use the gates to go to the next region like a " \
                          f"normal human being!{TextColors.ENDC}\n"
        self.assertEqual(expected_output, the_function_printed_this)

    def test_at_wall_y_coordinate_change(self):
        user_input = "2"
        character_stats = {"x_coordinate": 9, "player_level": 2, "y_coordinate": 14}
        game.level_two_region_restriction(user_input, character_stats)
        actual = character_stats["y_coordinate"]
        expected = 13
        self.assertEqual(actual, expected)
