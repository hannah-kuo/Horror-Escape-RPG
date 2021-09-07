"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 26, 2021
"""

from unittest import TestCase
import game


class TestJoiningTuple(TestCase):

    def test_zeros(self):
        first_number = 0
        second_number = 0
        actual = game.joining_tuple(first_number, second_number)
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_non_zeros(self):
        first_number = 10
        second_number = 7
        actual = game.joining_tuple(first_number, second_number)
        expected = (10, 7)
        self.assertEqual(expected, actual)

    def test_border_coordinates(self):
        first_number = 24
        second_number = 24
        actual = game.joining_tuple(first_number, second_number)
        expected = (24, 24)
        self.assertEqual(expected, actual)
