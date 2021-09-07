"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 28, 2021
"""

from unittest import TestCase
from unittest.mock import patch
import game


class Test(TestCase):

    @patch('random.randint', return_value=1)
    def test_randomizer_lower_bound(self, random_number_generator):
        character_stats = {"player_hp": 10}
        enemy_exists = game.check_for_enemy(character_stats)
        self.assertTrue(enemy_exists)

    @patch('random.randint', return_value=10)
    def test_randomizer_upper_bound(self, random_number_generator):
        character_stats = {"player_hp": 10, "max_player_hp": 30}
        enemy_exists = game.check_for_enemy(character_stats)
        self.assertFalse(enemy_exists)

    @patch('random.randint', return_value=5)
    def test_middle_number(self, random_number_generator):
        character_stats = {"player_hp": 10, "max_player_hp": 30}
        enemy_exists = game.check_for_enemy(character_stats)
        self.assertFalse(enemy_exists)

    @patch('random.randint', return_value=8)
    def test_healed_hp_larger_than_max_hp(self, random_number_generator):
        character_stats = {"player_hp": 28, "max_player_hp": 30}
        game.check_for_enemy(character_stats)
        actual = character_stats["player_hp"]
        expected = 30
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)
    def test_healed_hp_lower_than_max_hp(self, random_number_generator):
        character_stats = {"player_hp": 14, "max_player_hp": 30}
        game.check_for_enemy(character_stats)
        actual = character_stats["player_hp"]
        expected = 18
        self.assertEqual(actual, expected)
