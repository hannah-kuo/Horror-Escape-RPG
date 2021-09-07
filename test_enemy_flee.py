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

    # @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @patch('random.randint', side_effect=[5])
    def test_enemy_does_not_flee(self, random_number_generator):
        actual = game.enemy_flee()
        expected = False
        self.assertEqual(actual, expected)

    # @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @patch('random.randint', side_effect=[2])
    def test_enemy_does_flee_maximum(self, random_number_generator):
        actual = game.enemy_flee()
        expected = True
        self.assertEqual(actual, expected)

    # @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @patch('random.randint', side_effect=[1])
    def test_enemy_does_flee_minimum(self, random_number_generator):
        actual = game.enemy_flee()
        expected = True
        self.assertEqual(actual, expected)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @patch('random.randint', side_effect=[2])
    def test_enemy_does_flee_prints_message_maximum(self, random_number_generator, mock_output):
        actual = game.enemy_flee()
        the_function_printed_this = mock_output.getvalue()
        expected = "\nThe enemy ran away.\n\n"
        self.assertEqual(the_function_printed_this, expected)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @patch('random.randint', side_effect=[1])
    def test_enemy_does_flee_prints_message_maximum(self, random_number_generator, mock_output):
        actual = game.enemy_flee()
        the_function_printed_this = mock_output.getvalue()
        expected = "\nThe enemy ran away.\n\n"
        self.assertEqual(the_function_printed_this, expected)
