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


class TestSuburbanNeighborhoodScreen(TestCase):

    @patch('builtins.input', side_effect=[''])
    def test_return_none(self, mock_input):
        actual = game.suburban_neighborhood_screen()
        expected = None
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_game_title(self, mock_stdout, mock_input):
        game.suburban_neighborhood_screen()
        expected = r"""________.   ._____________________________.
(///(////\  ///(///(///(///(///(///(///(////\
///(///(  \///(///(///(///(///(///(///(///(  \
//(///(   ///(///(///(///(///(///(///(///(   |
/(///(  .///(///(///(///(///(///(///(///(  . |
    | .' |  ___    ___    ___   _____  | .'| |
    | |.'| |_|_|  |_|_|  |_|_| |__|__| | |.' |
    | '  | |_|_|  |_|_|  |_|_| |__|__| | ' . ||'--:|
__  |  .'|    __   _____    _ %%%____  | .'| |  .|
__| | |.'|   |  | |__|__|  |_%%%%%___| ||.' .'.|   .'         .'
__| | '.'|   | .| |__|__|  |%%%:%%___| |' .'.|   .'         .'
____|.'  |___|__|___________%%::%______|.'.|   .'         .'
       .|   '-=-.'            :'       .|    .'         .'
     .|   '   .               :      .|    .'         .'
   .|   '   .                       .|   .'         .'
  |'--'|==||'--'|'--'|'--'|'--'|'-'|   .'         .'
===jim================================'         .'
.    ...   ...   ...   ...   ...              .'
================================.
                              .'         .'
                            .'         .'
"""
        self.assertEqual(mock_stdout.getvalue(), expected)
