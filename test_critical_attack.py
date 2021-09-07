"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 28, 2021
"""

from unittest import TestCase
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

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_critical_attack_light_damage_print_statements(self, mock_output):
        character_stats = {"enemy_hp": 10, "light_damage": 3, "special_attack": "LUCKY STRIKE"}
        game.critical_attack(character_stats, "0")
        critical_attack_printed_this = mock_output.getvalue()
        expected_output = f"\nWow! A special attack! \nYou perform {TextColors.GREEN}" \
                          f"{character_stats['special_attack']}{TextColors.GREEN}{TextColors.ENDC} and deal " \
                          f"{TextColors.RED}{character_stats['light_damage'] * 2}"f"{TextColors.ENDC} damage to the" \
                          f" enemy!\n"
        self.assertEqual(expected_output, critical_attack_printed_this)

    def test_critical_attack_light_damage_enemy_hp_change(self):
        character_stats = {"enemy_hp": 10, "light_damage": 3, "special_attack": "LUCKY STRIKE"}
        game.critical_attack(character_stats, "0")
        actual_hp = character_stats["enemy_hp"]
        expected_hp = 4
        self.assertEqual(actual_hp, expected_hp)

    @unittest.mock.patch("sys.stdout", new_callable=io.StringIO)
    def test_critical_attack_heavy_damage_print_statements(self, mock_output):
        character_stats = {"enemy_hp": 30, "heavy_damage": 10, "special_attack": "LUCKY STRIKE"}
        game.critical_attack(character_stats, "2")
        critical_attack_printed_this = mock_output.getvalue()
        expected_output = f"\nWow! A special attack! \nYou perform {TextColors.GREEN}" \
                          f"{character_stats['special_attack']}{TextColors.GREEN}{TextColors.ENDC} and deal " \
                          f"{TextColors.RED}{character_stats['heavy_damage'] * 2}{TextColors.ENDC} damage to the " \
                          f"enemy!\n"
        self.assertEqual(expected_output, critical_attack_printed_this)

    def test_critical_attack_heavy_damage_enemy_hp_change(self):
        character_stats = {"enemy_hp": 30, "heavy_damage": 10, "special_attack": "LUCKY STRIKE"}
        game.critical_attack(character_stats, "2")
        actual_hp = character_stats["enemy_hp"]
        expected_hp = 10
        self.assertEqual(actual_hp, expected_hp)
