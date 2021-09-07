"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 28, 2021
"""

from unittest import TestCase
import game


class Test(TestCase):

    def test_validate_player_missed_attack(self):
        character_stats = {"enemy_hp": 10}
        initial_enemy_hp = 10
        actual = game.validate_missed_attack(character_stats, initial_enemy_hp)
        expected = "missed"
        self.assertEqual(actual, expected)

    def test_validate_player_successful_attack_mid_value(self):
        character_stats = {"enemy_hp": 5}
        initial_enemy_hp = 10
        actual = game.validate_missed_attack(character_stats, initial_enemy_hp)
        expected = None
        self.assertEqual(actual, expected)

    def test_validate_player_successful_attack_zero_value(self):
        character_stats = {"enemy_hp": 0}
        initial_enemy_hp = 10
        actual = game.validate_missed_attack(character_stats, initial_enemy_hp)
        expected = None
        self.assertEqual(actual, expected)
