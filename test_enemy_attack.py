"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 27, 2021
"""

from unittest import TestCase
import unittest.mock
from unittest.mock import patch
import io
import game


class Test(TestCase):

    @patch('random.randint', side_effect=[3])
    def test_player_hp_change_nonzero_result(self, random_number_generator):
        character_stats = {'player_hp': 30, 'current_location': (3, 4), 'player_level': 1}
        game.enemy_attack(character_stats)
        actual_hp_result = character_stats["player_hp"]
        expected_hp_result = 27
        self.assertEqual(actual_hp_result, expected_hp_result)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @patch('random.randint', side_effect=[3])
    def test_player_damage_print_messages(self, random_number_generator, mock_output):
        character_stats = {'player_hp': 30, 'current_location': (3, 4), 'player_level': 1}
        game.enemy_attack(character_stats)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYour foe attacks!\nYou take 3 damage!\nYou now have 27 health points.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @patch('random.randint', side_effect=[29])
    def test_player_max_damage_nondeath_print_messages(self, random_number_generator, mock_output):
        character_stats = {'player_hp': 30, 'current_location': (3, 4), 'player_level': 1}
        game.enemy_attack(character_stats)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYour foe attacks!\nYou take 29 damage!\nYou now have 1 health points.\n"
        self.assertEqual(expected_output, the_function_printed_this)
