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

    @patch('builtins.input', side_effect=['2'])
    @patch('random.randint', side_effect=[9, 7])
    def test_attack_miss(self, random_number_generator, mock_input):
        character_stats = {'name': 'Test', 'x_coordinate': 0, 'y_coordinate': 0, 'current_location': (0, 0),
                           'player_xp': 0, 'player_hp': 30, 'player_level': 1, 'max_player_hp': 30,
                           'light_damage': 6, 'medium_damage': 10, 'heavy_damage': 15,
                           'heavy_attack_hit_chance': 6, 'heavy_attack_critical_hit_chance': 8,
                           'medium_attack_hit_chance': 7, 'light_attack_hit_chance': 10,
                           'light_attack_critical_hit_chance': 8, 'player_class': 'THE NATURAL', 're-rolls': 0,
                           'special_attack': 'LUCKY STRIKE', 'class_level': 'DAYDREAMER', 'healing_landmarks':
                               [(14, 12), (22, 3), (6, 8), (11, 21), (10, 16), (8, 5), (4, 1), (3, 15)],
                           'height': 25, 'width': 25, 'enemy_hp': 15}
        actual = game.player_attack(character_stats)
        expected = "missed"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    @patch('random.randint', side_effect=[4, 2])
    def test_attack_hit(self, random_number_generator, mock_input):
        character_stats = {'name': 'Kevin', 'x_coordinate': 0, 'y_coordinate': 0, 'current_location': (0, 0),
                           'player_xp': 0, 'player_hp': 30, 'player_level': 1, 'max_player_hp': 30,
                           'light_damage': 6, 'medium_damage': 10, 'heavy_damage': 15,
                           'heavy_attack_hit_chance': 6, 'heavy_attack_critical_hit_chance': 8,
                           'medium_attack_hit_chance': 7, 'light_attack_hit_chance': 10,
                           'light_attack_critical_hit_chance': 8, 'player_class': 'THE NATURAL', 're-rolls': 0,
                           'special_attack': 'LUCKY STRIKE', 'class_level': 'DAYDREAMER', 'healing_landmarks':
                               [(14, 12), (22, 3), (6, 8), (11, 21), (10, 16), (8, 5), (4, 1), (3, 15)],
                           'height': 25, 'width': 25, 'enemy_hp': 15}
        actual = game.player_attack(character_stats)
        expected = None
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    @patch('random.randint', side_effect=[9, 2])
    def test_enemy_hp(self, random_number_generator, mock_input):
        character_stats = {'name': 'Malone', 'x_coordinate': 0, 'y_coordinate': 0, 'current_location': (0, 0),
                           'player_xp': 0, 'player_hp': 30, 'player_level': 1, 'max_player_hp': 30,
                           'light_damage': 6, 'medium_damage': 10, 'heavy_damage': 15,
                           'heavy_attack_hit_chance': 6, 'heavy_attack_critical_hit_chance': 8,
                           'medium_attack_hit_chance': 7, 'light_attack_hit_chance': 10,
                           'light_attack_critical_hit_chance': 8, 'player_class': 'THE NATURAL', 're-rolls': 0,
                           'special_attack': 'LUCKY STRIKE', 'class_level': 'DAYDREAMER', 'healing_landmarks':
                               [(14, 12), (22, 3), (6, 8), (11, 21), (10, 16), (8, 5), (4, 1), (3, 15)],
                           'height': 25, 'width': 25, 'enemy_hp': 16}
        game.player_attack(character_stats)
        actual = character_stats['enemy_hp']
        expected = 1
        self.assertEqual(actual, expected)
