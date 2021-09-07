"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 26, 2021
"""

from unittest import TestCase
import game


class TestMakeBoard(TestCase):

    def test_heal_locations(self):
        character_stats = {"healing_landmarks": [(13, 19), (16, 11), (20, 4), (4, 18), (3, 1), (19, 5), (10, 8),
                                                 (1, 12)], "current_location": (0, 0)}
        board = game.make_board(character_stats)
        correct_change = False
        if board[(13, 19)] == "heal" and board[(16, 11)] == "heal" and board[(20, 4)] == "heal" \
                and board[(4, 18)] == "heal" and board[(3, 1)] == "heal" and board[(19, 5)] == "heal"\
                and board[(10, 8)] == "heal" and board[(1, 12)] == "heal":
            correct_change = True
        self.assertTrue(correct_change)

    def test_boss_location(self):
        character_stats = {"healing_landmarks": [(2, 15), (21, 9), (12, 5), (20, 6), (13, 21), (11, 16), (10, 19),
                                                 (19, 2)], "current_location": (0, 0)}
        board = game.make_board(character_stats)
        correct_change = False
        if board[(12, 24)] == "boss":
            correct_change = True
        self.assertTrue(correct_change)

    def test_starting_location(self):
        character_stats = {"healing_landmarks": [(1, 5), (5, 20), (21, 8), (20, 6), (7, 14), (22, 15), (6, 2),
                                                 (9, 12)], "current_location": (0, 0)}
        board = game.make_board(character_stats)
        correct_change = False
        if board[(0, 0)] is True:
            correct_change = True
        self.assertTrue(correct_change)

    def test_all_tuple_keys(self):
        character_stats = {"healing_landmarks": [(19, 11), (5, 19), (1, 5), (11, 12), (7, 8), (2, 6), (12, 18),
                                                 (14, 20)], "current_location": (0, 0)}
        board = game.make_board(character_stats)
        for key in board:
            self.assertTrue(type(key) is tuple)

    def test_length_of_board_dictionary(self):
        character_stats = {"healing_landmarks": [(19, 11), (5, 19), (1, 5), (11, 11), (7, 8), (2, 6), (12, 18),
                                                 (14, 20)], "current_location": (0, 0)}
        board = game.make_board(character_stats)
        self.assertTrue(len(board) == 625)
