"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 28, 2021
"""

from unittest import TestCase
import game


class Test(TestCase):

    def test_user_input_1(self):
        character_stats = {"x_coordinate": 0, "y_coordinate": 2}
        valid_move = game.validate_move("1", character_stats)
        self.assertTrue(valid_move)

    def test_user_input_2(self):
        character_stats = {"x_coordinate": 0, "y_coordinate": 22}
        valid_move = game.validate_move("2", character_stats)
        self.assertTrue(valid_move)

    def test_user_input_3(self):
        character_stats = {"x_coordinate": 14, "y_coordinate": 24}
        valid_move = game.validate_move("3", character_stats)
        self.assertTrue(valid_move)

    def test_user_input_4(self):
        character_stats = {"x_coordinate": 16, "y_coordinate": 0}
        valid_move = game.validate_move("4", character_stats)
        self.assertTrue(valid_move)

    def test_invalid_move(self):
        character_stats = {"y_coordinate": 0, "x_coordinate": 1}
        valid_move = game.validate_move("1", character_stats)
        self.assertFalse(valid_move)
