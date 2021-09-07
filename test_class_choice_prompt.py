"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 27, 2021
"""

from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import game


class TestClassChoicePrompt(TestCase):

    @patch('builtins.input', side_effect=['0'])
    def test_shrieking_stumbler(self, mock_input):
        actual = game.class_choice_prompt()
        expected = "0"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_school_jock(self, mock_input):
        actual = game.class_choice_prompt()
        expected = "1"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_computer_nerd(self, mock_input):
        actual = game.class_choice_prompt()
        expected = "2"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_the_natural(self, mock_input):
        actual = game.class_choice_prompt()
        expected = "3"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input(self, mock_stdout, mock_input):
        game.class_choice_prompt()
        expected = "Please enter a valid input.\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
