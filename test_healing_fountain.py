"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 27, 2021
"""

from unittest import TestCase
from unittest.mock import patch
import game


class TestHealingFountain(TestCase):

    @patch('builtins.input', side_effect=['0'])
    @patch('random.randint', return_value=5)
    def test_smallest_coin_number(self, random_number_generator, mock_input):
        character_stats = {'healing_landmarks': [(14, 12), (22, 3), (6, 8), (11, 21), (10, 16), (8, 5), (4, 1),
                                                 (3, 15)], 'current_location': (10, 16),
                           'player_hp': 20, "max_player_hp": 30}
        game.healing_fountain(character_stats)
        expected = 25
        actual = character_stats["player_hp"]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['0'])
    @patch('random.randint', return_value=10)
    def test_largest_coin_number(self, random_number_generator, mock_input):
        character_stats = {'healing_landmarks': [(14, 12), (22, 3), (6, 8), (11, 21), (10, 16), (8, 5), (5, 1),
                                                 (3, 15)], 'current_location': (5, 1),
                           'player_hp': 11, "max_player_hp": 30}
        game.healing_fountain(character_stats)
        expected = 21
        actual = character_stats["player_hp"]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    @patch('random.randint', return_value=10)
    def test_refuse_heal(self, random_number_generator, mock_input):
        character_stats = {'healing_landmarks': [(14, 12), (20, 3), (6, 8), (11, 21), (10, 16), (8, 5), (5, 1),
                                                 (3, 15)], 'current_location': (20, 3),
                           'player_hp': 11, "max_player_hp": 30}
        game.healing_fountain(character_stats)
        expected = 11
        actual = character_stats["player_hp"]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['0'])
    @patch('random.randint', return_value=6)
    def test_healed_hp_exceeds_max_hp(self, random_number_generator, mock_input):
        character_stats = {'healing_landmarks': [(14, 12), (20, 3), (6, 8), (11, 21), (10, 16), (7, 5), (5, 1),
                                                 (3, 15)], 'current_location': (20, 3),
                           'player_hp': 28, "max_player_hp": 30}
        game.healing_fountain(character_stats)
        expected = 30
        actual = character_stats["player_hp"]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['0'])
    @patch('random.randint', return_value=7)
    def test_healed_hp_smaller_than_max_hp(self, random_number_generator, mock_input):
        character_stats = {'healing_landmarks': [(14, 12), (22, 3), (6, 8), (11, 21), (10, 16), (8, 5), (4, 1),
                                                 (3, 15)], 'current_location': (8, 5),
                           'player_hp': 11, "max_player_hp": 30}
        game.healing_fountain(character_stats)
        expected = 18
        actual = character_stats["player_hp"]
        self.assertEqual(expected, actual)
