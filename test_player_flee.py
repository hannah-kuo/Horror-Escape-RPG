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

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @patch('random.randint', side_effect=[3, 1])
    def test_player_safe(self, random_number_generator, mock_output):
        character_stats = {"player_hp": 30}
        game.player_flee(character_stats)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "Luck is on your side! You have successfully run away from the enemy.\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @patch('random.randint', side_effect=[2, 1])
    def test_player_back_stabbed(self, random_number_generator, mock_output):
        character_stats = {"player_hp": 30}
        game.player_flee(character_stats)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "AH! OUCH! OH NO! You've been back-stabbed by the enemy! You lost 1 hp.\nYou now have " \
                          "29 health points.\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('random.randint', side_effect=[2, 8])
    def test_player_hp_change(self, random_number_generator):
        character_stats = {"player_hp": 30}
        game.player_flee(character_stats)
        expected = 22
        actual = character_stats["player_hp"]
        self.assertEqual(expected, actual)
