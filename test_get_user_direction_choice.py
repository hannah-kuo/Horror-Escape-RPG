"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 27, 2021
"""

from unittest import TestCase
from unittest.mock import patch
import game


class TestGetUserDirectionChoice(TestCase):

    @patch('builtins.input', side_effect=['0'])
    def test_quit(self, mock_input):
        character_stats = {"current_location": (1, 2)}
        actual = game.get_user_direction_choice(character_stats)
        expected = "0"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['1'])
    def test_north(self, mock_input):
        character_stats = {"current_location": (0, 0)}
        actual = game.get_user_direction_choice(character_stats)
        expected = "1"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_south(self, mock_input):
        character_stats = {"current_location": (0, 10)}
        actual = game.get_user_direction_choice(character_stats)
        expected = "2"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['3'])
    def test_east(self, mock_input):
        character_stats = {"current_location": (23, 17)}
        actual = game.get_user_direction_choice(character_stats)
        expected = "3"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['4'])
    def test_west(self, mock_input):
        character_stats = {"current_location": (16, 3)}
        actual = game.get_user_direction_choice(character_stats)
        expected = "4"
        self.assertEqual(actual, expected)
