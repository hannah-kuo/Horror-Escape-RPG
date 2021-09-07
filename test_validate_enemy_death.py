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
    def test_print_messages_awarded_experience_points(self, mock_output):
        character_stats = {"enemy_hp": 0, "player_xp": 100}
        game.validate_enemy_death(character_stats)
        the_function_printed_this = mock_output.getvalue()
        expected_output = f"You have defeated your foe! You're a true warrior! You gained 100 experience points and " \
                          f"now you have {character_stats['player_xp']} xp.\n"
        self.assertEqual(expected_output, the_function_printed_this)

    def test_enemy_death_validated(self):
        character_stats = {"enemy_hp": 0, "player_xp": 100}
        actual = game.validate_enemy_death(character_stats)
        expected = True
        self.assertEqual(actual, expected)

    def test_enemy_not_dead_validated(self):
        character_stats = {"enemy_hp": 10, "player_xp": 100}
        actual = game.validate_enemy_death(character_stats)
        expected = False
        self.assertEqual(actual, expected)

    def test_experience_points_correctly_awarded(self):
        character_stats = {"enemy_hp": 0, "player_xp": 100}
        game.validate_enemy_death(character_stats)
        actual = character_stats["player_xp"]
        expected = 200
        self.assertEqual(actual, expected)
