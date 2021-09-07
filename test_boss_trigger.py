"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 27, 2021
"""

from unittest import TestCase
import game


class TestBossTrigger(TestCase):

    def test_not_at_boss_location(self):
        character_stats = {"current_location": (1, 11)}
        boss_triggered = game.boss_trigger(character_stats)
        self.assertFalse(boss_triggered)

    def test_enemy_hp(self):
        character_stats = {"current_location": (12, 24)}
        game.boss_trigger(character_stats)
        expected = 120
        actual = character_stats["enemy_hp"]
        self.assertEqual(actual, expected)

    def test_current_enemy(self):
        character_stats = {"current_location": (12, 24)}
        game.boss_trigger(character_stats)
        expected = "THE QUEEN XENOMORPH"
        actual = character_stats["current_enemy"]
        self.assertEqual(actual, expected)

    def test_enemy_description(self):
        character_stats = {"current_location": (12, 24)}
        game.boss_trigger(character_stats)
        expected = "You think you see a tail flick in the shadows. You come closer into a room whose oscillating " \
                   "fan cuts the light in fractional slices,\ncausing a strobe light effect. Is it your imagination, " \
                   "or is there a giant reptilian creature extending her dripping maw towards you?\nSuddenly, she " \
                   "rears up, the queen of the Xenomorphs. You back slowly into the P-5000 mecha suit conveniently " \
                   "behind you and prepare for battle.\nBeware, this will be a combat to the death.\n"
        actual = character_stats["enemy_description"]
        self.assertEqual(actual, expected)

    def test_return_true(self):
        character_stats = {"current_location": (12, 24)}
        boss_triggered = game.boss_trigger(character_stats)
        self.assertTrue(boss_triggered)
