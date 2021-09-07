"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 27, 2021
"""

from unittest import TestCase
import unittest.mock
import io
import game


class Test(TestCase):

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_medium_attack_hit_print_messages(self, mock_output):
        character_stats = {"enemy_hp": 20, "medium_damage": 10, "medium_attack_hit_chance": 7}
        game.medium_attack(character_stats, 7)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou have chosen medium attack. Solid safe choice.\n\nYou attack! \nYou deal " \
                          "10 damage!\n"
        self.assertEqual(expected_output, the_function_printed_this)

    def test_enemy_hp_update_mid_value(self):
        character_stats = {"enemy_hp": 20, "medium_damage": 10, "medium_attack_hit_chance": 7}
        game.medium_attack(character_stats, 7)
        actual_hp = character_stats["enemy_hp"]
        expected_hp = 10
        self.assertEqual(actual_hp, expected_hp)

    def test_enemy_hp_update_low_value(self):
        character_stats = {"enemy_hp": 20, "medium_damage": 1, "medium_attack_hit_chance": 7}
        game.medium_attack(character_stats, 7)
        actual_hp = character_stats["enemy_hp"]
        expected_hp = 19
        self.assertEqual(actual_hp, expected_hp)

    def test_enemy_hp_update_zero_value(self):
        character_stats = {"enemy_hp": 10, "medium_damage": 10, "medium_attack_hit_chance": 7}
        game.medium_attack(character_stats, 7)
        actual_hp = character_stats["enemy_hp"]
        expected_hp = 0
        self.assertEqual(actual_hp, expected_hp)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_medium_attack_missed(self, mock_output):
        character_stats = {"enemy_hp": 10, "medium_damage": 10, "medium_attack_hit_chance": 7}
        game.medium_attack(character_stats, 9)
        the_function_printed_this = mock_output.getvalue()
        expected_output = "\nYou have chosen medium attack. Solid safe choice.\nOh no! You panicked and missed " \
                          "your shot!\n"
        self.assertEqual(expected_output, the_function_printed_this)
