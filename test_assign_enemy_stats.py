"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 28, 2021
"""

from unittest import TestCase
from unittest.mock import patch
import game


class Test(TestCase):

    @patch('random.randint', return_value=1)
    def test_level_one_enemy_description(self, random_number_generator):
        character_stats = {"y_coordinate": 5, "enemy_hp": 15, "current_enemy": "Freddy",
                           "enemy_description": "You find yourself incredibly sleepy. Time for a nap...you see a man "
                                                "wearing a fedora with the name \"Fred Krueger\" on the side. He "
                                                "lunges toward you."}
        game.assign_enemy_stats(character_stats)
        actual = character_stats["enemy_description"]
        expected = "You stumble across a hotel. There is a dark figure stuffing something into the trunk of a " \
                   "car...could it be a body? Norman Bates isn't happy to see you...\"Mother\" isn't happy to see " \
                   "you..."
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=3)
    def test_level_two_enemy_name(self, random_number_generator):
        character_stats = {"y_coordinate": 10, "enemy_hp": 15, "current_enemy": "Freddy",
                           "enemy_description": "You find yourself incredibly sleepy. Time for a nap...you see a man "
                                                "wearing a fedora with the name \"Fred Krueger\" on the side. He "
                                                "lunges toward you."}
        game.assign_enemy_stats(character_stats)
        actual = character_stats["current_enemy"]
        expected = "Kayako"
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=6)
    def test_level_three_enemy_description(self, random_number_generator):
        character_stats = {"y_coordinate": 18, "enemy_hp": 15, "current_enemy": "Kayako",
                           "enemy_description": "You notice an old hut. \"Probably the graveyard keeper's shed\", "
                                                "you think to yourself. You wander inside, it's bigger than you "
                                                "thought. It appears to have Japanese-style sliding doors. \nYour "
                                                "blood runs cold when you see one slowly sliding open, a pale hand, "
                                                "gripping its frame. You hear a low, grating grumble, the sound of air "
                                                "escaping the throat of a vengeful, dying woman \nfor the last time. "
                                                "She lunges toward you, her black mouth agape and her long hair "
                                                "swinging in her face."}
        game.assign_enemy_stats(character_stats)
        actual = character_stats["enemy_description"]
        expected = "You feel your stomach grumble and decide to grab a snack. As you make your way to the cotton " \
                   "candy machine, you hear a giggle and something\nsmall brushes by you. But when you look down, " \
                   "no one is there. When you make it to the counter, there is a doll propped up by the machine." \
                   "\nYou feel yourself freeze in shock as you watch the doll's head swivel, and its beady eyes lock " \
                   "onto yours."
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=6)
    def test_level_two_enemy_hp(self, random_number_generator):
        character_stats = {"y_coordinate": 9, "enemy_hp": 15, "current_enemy": "Freddy",
                           "enemy_description": "You find yourself incredibly sleepy. Time for a nap...you see a man "
                                                "wearing a fedora with the name \"Fred Krueger\" on the side. He "
                                                "lunges toward you."}
        game.assign_enemy_stats(character_stats)
        actual = character_stats["enemy_hp"]
        expected = 20
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=5)
    def test_level_three_enemy_hp(self, random_number_generator):
        character_stats = {"y_coordinate": 21, "enemy_hp": 20, "current_enemy": "Freddy",
                           "enemy_description": "You find yourself incredibly sleepy. Time for a nap...you see a man "
                                                "wearing a fedora with the name \"Fred Krueger\" on the side. He "
                                                "lunges toward you."}
        game.assign_enemy_stats(character_stats)
        actual = character_stats["enemy_hp"]
        expected = 25
        self.assertEqual(actual, expected)
