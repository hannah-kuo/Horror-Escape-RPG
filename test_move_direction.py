"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 28, 2021
"""

from unittest import TestCase
import game


class Test(TestCase):

    def test_user_input_1(self):
        character_stats = {"x_coordinate": 0, "y_coordinate": 2, "current_location": (0, 2)}
        game.move_direction(character_stats, "1")
        actual = character_stats["current_location"]
        expected = (0, 1)
        self.assertEqual(actual, expected)

    def test_user_input_2(self):
        character_stats = {"x_coordinate": 0, "y_coordinate": 2, "current_location": (0, 2)}
        game.move_direction(character_stats, "2")
        actual = character_stats["current_location"]
        expected = (0, 3)
        self.assertEqual(actual, expected)

    def test_user_input_3(self):
        character_stats = {"x_coordinate": 16, "y_coordinate": 8, "current_location": (16, 8)}
        game.move_direction(character_stats, "3")
        actual = character_stats["current_location"]
        expected = (17, 8)
        self.assertEqual(actual, expected)

    def test_user_input_4(self):
        character_stats = {"x_coordinate": 24, "y_coordinate": 20, "current_location": (24, 20)}
        game.move_direction(character_stats, "4")
        actual = character_stats["current_location"]
        expected = (23, 20)
        self.assertEqual(actual, expected)
