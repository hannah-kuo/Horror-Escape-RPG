"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 26, 2021
"""

from unittest import TestCase
from unittest.mock import patch
import game


class TestCreateCharacter(TestCase):

    @patch('builtins.input', side_effect=['horror'])
    def test_name_input(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["name"]
        expected = "horror"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_x_coordinate(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["x_coordinate"]
        expected = 0
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_y_coordinate(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["y_coordinate"]
        expected = 0
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_current_location(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["current_location"]
        expected = (0, 0)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_player_xp(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["player_xp"]
        expected = 0
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_level_one_player_hp(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["player_hp"]
        expected = 30
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_level_one_player_level(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["player_level"]
        expected = 1
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_level_one_max_player_hp(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["max_player_hp"]
        expected = 30
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_level_one_light_damage(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["light_damage"]
        expected = 6
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_level_one_medium_damage(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["medium_damage"]
        expected = 10
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_level_one_heavy_damage(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["heavy_damage"]
        expected = 15
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_heavy_attack_hit_chance(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["heavy_attack_hit_chance"]
        expected = 4
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_heavy_attack_critical_hit_chance(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["heavy_attack_critical_hit_chance"]
        expected = 8
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_medium_attack_hit_chance(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["medium_attack_hit_chance"]
        expected = 7
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_light_attack_hit_chance(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["light_attack_hit_chance"]
        expected = 10
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['horror'])
    def test_light_attack_critical_hit_chance(self, mock_input):
        character_stats = {}
        game.create_character(character_stats)
        actual = character_stats["light_attack_critical_hit_chance"]
        expected = 8
        self.assertEqual(expected, actual)
