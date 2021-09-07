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


class TestStartScreen(TestCase):

    @patch('builtins.input', side_effect=[''])
    def test_return_none(self, mock_input):
        actual = game.start_screen()
        expected = None
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_game_title(self, mock_stdout, mock_input):
        game.start_screen()
        expected = r"""
 ██░ ██ ▒█████  ██▀███  ██▀███  ▒█████  ██▀███      ███▄ ▄███▓▒█████  ██▒   █▓██▓█████
▓██░ ██▒██▒  ██▓██ ▒ ██▓██ ▒ ██▒██▒  ██▓██ ▒ ██▒   ▓██▒▀█▀ ██▒██▒  ██▓██░   █▓██▓█   ▀
▒██▀▀██▒██░  ██▓██ ░▄█ ▓██ ░▄█ ▒██░  ██▓██ ░▄█ ▒   ▓██    ▓██▒██░  ██▒▓██  █▒▒██▒███
░▓█ ░██▒██   ██▒██▀▀█▄ ▒██▀▀█▄ ▒██   ██▒██▀▀█▄     ▒██    ▒██▒██   ██░ ▒██ █░░██▒▓█  ▄
░▓█▒░██░ ████▓▒░██▓ ▒██░██▓ ▒██░ ████▓▒░██▓ ▒██▒   ▒██▒   ░██░ ████▓▒░  ▒▀█░ ░██░▒████▒
 ▒ ░░▒░░ ▒░▒░▒░░ ▒▓ ░▒▓░ ▒▓ ░▒▓░ ▒░▒░▒░░ ▒▓ ░▒▓░   ░ ▒░   ░  ░ ▒░▒░▒░   ░ ▐░ ░▓ ░░ ▒░ ░
 ▒ ░▒░ ░ ░ ▒ ▒░  ░▒ ░ ▒░ ░▒ ░ ▒░ ░ ▒ ▒░  ░▒ ░ ▒░   ░  ░      ░ ░ ▒ ▒░   ░ ░░  ▒ ░░ ░  ░
 ░  ░░ ░ ░ ░ ▒   ░░   ░  ░░   ░░ ░ ░ ▒   ░░   ░    ░      ░  ░ ░ ░ ▒      ░░  ▒ ░  ░
 ░  ░  ░   ░ ░    ░       ░        ░ ░    ░               ░      ░ ░       ░  ░    ░  ░
               ▓█████  ██████ ▄████▄  ▄▄▄      ██▓███ ▓█████              ░
               ▓█   ▀▒██    ▒▒██▀ ▀█ ▒████▄   ▓██░  ██▓█   ▀
               ▒███  ░ ▓██▄  ▒▓█    ▄▒██  ▀█▄ ▓██░ ██▓▒███
               ▒▓█  ▄  ▒   ██▒▓▓▄ ▄██░██▄▄▄▄██▒██▄█▓▒ ▒▓█  ▄
               ░▒████▒██████▒▒ ▓███▀ ░▓█   ▓██▒██▒ ░  ░▒████▒
               ░░ ▒░ ▒ ▒▓▒ ▒ ░ ░▒ ▒  ░▒▒   ▓▒█▒▓▒░ ░  ░░ ▒░ ░
                ░ ░  ░ ░▒  ░ ░ ░  ▒    ▒   ▒▒ ░▒ ░     ░ ░  ░
                  ░  ░  ░  ░ ░         ░   ▒  ░░         ░
                  ░  ░     ░ ░ ░           ░  ░          ░  ░
                             ░

"""
        self.assertEqual(mock_stdout.getvalue(), expected)
