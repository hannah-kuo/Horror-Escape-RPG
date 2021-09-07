"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 28, 2021
"""

from unittest import TestCase
import unittest.mock
import io
import game


class Test(TestCase):

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_heavy_attack_hit_print_messages(self, mock_output):
        character_stats = {"enemy_hp": 20, "heavy_damage": 15}
        game.heavy_attack(character_stats)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou have chosen heavy attack. Seems like you're a fan of high risk high reward.\n\nYou " \
                          "attack! \nYou deal 15 damage!\n"
        self.assertEqual(expected_output, the_function_printed_this)

    def test_enemy_hp_update_mid_value(self):
        character_stats = {"enemy_hp": 20, "heavy_damage": 15}
        game.heavy_attack(character_stats)
        actual_hp = character_stats["enemy_hp"]
        expected_hp = 5
        self.assertEqual(actual_hp, expected_hp)

    def test_enemy_hp_update_low_value(self):
        character_stats = {"enemy_hp": 20, "heavy_damage": 1}
        game.heavy_attack(character_stats)
        actual_hp = character_stats["enemy_hp"]
        expected_hp = 19
        self.assertEqual(actual_hp, expected_hp)

    def test_enemy_hp_update_zero_value(self):
        character_stats = {"enemy_hp": 10, "heavy_damage": 10}
        game.heavy_attack(character_stats)
        actual_hp = character_stats["enemy_hp"]
        expected_hp = 0
        self.assertEqual(actual_hp, expected_hp)
