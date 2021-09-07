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

    @patch('random.randint', side_effect=[100, 1])
    def test_player_max_initiative(self, random_number_generator):
        actual = game.roll_for_initiative()
        expected = "player"
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[2, 1])
    def test_player_rolled_minimally_higher(self, random_number_generator):
        actual = game.roll_for_initiative()
        expected = "player"
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[1, 100])
    def test_enemy_max_initiative(self, random_number_generator):
        actual = game.roll_for_initiative()
        expected = "enemy"
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[1, 2])
    def test_enemy_rolled_minimally_higher(self, random_number_generator):
        actual = game.roll_for_initiative()
        expected = "enemy"
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[50, 50])
    def test_both_parties_rolled_same_value_return(self, random_number_generator):
        actual = game.roll_for_initiative()
        expected = None
        self.assertEqual(actual, expected)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @patch('random.randint', side_effect=[50, 50])
    def test_both_parties_rolled_same_value_print(self, random_number_generator, mock_output):
        game.roll_for_initiative()
        the_function_printed_this = mock_output.getvalue()
        expected = "\nEnter combat round !!!!!! \nRoll die for initiative (drumroll please ......)\n\nWow you just " \
                   "experienced the 0.0001 probability where both sides roll the same number on a 100 side die.\nIf I " \
                   "were you, I'd go buy a lottery ticket right now ;)\n"
        self.assertEqual(the_function_printed_this, expected)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @patch('random.randint', side_effect=[51, 50])
    def test_player_rolled_higher_print_messages(self, random_number_generator, mock_output):
        game.roll_for_initiative()
        the_function_printed_this = mock_output.getvalue()
        expected = "\nEnter combat round !!!!!! \nRoll die for initiative (drumroll please ......)\n\nYou've rolled a " \
                   "bigger number! You're striking first!\n"
        self.assertEqual(the_function_printed_this, expected)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    @patch('random.randint', side_effect=[50, 51])
    def test_enemy_rolled_higher_print_messages(self, random_number_generator, mock_output):
        game.roll_for_initiative()
        the_function_printed_this = mock_output.getvalue()
        expected = "\nEnter combat round !!!!!! \nRoll die for initiative (drumroll please ......)\n\nThe enemy " \
                   "rolled a bigger number! The enemy is striking first!\n"
        self.assertEqual(the_function_printed_this, expected)
