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


class TextColors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'


class TestDescriptionPrint(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_shrieking_stumbler_description(self, mock_stdout):
        class_choice = "0d"
        game.description_print(class_choice)
        expected = \
            f"\n\n{TextColors.PURPLE}CLASS: SHRIEKING STUMBLER\n\n{TextColors.YELLOW}The {TextColors.PURPLE}SHRIEKING "\
            f"STUMBLER {TextColors.YELLOW}is great at screaming and yelling and falling, but still manages to " \
            f"survive. They are also very good at picking up items they find\nfrom the ample time they spend on the " \
            f"ground.\n\n{TextColors.BLUE}SUBCLASS: DAY TRIPPER\n{TextColors.RED}SPECIAL ATTACK: STICK STAB\n" \
            f"{TextColors.CYAN}CLASS BENEFIT: ONE EXTRA CHANCE TO ATTACK ON MISSED ATTACK{TextColors.ENDC}\n\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_school_jock_description(self, mock_stdout):
        class_choice = "1d"
        game.description_print(class_choice)
        expected = \
            f"\n\n{TextColors.PURPLE}CLASS: SCHOOL JOCK\n\n{TextColors.YELLOW}The {TextColors.PURPLE}SCHOOL JOCK " \
            f"{TextColors.YELLOW}is tough to defeat. After long hours of extracurricular sports-ing, taking down a " \
            f"ghost or a killer hardly makes them break a sweat.\n\n{TextColors.BLUE}SUBCLASS: FRESHMAN\n" \
            f"{TextColors.RED}SPECIAL ATTACK: HOCKEY STICK SWING\n{TextColors.CYAN}CLASS BENEFIT: +10 HP" \
            f"{TextColors.ENDC}\n\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_computer_nerd_description(self, mock_stdout):
        class_choice = "2d"
        game.description_print(class_choice)
        expected = \
            f"\n\n{TextColors.PURPLE}CLASS: COMPUTER NERD\n\n{TextColors.YELLOW}The {TextColors.PURPLE}COMPUTER NERD " \
            f"{TextColors.YELLOW}knows that a strategic plan wins the day. With their know-how and Googling skills, " \
            f"enemies are just another bug to squash.\n\n{TextColors.BLUE}SUBCLASS: n00b\n{TextColors.RED}SPECIAL " \
            f"ATTACK: MECHANICAL KEYBOARD CLICKING\n{TextColors.CYAN}CLASS BENEFIT: LIGHT ATTACK - 100% CHANCE OF " \
            f"CRITICAL HIT CHANCE{TextColors.ENDC}\n\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_the_natural_description(self, mock_stdout):
        class_choice = "3d"
        game.description_print(class_choice)
        expected = \
            f"\n\n{TextColors.PURPLE}CLASS: THE NATURAL\n\n{TextColors.YELLOW}The {TextColors.PURPLE}THE NATURAL " \
            f"{TextColors.YELLOW}was just another person in the crowd until they felt the rush of their first fight. " \
            f"It's now unclear who the real killer is.\n\n{TextColors.BLUE}SUBCLASS: DAYDREAMER\n{TextColors.RED}" \
            f"SPECIAL ATTACK: LUCKY STRIKE\n{TextColors.CYAN}CLASS BENEFIT: HEAVY ATTACK - 60% CHANCE OF CRITICAL " \
            f"HIT CHANCE{TextColors.ENDC}\n\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
