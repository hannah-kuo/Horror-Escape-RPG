"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 28, 2021
"""

from unittest import TestCase
from unittest.mock import patch
import game


class Test(TestCase):

    @patch('builtins.input', side_effect=['0'])
    def test_return_true(self, mock_input):
        character_stats = {"enemy_hp": 15, "current_enemy": "Freddy", "player_hp": 30,
                           "enemy_description": "You find yourself incredibly sleepy. Time for a nap...you see a man "
                                                "wearing a fedora with the name \"Fred Krueger\" on the side. He "
                                                "lunges toward you."}
        combat_decision = game.choose_to_combat(character_stats)
        self.assertTrue(combat_decision)

    @patch('builtins.input', side_effect=['1'])
    def test_return_false(self, mock_input):
        character_stats = {"enemy_hp": 15, "current_enemy": "Freddy", "player_hp": 29,
                           "enemy_description": "You find yourself incredibly sleepy. Time for a nap...you see a man "
                                                "wearing a fedora with the name \"Fred Krueger\" on the side. He "
                                                "lunges toward you."}
        combat_decision = game.choose_to_combat(character_stats)
        self.assertFalse(combat_decision)

    @patch('builtins.input', side_effect=['0'])
    def test_return_bool(self, mock_input):
        character_stats = {"enemy_hp": 15, "current_enemy": "Freddy", "player_hp": 27,
                           "enemy_description": "You find yourself incredibly sleepy. Time for a nap...you see a man "
                                                "wearing a fedora with the name \"Fred Krueger\" on the side. He "
                                                "lunges toward you."}
        combat_decision = game.choose_to_combat(character_stats)
        self.assertIsInstance(combat_decision, bool)
