"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 28, 2021
"""

from unittest import TestCase
from unittest.mock import patch
import unittest.mock
import io
import game


class TextColors:
    BLACK = '\033[30m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[37m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    NEGATIVE = '\033[3m'


class Test(TestCase):

    @patch('builtins.input', side_effect=[''])
    def test_return_none(self, mock_input):
        actual = game.graveyard_screen()
        expected = None
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_picture_print(self, mock_stdout, mock_input):
        game.graveyard_screen()
        expected = r"""
                  _  /)
                 mo / )
                 |/)\)
                  /\_
                  \__|=
                 (    )
                 __)(__
________+_______/      \_______+__________
- --_ _-| _               _    |---_   - -
  __--  |/_|) \ |\||\| /||_|  /|-_-- __
_ --_ - |\/|\/-\| ||/|/ ||_|// |   -_  -
_-- -   |_____ __________ _____|_ --  _
-_-- __  || | | | {|    /| | || __---  -_
 --__-   || | | | {|   /|| | ||--        -
         || | | | {|  /||| | ||__--
 __-- -__|| | | | {| |}||| | ||--   __--
         ||_|_|_|_{| |}|||_|_||  -__
 --__-  -|| | | | {& |}||/ | ||---   __--
         || | | | {| |}|/| | ||-__
--   __--|| | | | {| |}/|| | ||__-- -__
  --     || | | | {| &}||| | ||   __
---   __-|| | | | {| |}||| | ||_---__-  --
 -  -_   || | | | {| |}||| | || --
 __ejm 97|| | | | {| |}||| | ||_--__-   _---
_________||_|_|_|_{| |}|||_|_||______________
                     |}|/
                     |}/
                     |/

"""
        self.assertEqual(mock_stdout.getvalue(), expected)
