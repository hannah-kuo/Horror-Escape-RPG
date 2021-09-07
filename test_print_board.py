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


class TestPrintBoard(TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_board(self, mock_stdout):
        character_stats = {'height': 25, 'width': 25}
        board = \
            {(0, 0): False, (0, 1): False, (0, 2): False, (0, 3): False, (0, 4): False, (0, 5): False, (0, 6): False,
             (0, 7): False, (0, 8): False, (0, 9): False, (0, 10): False, (0, 11): False, (0, 12): False,
             (0, 13): False, (0, 14): False, (0, 15): False, (0, 16): False, (0, 17): False, (0, 18): False,
             (0, 19): False, (0, 20): False, (0, 21): False, (0, 22): False, (0, 23): False, (0, 24): False,
             (1, 0): False, (1, 1): False, (1, 2): False, (1, 3): False, (1, 4): False, (1, 5): False, (1, 6): False,
             (1, 7): False, (1, 8): False, (1, 9): False, (1, 10): False, (1, 11): False, (1, 12): False,
             (1, 13): False, (1, 14): False, (1, 15): False, (1, 16): False, (1, 17): False, (1, 18): False,
             (1, 19): False, (1, 20): False, (1, 21): False, (1, 22): False, (1, 23): False, (1, 24): False,
             (2, 0): False, (2, 1): False, (2, 2): False, (2, 3): False, (2, 4): False, (2, 5): False, (2, 6): False,
             (2, 7): False, (2, 8): False, (2, 9): False, (2, 10): False, (2, 11): False, (2, 12): False,
             (2, 13): False, (2, 14): False, (2, 15): False, (2, 16): False, (2, 17): False, (2, 18): False,
             (2, 19): False, (2, 20): False, (2, 21): False, (2, 22): False, (2, 23): False, (2, 24): False,
             (3, 0): False, (3, 1): False, (3, 2): False, (3, 3): False, (3, 4): False, (3, 5): False, (3, 6): False,
             (3, 7): False, (3, 8): False, (3, 9): False, (3, 10): False, (3, 11): False, (3, 12): False,
             (3, 13): False, (3, 14): False, (3, 15): False, (3, 16): False, (3, 17): False, (3, 18): False,
             (3, 19): False, (3, 20): False, (3, 21): False, (3, 22): False, (3, 23): False, (3, 24): False,
             (4, 0): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): False, (4, 5): False, (4, 6): False,
             (4, 7): False, (4, 8): False, (4, 9): False, (4, 10): False, (4, 11): False, (4, 12): False,
             (4, 13): False, (4, 14): False, (4, 15): False, (4, 16): False, (4, 17): False, (4, 18): False,
             (4, 19): False, (4, 20): False, (4, 21): False, (4, 22): False, (4, 23): False, (4, 24): False,
             (5, 0): False, (5, 1): False, (5, 2): False, (5, 3): False, (5, 4): False, (5, 5): False, (5, 6): False,
             (5, 7): False, (5, 8): False, (5, 9): False, (5, 10): False, (5, 11): False, (5, 12): False,
             (5, 13): False, (5, 14): False, (5, 15): False, (5, 16): False, (5, 17): False, (5, 18): False,
             (5, 19): False, (5, 20): False, (5, 21): False, (5, 22): False, (5, 23): False, (5, 24): False,
             (6, 0): False, (6, 1): False, (6, 2): False, (6, 3): False, (6, 4): False, (6, 5): False, (6, 6): False,
             (6, 7): False, (6, 8): False, (6, 9): False, (6, 10): False, (6, 11): False, (6, 12): False,
             (6, 13): False, (6, 14): False, (6, 15): False, (6, 16): False, (6, 17): False, (6, 18): False,
             (6, 19): False, (6, 20): False, (6, 21): False, (6, 22): False, (6, 23): False, (6, 24): False,
             (7, 0): False, (7, 1): False, (7, 2): False, (7, 3): False, (7, 4): False, (7, 5): False, (7, 6): False,
             (7, 7): False, (7, 8): False, (7, 9): False, (7, 10): False, (7, 11): False, (7, 12): False,
             (7, 13): False, (7, 14): False, (7, 15): False, (7, 16): False, (7, 17): False, (7, 18): False,
             (7, 19): False, (7, 20): False, (7, 21): False, (7, 22): False, (7, 23): False, (7, 24): False,
             (8, 0): False, (8, 1): False, (8, 2): False, (8, 3): False, (8, 4): False, (8, 5): False, (8, 6): False,
             (8, 7): False, (8, 8): False, (8, 9): False, (8, 10): False, (8, 11): False, (8, 12): False,
             (8, 13): False, (8, 14): False, (8, 15): False, (8, 16): False, (8, 17): False, (8, 18): False,
             (8, 19): False, (8, 20): False, (8, 21): False, (8, 22): False, (8, 23): False, (8, 24): False,
             (9, 0): False, (9, 1): False, (9, 2): False, (9, 3): False, (9, 4): False, (9, 5): False, (9, 6): False,
             (9, 7): False, (9, 8): False, (9, 9): False, (9, 10): False, (9, 11): False, (9, 12): False,
             (9, 13): False, (9, 14): False, (9, 15): False, (9, 16): False, (9, 17): False, (9, 18): False,
             (9, 19): False, (9, 20): False, (9, 21): False, (9, 22): False, (9, 23): False, (9, 24): False,
             (10, 0): False, (10, 1): False, (10, 2): False, (10, 3): False, (10, 4): False, (10, 5): False,
             (10, 6): False, (10, 7): False, (10, 8): False, (10, 9): False, (10, 10): False, (10, 11): False,
             (10, 12): False, (10, 13): False, (10, 14): False, (10, 15): False, (10, 16): False, (10, 17): False,
             (10, 18): False, (10, 19): False, (10, 20): False, (10, 21): False, (10, 22): False, (10, 23): False,
             (10, 24): False, (11, 0): False, (11, 1): False, (11, 2): False, (11, 3): False, (11, 4): False,
             (11, 5): False, (11, 6): False, (11, 7): False, (11, 8): False, (11, 9): False, (11, 10): False,
             (11, 11): False, (11, 12): False, (11, 13): False, (11, 14): False, (11, 15): False, (11, 16): False,
             (11, 17): False, (11, 18): False, (11, 19): False, (11, 20): False, (11, 21): False, (11, 22): False,
             (11, 23): False, (11, 24): False, (12, 0): False, (12, 1): False, (12, 2): False, (12, 3): False,
             (12, 4): False, (12, 5): False, (12, 6): False, (12, 7): False, (12, 8): False, (12, 9): False,
             (12, 10): False, (12, 11): False, (12, 12): False, (12, 13): False, (12, 14): False, (12, 15): False,
             (12, 16): False, (12, 17): False, (12, 18): False, (12, 19): False, (12, 20): False, (12, 21): False,
             (12, 22): False, (12, 23): False, (12, 24): False, (13, 0): False, (13, 1): False, (13, 2): False,
             (13, 3): False, (13, 4): False, (13, 5): False, (13, 6): False, (13, 7): False, (13, 8): False,
             (13, 9): False, (13, 10): False, (13, 11): False, (13, 12): False, (13, 13): False, (13, 14): False,
             (13, 15): False, (13, 16): False, (13, 17): False, (13, 18): False, (13, 19): False, (13, 20): False,
             (13, 21): False, (13, 22): False, (13, 23): False, (13, 24): False, (14, 0): False, (14, 1): False,
             (14, 2): False, (14, 3): False, (14, 4): False, (14, 5): False, (14, 6): False, (14, 7): False,
             (14, 8): False, (14, 9): False, (14, 10): False, (14, 11): False, (14, 12): False, (14, 13): False,
             (14, 14): False, (14, 15): False, (14, 16): False, (14, 17): False, (14, 18): False, (14, 19): False,
             (14, 20): False, (14, 21): False, (14, 22): False, (14, 23): False, (14, 24): False, (15, 0): False,
             (15, 1): False, (15, 2): False, (15, 3): False, (15, 4): False, (15, 5): False, (15, 6): False,
             (15, 7): False, (15, 8): False, (15, 9): False, (15, 10): False, (15, 11): False, (15, 12): False,
             (15, 13): False, (15, 14): False, (15, 15): False, (15, 16): False, (15, 17): False, (15, 18): False,
             (15, 19): False, (15, 20): False, (15, 21): False, (15, 22): False, (15, 23): False, (15, 24): False,
             (16, 0): False, (16, 1): False, (16, 2): False, (16, 3): False, (16, 4): False, (16, 5): False,
             (16, 6): False, (16, 7): False, (16, 8): False, (16, 9): False, (16, 10): False, (16, 11): False,
             (16, 12): False, (16, 13): False, (16, 14): False, (16, 15): False, (16, 16): False, (16, 17): False,
             (16, 18): False, (16, 19): False, (16, 20): False, (16, 21): False, (16, 22): False, (16, 23): False,
             (16, 24): False, (17, 0): False, (17, 1): False, (17, 2): False, (17, 3): False, (17, 4): False,
             (17, 5): False, (17, 6): False, (17, 7): False, (17, 8): False, (17, 9): False, (17, 10): False,
             (17, 11): False, (17, 12): False, (17, 13): False, (17, 14): False, (17, 15): False, (17, 16): False,
             (17, 17): False, (17, 18): False, (17, 19): False, (17, 20): False, (17, 21): False, (17, 22): False,
             (17, 23): False, (17, 24): False, (18, 0): False, (18, 1): False, (18, 2): False, (18, 3): False,
             (18, 4): False, (18, 5): False, (18, 6): False, (18, 7): False, (18, 8): False, (18, 9): False,
             (18, 10): False, (18, 11): False, (18, 12): False, (18, 13): False, (18, 14): False, (18, 15): False,
             (18, 16): False, (18, 17): False, (18, 18): False, (18, 19): False, (18, 20): False, (18, 21): False,
             (18, 22): False, (18, 23): False, (18, 24): False, (19, 0): False, (19, 1): False, (19, 2): False,
             (19, 3): False, (19, 4): False, (19, 5): False, (19, 6): False, (19, 7): False, (19, 8): False,
             (19, 9): False, (19, 10): False, (19, 11): False, (19, 12): False, (19, 13): False, (19, 14): False,
             (19, 15): False, (19, 16): False, (19, 17): False, (19, 18): False, (19, 19): False, (19, 20): False,
             (19, 21): False, (19, 22): False, (19, 23): False, (19, 24): False, (20, 0): False, (20, 1): False,
             (20, 2): False, (20, 3): False, (20, 4): False, (20, 5): False, (20, 6): False, (20, 7): False,
             (20, 8): False, (20, 9): False, (20, 10): False, (20, 11): False, (20, 12): False, (20, 13): False,
             (20, 14): False, (20, 15): False, (20, 16): False, (20, 17): False, (20, 18): False, (20, 19): False,
             (20, 20): False, (20, 21): False, (20, 22): False, (20, 23): False, (20, 24): False, (21, 0): False,
             (21, 1): False, (21, 2): False, (21, 3): False, (21, 4): False, (21, 5): False, (21, 6): False,
             (21, 7): False, (21, 8): False, (21, 9): False, (21, 10): False, (21, 11): False, (21, 12): False,
             (21, 13): False, (21, 14): False, (21, 15): False, (21, 16): False, (21, 17): False, (21, 18): False,
             (21, 19): False, (21, 20): False, (21, 21): False, (21, 22): False, (21, 23): False, (21, 24): False,
             (22, 0): False, (22, 1): False, (22, 2): False, (22, 3): False, (22, 4): False, (22, 5): False,
             (22, 6): False, (22, 7): False, (22, 8): False, (22, 9): False, (22, 10): False, (22, 11): False,
             (22, 12): False, (22, 13): False, (22, 14): False, (22, 15): False, (22, 16): False, (22, 17): False,
             (22, 18): False, (22, 19): False, (22, 20): False, (22, 21): False, (22, 22): False, (22, 23): False,
             (22, 24): False, (23, 0): False, (23, 1): False, (23, 2): False, (23, 3): False, (23, 4): False,
             (23, 5): False, (23, 6): False, (23, 7): False, (23, 8): False, (23, 9): False, (23, 10): False,
             (23, 11): False, (23, 12): False, (23, 13): False, (23, 14): False, (23, 15): False, (23, 16): False,
             (23, 17): False, (23, 18): False, (23, 19): False, (23, 20): False, (23, 21): False, (23, 22): False,
             (23, 23): False, (23, 24): False, (24, 0): False, (24, 1): False, (24, 2): False, (24, 3): False,
             (24, 4): False, (24, 5): False, (24, 6): False, (24, 7): False, (24, 8): False, (24, 9): False,
             (24, 10): False, (24, 11): False, (24, 12): False, (24, 13): False, (24, 14): False, (24, 15): False,
             (24, 16): False, (24, 17): False, (24, 18): False, (24, 19): False, (24, 20): False, (24, 21): False,
             (24, 22): False, (24, 23): False, (24, 24): False}
        game.print_board(character_stats, board)
        expected = \
            f"\n+-----------------------------------------------+\n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f"+--------------------[     ]--------------------+\n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f"+--------------------[     ]--------------------+\n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f"+-----------------------------------------------+\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_player_location(self, mock_stdout):
        character_stats = {'height': 25, 'width': 25}
        board = \
            {(0, 0): False, (0, 1): False, (0, 2): False, (0, 3): False, (0, 4): False, (0, 5): False, (0, 6): False,
             (0, 7): False, (0, 8): False, (0, 9): False, (0, 10): False, (0, 11): False, (0, 12): False,
             (0, 13): False, (0, 14): False, (0, 15): False, (0, 16): False, (0, 17): False, (0, 18): False,
             (0, 19): False, (0, 20): False, (0, 21): False, (0, 22): False, (0, 23): False, (0, 24): False,
             (1, 0): False, (1, 1): False, (1, 2): False, (1, 3): False, (1, 4): False, (1, 5): False, (1, 6): False,
             (1, 7): False, (1, 8): False, (1, 9): False, (1, 10): False, (1, 11): False, (1, 12): False,
             (1, 13): False, (1, 14): False, (1, 15): False, (1, 16): False, (1, 17): False, (1, 18): False,
             (1, 19): False, (1, 20): False, (1, 21): False, (1, 22): False, (1, 23): False, (1, 24): False,
             (2, 0): False, (2, 1): False, (2, 2): False, (2, 3): False, (2, 4): False, (2, 5): False, (2, 6): False,
             (2, 7): False, (2, 8): False, (2, 9): False, (2, 10): False, (2, 11): False, (2, 12): False,
             (2, 13): False, (2, 14): False, (2, 15): False, (2, 16): False, (2, 17): False, (2, 18): False,
             (2, 19): False, (2, 20): False, (2, 21): False, (2, 22): False, (2, 23): False, (2, 24): False,
             (3, 0): False, (3, 1): False, (3, 2): False, (3, 3): False, (3, 4): False, (3, 5): False, (3, 6): False,
             (3, 7): False, (3, 8): False, (3, 9): False, (3, 10): False, (3, 11): False, (3, 12): False,
             (3, 13): False, (3, 14): False, (3, 15): False, (3, 16): False, (3, 17): False, (3, 18): False,
             (3, 19): False, (3, 20): False, (3, 21): False, (3, 22): False, (3, 23): False, (3, 24): False,
             (4, 0): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): False, (4, 5): False, (4, 6): False,
             (4, 7): False, (4, 8): False, (4, 9): False, (4, 10): False, (4, 11): False, (4, 12): False,
             (4, 13): False, (4, 14): False, (4, 15): False, (4, 16): False, (4, 17): False, (4, 18): False,
             (4, 19): False, (4, 20): False, (4, 21): False, (4, 22): False, (4, 23): False, (4, 24): False,
             (5, 0): False, (5, 1): False, (5, 2): False, (5, 3): False, (5, 4): False, (5, 5): False, (5, 6): False,
             (5, 7): False, (5, 8): False, (5, 9): False, (5, 10): False, (5, 11): False, (5, 12): False,
             (5, 13): False, (5, 14): False, (5, 15): False, (5, 16): False, (5, 17): False, (5, 18): False,
             (5, 19): False, (5, 20): False, (5, 21): False, (5, 22): False, (5, 23): False, (5, 24): False,
             (6, 0): False, (6, 1): False, (6, 2): False, (6, 3): False, (6, 4): False, (6, 5): False, (6, 6): False,
             (6, 7): False, (6, 8): False, (6, 9): False, (6, 10): False, (6, 11): False, (6, 12): False,
             (6, 13): False, (6, 14): False, (6, 15): False, (6, 16): False, (6, 17): False, (6, 18): False,
             (6, 19): False, (6, 20): False, (6, 21): False, (6, 22): False, (6, 23): False, (6, 24): False,
             (7, 0): False, (7, 1): False, (7, 2): False, (7, 3): False, (7, 4): False, (7, 5): False, (7, 6): False,
             (7, 7): False, (7, 8): False, (7, 9): False, (7, 10): False, (7, 11): False, (7, 12): False,
             (7, 13): False, (7, 14): False, (7, 15): False, (7, 16): False, (7, 17): False, (7, 18): False,
             (7, 19): False, (7, 20): False, (7, 21): False, (7, 22): False, (7, 23): False, (7, 24): False,
             (8, 0): False, (8, 1): False, (8, 2): False, (8, 3): False, (8, 4): False, (8, 5): False, (8, 6): False,
             (8, 7): False, (8, 8): False, (8, 9): False, (8, 10): False, (8, 11): False, (8, 12): False,
             (8, 13): False, (8, 14): False, (8, 15): False, (8, 16): False, (8, 17): False, (8, 18): False,
             (8, 19): False, (8, 20): False, (8, 21): False, (8, 22): False, (8, 23): False, (8, 24): False,
             (9, 0): False, (9, 1): False, (9, 2): False, (9, 3): False, (9, 4): False, (9, 5): False, (9, 6): False,
             (9, 7): False, (9, 8): False, (9, 9): False, (9, 10): False, (9, 11): False, (9, 12): False,
             (9, 13): False, (9, 14): False, (9, 15): False, (9, 16): False, (9, 17): False, (9, 18): False,
             (9, 19): False, (9, 20): False, (9, 21): False, (9, 22): False, (9, 23): False, (9, 24): False,
             (10, 0): False, (10, 1): False, (10, 2): False, (10, 3): False, (10, 4): False, (10, 5): False,
             (10, 6): False, (10, 7): False, (10, 8): False, (10, 9): False, (10, 10): False, (10, 11): False,
             (10, 12): False, (10, 13): False, (10, 14): False, (10, 15): False, (10, 16): False, (10, 17): False,
             (10, 18): False, (10, 19): False, (10, 20): False, (10, 21): False, (10, 22): False, (10, 23): False,
             (10, 24): False, (11, 0): False, (11, 1): False, (11, 2): False, (11, 3): False, (11, 4): False,
             (11, 5): False, (11, 6): False, (11, 7): False, (11, 8): False, (11, 9): False, (11, 10): False,
             (11, 11): False, (11, 12): False, (11, 13): False, (11, 14): False, (11, 15): False, (11, 16): False,
             (11, 17): False, (11, 18): False, (11, 19): False, (11, 20): False, (11, 21): False, (11, 22): False,
             (11, 23): False, (11, 24): False, (12, 0): False, (12, 1): False, (12, 2): False, (12, 3): False,
             (12, 4): False, (12, 5): False, (12, 6): False, (12, 7): False, (12, 8): False, (12, 9): False,
             (12, 10): False, (12, 11): False, (12, 12): False, (12, 13): False, (12, 14): False, (12, 15): False,
             (12, 16): False, (12, 17): False, (12, 18): False, (12, 19): False, (12, 20): False, (12, 21): False,
             (12, 22): False, (12, 23): False, (12, 24): False, (13, 0): False, (13, 1): False, (13, 2): False,
             (13, 3): False, (13, 4): False, (13, 5): False, (13, 6): False, (13, 7): False, (13, 8): False,
             (13, 9): False, (13, 10): False, (13, 11): False, (13, 12): False, (13, 13): False, (13, 14): False,
             (13, 15): False, (13, 16): False, (13, 17): False, (13, 18): False, (13, 19): False, (13, 20): False,
             (13, 21): False, (13, 22): False, (13, 23): False, (13, 24): False, (14, 0): False, (14, 1): False,
             (14, 2): False, (14, 3): False, (14, 4): False, (14, 5): False, (14, 6): False, (14, 7): False,
             (14, 8): False, (14, 9): False, (14, 10): False, (14, 11): False, (14, 12): False, (14, 13): False,
             (14, 14): False, (14, 15): False, (14, 16): False, (14, 17): False, (14, 18): False, (14, 19): False,
             (14, 20): False, (14, 21): False, (14, 22): False, (14, 23): False, (14, 24): False, (15, 0): False,
             (15, 1): False, (15, 2): False, (15, 3): False, (15, 4): False, (15, 5): False, (15, 6): False,
             (15, 7): False, (15, 8): False, (15, 9): False, (15, 10): False, (15, 11): False, (15, 12): False,
             (15, 13): False, (15, 14): False, (15, 15): False, (15, 16): False, (15, 17): False, (15, 18): False,
             (15, 19): False, (15, 20): False, (15, 21): False, (15, 22): False, (15, 23): False, (15, 24): False,
             (16, 0): False, (16, 1): False, (16, 2): False, (16, 3): False, (16, 4): False, (16, 5): False,
             (16, 6): False, (16, 7): False, (16, 8): False, (16, 9): False, (16, 10): False, (16, 11): False,
             (16, 12): False, (16, 13): False, (16, 14): False, (16, 15): False, (16, 16): False, (16, 17): False,
             (16, 18): False, (16, 19): False, (16, 20): False, (16, 21): False, (16, 22): False, (16, 23): False,
             (16, 24): False, (17, 0): False, (17, 1): False, (17, 2): False, (17, 3): False, (17, 4): False,
             (17, 5): False, (17, 6): False, (17, 7): False, (17, 8): False, (17, 9): False, (17, 10): False,
             (17, 11): False, (17, 12): False, (17, 13): False, (17, 14): False, (17, 15): False, (17, 16): False,
             (17, 17): False, (17, 18): False, (17, 19): False, (17, 20): False, (17, 21): False, (17, 22): False,
             (17, 23): False, (17, 24): False, (18, 0): False, (18, 1): False, (18, 2): False, (18, 3): False,
             (18, 4): False, (18, 5): False, (18, 6): True, (18, 7): False, (18, 8): False, (18, 9): False,
             (18, 10): False, (18, 11): False, (18, 12): False, (18, 13): False, (18, 14): False, (18, 15): False,
             (18, 16): False, (18, 17): False, (18, 18): False, (18, 19): False, (18, 20): False, (18, 21): False,
             (18, 22): False, (18, 23): False, (18, 24): False, (19, 0): False, (19, 1): False, (19, 2): False,
             (19, 3): False, (19, 4): False, (19, 5): False, (19, 6): False, (19, 7): False, (19, 8): False,
             (19, 9): False, (19, 10): False, (19, 11): False, (19, 12): False, (19, 13): False, (19, 14): False,
             (19, 15): False, (19, 16): False, (19, 17): False, (19, 18): False, (19, 19): False, (19, 20): False,
             (19, 21): False, (19, 22): False, (19, 23): False, (19, 24): False, (20, 0): False, (20, 1): False,
             (20, 2): False, (20, 3): False, (20, 4): False, (20, 5): False, (20, 6): False, (20, 7): False,
             (20, 8): False, (20, 9): False, (20, 10): False, (20, 11): False, (20, 12): False, (20, 13): False,
             (20, 14): False, (20, 15): False, (20, 16): False, (20, 17): False, (20, 18): False, (20, 19): False,
             (20, 20): False, (20, 21): False, (20, 22): False, (20, 23): False, (20, 24): False, (21, 0): False,
             (21, 1): False, (21, 2): False, (21, 3): False, (21, 4): False, (21, 5): False, (21, 6): False,
             (21, 7): False, (21, 8): False, (21, 9): False, (21, 10): False, (21, 11): False, (21, 12): False,
             (21, 13): False, (21, 14): False, (21, 15): False, (21, 16): False, (21, 17): False, (21, 18): False,
             (21, 19): False, (21, 20): False, (21, 21): False, (21, 22): False, (21, 23): False, (21, 24): False,
             (22, 0): False, (22, 1): False, (22, 2): False, (22, 3): False, (22, 4): False, (22, 5): False,
             (22, 6): False, (22, 7): False, (22, 8): False, (22, 9): False, (22, 10): False, (22, 11): False,
             (22, 12): False, (22, 13): False, (22, 14): False, (22, 15): False, (22, 16): False, (22, 17): False,
             (22, 18): False, (22, 19): False, (22, 20): False, (22, 21): False, (22, 22): False, (22, 23): False,
             (22, 24): False, (23, 0): False, (23, 1): False, (23, 2): False, (23, 3): False, (23, 4): False,
             (23, 5): False, (23, 6): False, (23, 7): False, (23, 8): False, (23, 9): False, (23, 10): False,
             (23, 11): False, (23, 12): False, (23, 13): False, (23, 14): False, (23, 15): False, (23, 16): False,
             (23, 17): False, (23, 18): False, (23, 19): False, (23, 20): False, (23, 21): False, (23, 22): False,
             (23, 23): False, (23, 24): False, (24, 0): False, (24, 1): False, (24, 2): False, (24, 3): False,
             (24, 4): False, (24, 5): False, (24, 6): False, (24, 7): False, (24, 8): False, (24, 9): False,
             (24, 10): False, (24, 11): False, (24, 12): False, (24, 13): False, (24, 14): False, (24, 15): False,
             (24, 16): False, (24, 17): False, (24, 18): False, (24, 19): False, (24, 20): False, (24, 21): False,
             (24, 22): False, (24, 23): False, (24, 24): False}
        game.print_board(character_stats, board)
        expected = \
            f"\n+-----------------------------------------------+\n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . # . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f"+--------------------[     ]--------------------+\n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f"+--------------------[     ]--------------------+\n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f"+-----------------------------------------------+\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_healing_fountain(self, mock_stdout):
        character_stats = {'height': 25, 'width': 25}
        board = \
            {(0, 0): False, (0, 1): False, (0, 2): False, (0, 3): False, (0, 4): False, (0, 5): False, (0, 6): False,
             (0, 7): False, (0, 8): False, (0, 9): False, (0, 10): False, (0, 11): False, (0, 12): False,
             (0, 13): False, (0, 14): False, (0, 15): False, (0, 16): False, (0, 17): False, (0, 18): False,
             (0, 19): False, (0, 20): False, (0, 21): False, (0, 22): False, (0, 23): False, (0, 24): False,
             (1, 0): False, (1, 1): False, (1, 2): False, (1, 3): False, (1, 4): False, (1, 5): False, (1, 6): False,
             (1, 7): False, (1, 8): False, (1, 9): False, (1, 10): False, (1, 11): False, (1, 12): False,
             (1, 13): False, (1, 14): False, (1, 15): False, (1, 16): False, (1, 17): False, (1, 18): False,
             (1, 19): False, (1, 20): False, (1, 21): False, (1, 22): False, (1, 23): False, (1, 24): False,
             (2, 0): False, (2, 1): False, (2, 2): False, (2, 3): False, (2, 4): False, (2, 5): False, (2, 6): False,
             (2, 7): False, (2, 8): False, (2, 9): False, (2, 10): False, (2, 11): False, (2, 12): False,
             (2, 13): False, (2, 14): False, (2, 15): False, (2, 16): False, (2, 17): False, (2, 18): False,
             (2, 19): False, (2, 20): False, (2, 21): False, (2, 22): False, (2, 23): False, (2, 24): False,
             (3, 0): False, (3, 1): False, (3, 2): False, (3, 3): False, (3, 4): False, (3, 5): False, (3, 6): False,
             (3, 7): False, (3, 8): False, (3, 9): False, (3, 10): False, (3, 11): False, (3, 12): False,
             (3, 13): False, (3, 14): False, (3, 15): False, (3, 16): False, (3, 17): False, (3, 18): False,
             (3, 19): False, (3, 20): False, (3, 21): False, (3, 22): False, (3, 23): False, (3, 24): False,
             (4, 0): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): False, (4, 5): False, (4, 6): False,
             (4, 7): 'heal', (4, 8): False, (4, 9): False, (4, 10): False, (4, 11): False, (4, 12): False,
             (4, 13): False, (4, 14): False, (4, 15): False, (4, 16): False, (4, 17): False, (4, 18): False,
             (4, 19): False, (4, 20): False, (4, 21): False, (4, 22): False, (4, 23): False, (4, 24): False,
             (5, 0): False, (5, 1): False, (5, 2): False, (5, 3): False, (5, 4): False, (5, 5): False, (5, 6): False,
             (5, 7): False, (5, 8): False, (5, 9): False, (5, 10): False, (5, 11): False, (5, 12): False,
             (5, 13): False, (5, 14): False, (5, 15): False, (5, 16): False, (5, 17): False, (5, 18): False,
             (5, 19): False, (5, 20): False, (5, 21): False, (5, 22): False, (5, 23): False, (5, 24): False,
             (6, 0): False, (6, 1): False, (6, 2): False, (6, 3): False, (6, 4): False, (6, 5): 'heal', (6, 6): False,
             (6, 7): False, (6, 8): False, (6, 9): False, (6, 10): False, (6, 11): False, (6, 12): False,
             (6, 13): False, (6, 14): False, (6, 15): False, (6, 16): False, (6, 17): False, (6, 18): False,
             (6, 19): False, (6, 20): False, (6, 21): False, (6, 22): False, (6, 23): False, (6, 24): False,
             (7, 0): False, (7, 1): False, (7, 2): False, (7, 3): False, (7, 4): False, (7, 5): False, (7, 6): False,
             (7, 7): False, (7, 8): False, (7, 9): False, (7, 10): False, (7, 11): False, (7, 12): False,
             (7, 13): False, (7, 14): False, (7, 15): False, (7, 16): False, (7, 17): False, (7, 18): False,
             (7, 19): False, (7, 20): False, (7, 21): 'heal', (7, 22): False, (7, 23): False, (7, 24): False,
             (8, 0): False, (8, 1): False, (8, 2): False, (8, 3): False, (8, 4): False, (8, 5): False, (8, 6): False,
             (8, 7): False, (8, 8): False, (8, 9): False, (8, 10): 'heal', (8, 11): False, (8, 12): False,
             (8, 13): False, (8, 14): False, (8, 15): False, (8, 16): False, (8, 17): False, (8, 18): False,
             (8, 19): False, (8, 20): False, (8, 21): False, (8, 22): False, (8, 23): False, (8, 24): False,
             (9, 0): False, (9, 1): False, (9, 2): False, (9, 3): False, (9, 4): False, (9, 5): False, (9, 6): False,
             (9, 7): False, (9, 8): False, (9, 9): False, (9, 10): False, (9, 11): False, (9, 12): False,
             (9, 13): False, (9, 14): False, (9, 15): False, (9, 16): False, (9, 17): False, (9, 18): 'heal',
             (9, 19): False, (9, 20): False, (9, 21): False, (9, 22): False, (9, 23): False, (9, 24): False,
             (10, 0): False, (10, 1): False, (10, 2): False, (10, 3): False, (10, 4): False, (10, 5): False,
             (10, 6): False, (10, 7): False, (10, 8): False, (10, 9): False, (10, 10): False, (10, 11): False,
             (10, 12): False, (10, 13): False, (10, 14): False, (10, 15): False, (10, 16): False, (10, 17): False,
             (10, 18): False, (10, 19): False, (10, 20): False, (10, 21): False, (10, 22): False, (10, 23): False,
             (10, 24): False, (11, 0): False, (11, 1): False, (11, 2): False, (11, 3): False, (11, 4): False,
             (11, 5): False, (11, 6): False, (11, 7): False, (11, 8): False, (11, 9): False, (11, 10): False,
             (11, 11): False, (11, 12): False, (11, 13): False, (11, 14): False, (11, 15): False, (11, 16): False,
             (11, 17): 'heal', (11, 18): False, (11, 19): False, (11, 20): False, (11, 21): False, (11, 22): False,
             (11, 23): False, (11, 24): False, (12, 0): False, (12, 1): False, (12, 2): False, (12, 3): False,
             (12, 4): False, (12, 5): False, (12, 6): False, (12, 7): False, (12, 8): False, (12, 9): False,
             (12, 10): False, (12, 11): False, (12, 12): False, (12, 13): False, (12, 14): False, (12, 15): False,
             (12, 16): False, (12, 17): False, (12, 18): False, (12, 19): False, (12, 20): False, (12, 21): False,
             (12, 22): False, (12, 23): False, (12, 24): False, (13, 0): False, (13, 1): 'heal', (13, 2): False,
             (13, 3): False, (13, 4): False, (13, 5): False, (13, 6): False, (13, 7): False, (13, 8): False,
             (13, 9): False, (13, 10): False, (13, 11): False, (13, 12): False, (13, 13): False, (13, 14): False,
             (13, 15): False, (13, 16): False, (13, 17): False, (13, 18): False, (13, 19): False, (13, 20): False,
             (13, 21): False, (13, 22): False, (13, 23): False, (13, 24): False, (14, 0): False, (14, 1): False,
             (14, 2): False, (14, 3): False, (14, 4): False, (14, 5): False, (14, 6): False, (14, 7): False,
             (14, 8): False, (14, 9): False, (14, 10): False, (14, 11): False, (14, 12): False, (14, 13): False,
             (14, 14): False, (14, 15): False, (14, 16): False, (14, 17): False, (14, 18): False, (14, 19): False,
             (14, 20): False, (14, 21): False, (14, 22): False, (14, 23): False, (14, 24): False, (15, 0): False,
             (15, 1): False, (15, 2): False, (15, 3): False, (15, 4): False, (15, 5): False, (15, 6): False,
             (15, 7): False, (15, 8): False, (15, 9): False, (15, 10): False, (15, 11): False, (15, 12): False,
             (15, 13): False, (15, 14): False, (15, 15): False, (15, 16): False, (15, 17): False, (15, 18): False,
             (15, 19): False, (15, 20): False, (15, 21): False, (15, 22): False, (15, 23): False, (15, 24): False,
             (16, 0): False, (16, 1): False, (16, 2): False, (16, 3): False, (16, 4): False, (16, 5): False,
             (16, 6): False, (16, 7): False, (16, 8): False, (16, 9): False, (16, 10): False, (16, 11): False,
             (16, 12): False, (16, 13): False, (16, 14): False, (16, 15): False, (16, 16): False, (16, 17): False,
             (16, 18): False, (16, 19): False, (16, 20): False, (16, 21): False, (16, 22): False, (16, 23): False,
             (16, 24): False, (17, 0): False, (17, 1): False, (17, 2): False, (17, 3): False, (17, 4): False,
             (17, 5): False, (17, 6): False, (17, 7): False, (17, 8): False, (17, 9): False, (17, 10): False,
             (17, 11): False, (17, 12): False, (17, 13): False, (17, 14): False, (17, 15): False, (17, 16): False,
             (17, 17): False, (17, 18): False, (17, 19): False, (17, 20): False, (17, 21): False, (17, 22): False,
             (17, 23): False, (17, 24): False, (18, 0): False, (18, 1): False, (18, 2): False, (18, 3): False,
             (18, 4): False, (18, 5): False, (18, 6): False, (18, 7): False, (18, 8): False, (18, 9): False,
             (18, 10): False, (18, 11): 'heal', (18, 12): False, (18, 13): False, (18, 14): False, (18, 15): False,
             (18, 16): False, (18, 17): False, (18, 18): False, (18, 19): False, (18, 20): False, (18, 21): False,
             (18, 22): False, (18, 23): False, (18, 24): False, (19, 0): False, (19, 1): False, (19, 2): False,
             (19, 3): False, (19, 4): False, (19, 5): False, (19, 6): False, (19, 7): False, (19, 8): False,
             (19, 9): False, (19, 10): False, (19, 11): False, (19, 12): False, (19, 13): False, (19, 14): False,
             (19, 15): False, (19, 16): False, (19, 17): False, (19, 18): False, (19, 19): False, (19, 20): False,
             (19, 21): False, (19, 22): False, (19, 23): False, (19, 24): False, (20, 0): False, (20, 1): False,
             (20, 2): False, (20, 3): False, (20, 4): False, (20, 5): False, (20, 6): False, (20, 7): False,
             (20, 8): False, (20, 9): False, (20, 10): False, (20, 11): False, (20, 12): False, (20, 13): False,
             (20, 14): False, (20, 15): False, (20, 16): False, (20, 17): False, (20, 18): False, (20, 19): False,
             (20, 20): False, (20, 21): False, (20, 22): False, (20, 23): False, (20, 24): False, (21, 0): False,
             (21, 1): False, (21, 2): False, (21, 3): False, (21, 4): False, (21, 5): False, (21, 6): False,
             (21, 7): False, (21, 8): False, (21, 9): False, (21, 10): False, (21, 11): False, (21, 12): False,
             (21, 13): False, (21, 14): False, (21, 15): False, (21, 16): False, (21, 17): False, (21, 18): False,
             (21, 19): False, (21, 20): False, (21, 21): False, (21, 22): False, (21, 23): False, (21, 24): False,
             (22, 0): False, (22, 1): False, (22, 2): False, (22, 3): False, (22, 4): False, (22, 5): False,
             (22, 6): False, (22, 7): False, (22, 8): False, (22, 9): False, (22, 10): False, (22, 11): False,
             (22, 12): False, (22, 13): False, (22, 14): False, (22, 15): False, (22, 16): False, (22, 17): False,
             (22, 18): False, (22, 19): False, (22, 20): False, (22, 21): False, (22, 22): False, (22, 23): False,
             (22, 24): False, (23, 0): False, (23, 1): False, (23, 2): False, (23, 3): False, (23, 4): False,
             (23, 5): False, (23, 6): False, (23, 7): False, (23, 8): False, (23, 9): False, (23, 10): False,
             (23, 11): False, (23, 12): False, (23, 13): False, (23, 14): False, (23, 15): False, (23, 16): False,
             (23, 17): False, (23, 18): False, (23, 19): False, (23, 20): False, (23, 21): False, (23, 22): False,
             (23, 23): False, (23, 24): False, (24, 0): False, (24, 1): False, (24, 2): False, (24, 3): False,
             (24, 4): False, (24, 5): False, (24, 6): False, (24, 7): False, (24, 8): False, (24, 9): False,
             (24, 10): False, (24, 11): False, (24, 12): False, (24, 13): False, (24, 14): False, (24, 15): False,
             (24, 16): False, (24, 17): False, (24, 18): False, (24, 19): False, (24, 20): False, (24, 21): False,
             (24, 22): False, (24, 23): False, (24, 24): False}
        game.print_board(character_stats, board)
        expected = \
            f"\n+-----------------------------------------------+\n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . @ . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . @ . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . @ . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f"+--------------------[     ]--------------------+\n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . @ . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . @ . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f"+--------------------[     ]--------------------+\n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . @ . . . . . . . . . . . . . \n" \
            f". . . . . . . . . @ . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . @ . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f"+-----------------------------------------------+\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_location(self, mock_stdout):
        character_stats = {'height': 25, 'width': 25}
        board = \
            {(0, 0): False, (0, 1): False, (0, 2): False, (0, 3): False, (0, 4): False, (0, 5): False,(0, 6): False,
             (0, 7): False, (0, 8): False, (0, 9): False, (0, 10): False, (0, 11): False, (0, 12): False,
             (0, 13): False, (0, 14): False, (0, 15): False, (0, 16): False, (0, 17): False, (0, 18): False,
             (0, 19): False, (0, 20): False, (0, 21): False, (0, 22): False, (0, 23): False, (0, 24): False,
             (1, 0): False, (1, 1): False, (1, 2): False, (1, 3): False, (1, 4): False, (1, 5): False,(1, 6): False,
             (1, 7): False, (1, 8): False, (1, 9): False, (1, 10): False, (1, 11): False, (1, 12): False,
             (1, 13): False, (1, 14): False, (1, 15): False, (1, 16): False, (1, 17): False, (1, 18): False,
             (1, 19): False, (1, 20): False, (1, 21): False, (1, 22): False, (1, 23): False, (1, 24): False,
             (2, 0): False, (2, 1): False, (2, 2): False, (2, 3): False, (2, 4): False, (2, 5): False,(2, 6): False,
             (2, 7): False, (2, 8): False, (2, 9): False, (2, 10): False, (2, 11): False, (2, 12): False,
             (2, 13): False, (2, 14): False, (2, 15): False, (2, 16): False, (2, 17): False, (2, 18): False,
             (2, 19): False, (2, 20): False, (2, 21): False, (2, 22): False, (2, 23): False, (2, 24): False,
             (3, 0): False, (3, 1): False, (3, 2): False, (3, 3): False, (3, 4): False, (3, 5): False,(3, 6): False,
             (3, 7): False, (3, 8): False, (3, 9): False, (3, 10): False, (3, 11): False, (3, 12): False,
             (3, 13): False, (3, 14): False, (3, 15): False, (3, 16): False, (3, 17): False, (3, 18): False,
             (3, 19): False, (3, 20): False, (3, 21): False, (3, 22): False, (3, 23): False, (3, 24): False,
             (4, 0): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): False, (4, 5): False,(4, 6): False,
             (4, 7): False, (4, 8): False, (4, 9): False, (4, 10): False, (4, 11): False, (4, 12): False,
             (4, 13): False, (4, 14): False, (4, 15): False, (4, 16): False, (4, 17): False, (4, 18): False,
             (4, 19): False, (4, 20): False, (4, 21): False, (4, 22): False, (4, 23): False, (4, 24): False,
             (5, 0): False, (5, 1): False, (5, 2): False, (5, 3): False, (5, 4): False, (5, 5): False, (5, 6): False,
             (5, 7): False, (5, 8): False, (5, 9): False, (5, 10): False, (5, 11): False, (5, 12): False,
             (5, 13): False, (5, 14): False, (5, 15): False, (5, 16): False, (5, 17): False, (5, 18): False,
             (5, 19): False, (5, 20): False, (5, 21): False, (5, 22): False, (5, 23): False, (5, 24): False,
             (6, 0): False, (6, 1): False, (6, 2): False, (6, 3): False, (6, 4): False, (6, 5): False, (6, 6): False,
             (6, 7): False, (6, 8): False, (6, 9): False, (6, 10): False, (6, 11): False, (6, 12): False,
             (6, 13): False, (6, 14): False, (6, 15): False, (6, 16): False, (6, 17): False, (6, 18): False,
             (6, 19): False, (6, 20): False, (6, 21): False, (6, 22): False, (6, 23): False, (6, 24): False,
             (7, 0): False, (7, 1): False, (7, 2): False, (7, 3): False, (7, 4): False, (7, 5): False, (7, 6): False,
             (7, 7): False, (7, 8): False, (7, 9): False, (7, 10): False, (7, 11): False, (7, 12): False,
             (7, 13): False, (7, 14): False, (7, 15): False, (7, 16): False, (7, 17): False, (7, 18): False,
             (7, 19): False, (7, 20): False, (7, 21): False, (7, 22): False, (7, 23): False, (7, 24): False,
             (8, 0): False, (8, 1): False, (8, 2): False, (8, 3): False, (8, 4): False, (8, 5): False, (8, 6): False,
             (8, 7): False, (8, 8): False, (8, 9): False, (8, 10): False, (8, 11): False, (8, 12): False,
             (8, 13): False, (8, 14): False, (8, 15): False, (8, 16): False, (8, 17): False, (8, 18): False,
             (8, 19): False, (8, 20): False, (8, 21): False, (8, 22): False, (8, 23): False, (8, 24): False,
             (9, 0): False, (9, 1): False, (9, 2): False, (9, 3): False, (9, 4): False, (9, 5): False, (9, 6): False,
             (9, 7): False, (9, 8): False, (9, 9): False, (9, 10): False, (9, 11): False, (9, 12): False,
             (9, 13): False, (9, 14): False, (9, 15): False, (9, 16): False, (9, 17): False, (9, 18): False,
             (9, 19): False, (9, 20): False, (9, 21): False, (9, 22): False, (9, 23): False, (9, 24): False,
             (10, 0): False, (10, 1): False, (10, 2): False, (10, 3): False, (10, 4): False, (10, 5): False,
             (10, 6): False, (10, 7): False, (10, 8): False, (10, 9): False, (10, 10): False, (10, 11): False,
             (10, 12): False, (10, 13): False, (10, 14): False, (10, 15): False, (10, 16): False, (10, 17): False,
             (10, 18): False, (10, 19): False, (10, 20): False, (10, 21): False, (10, 22): False, (10, 23): False,
             (10, 24): False, (11, 0): False, (11, 1): False, (11, 2): False, (11, 3): False, (11, 4): False,
             (11, 5): False, (11, 6): False, (11, 7): False, (11, 8): False, (11, 9): False, (11, 10): False,
             (11, 11): False, (11, 12): False, (11, 13): False, (11, 14): False, (11, 15): False, (11, 16): False,
             (11, 17): False, (11, 18): False, (11, 19): False, (11, 20): False, (11, 21): False, (11, 22): False,
             (11, 23): False, (11, 24): False, (12, 0): False, (12, 1): False, (12, 2): False, (12, 3): False,
             (12, 4): False, (12, 5): False, (12, 6): False, (12, 7): False, (12, 8): False, (12, 9): False,
             (12, 10): False, (12, 11): False, (12, 12): False, (12, 13): False, (12, 14): False, (12, 15): False,
             (12, 16): False, (12, 17): False, (12, 18): False, (12, 19): False, (12, 20): False, (12, 21): False,
             (12, 22): False, (12, 23): False, (12, 24): 'boss', (13, 0): False, (13, 1): False, (13, 2): False,
             (13, 3): False, (13, 4): False, (13, 5): False, (13, 6): False, (13, 7): False, (13, 8): False,
             (13, 9): False, (13, 10): False, (13, 11): False, (13, 12): False, (13, 13): False, (13, 14): False,
             (13, 15): False, (13, 16): False, (13, 17): False, (13, 18): False, (13, 19): False, (13, 20): False,
             (13, 21): False, (13, 22): False, (13, 23): False, (13, 24): False, (14, 0): False, (14, 1): False,
             (14, 2): False, (14, 3): False, (14, 4): False, (14, 5): False, (14, 6): False, (14, 7): False,
             (14, 8): False, (14, 9): False, (14, 10): False, (14, 11): False, (14, 12): False, (14, 13): False,
             (14, 14): False, (14, 15): False, (14, 16): False, (14, 17): False, (14, 18): False, (14, 19): False,
             (14, 20): False, (14, 21): False, (14, 22): False, (14, 23): False, (14, 24): False, (15, 0): False,
             (15, 1): False, (15, 2): False, (15, 3): False, (15, 4): False, (15, 5): False, (15, 6): False,
             (15, 7): False, (15, 8): False, (15, 9): False, (15, 10): False, (15, 11): False, (15, 12): False,
             (15, 13): False, (15, 14): False, (15, 15): False, (15, 16): False, (15, 17): False, (15, 18): False,
             (15, 19): False, (15, 20): False, (15, 21): False, (15, 22): False, (15, 23): False, (15, 24): False,
             (16, 0): False, (16, 1): False, (16, 2): False, (16, 3): False, (16, 4): False, (16, 5): False,
             (16, 6): False, (16, 7): False, (16, 8): False, (16, 9): False, (16, 10): False, (16, 11): False,
             (16, 12): False, (16, 13): False, (16, 14): False, (16, 15): False, (16, 16): False, (16, 17): False,
             (16, 18): False, (16, 19): False, (16, 20): False, (16, 21): False, (16, 22): False, (16, 23): False,
             (16, 24): False, (17, 0): False, (17, 1): False, (17, 2): False, (17, 3): False, (17, 4): False,
             (17, 5): False, (17, 6): False, (17, 7): False, (17, 8): False, (17, 9): False, (17, 10): False,
             (17, 11): False, (17, 12): False, (17, 13): False, (17, 14): False, (17, 15): False, (17, 16): False,
             (17, 17): False, (17, 18): False, (17, 19): False, (17, 20): False, (17, 21): False, (17, 22): False,
             (17, 23): False, (17, 24): False, (18, 0): False, (18, 1): False, (18, 2): False, (18, 3): False,
             (18, 4): False, (18, 5): False, (18, 6): False, (18, 7): False, (18, 8): False, (18, 9): False,
             (18, 10): False, (18, 11): False, (18, 12): False, (18, 13): False, (18, 14): False, (18, 15): False,
             (18, 16): False, (18, 17): False, (18, 18): False, (18, 19): False, (18, 20): False, (18, 21): False,
             (18, 22): False, (18, 23): False, (18, 24): False, (19, 0): False, (19, 1): False, (19, 2): False,
             (19, 3): False, (19, 4): False, (19, 5): False, (19, 6): False, (19, 7): False, (19, 8): False,
             (19, 9): False, (19, 10): False, (19, 11): False, (19, 12): False, (19, 13): False, (19, 14): False,
             (19, 15): False, (19, 16): False, (19, 17): False, (19, 18): False, (19, 19): False, (19, 20): False,
             (19, 21): False, (19, 22): False, (19, 23): False, (19, 24): False, (20, 0): False, (20, 1): False,
             (20, 2): False, (20, 3): False, (20, 4): False, (20, 5): False, (20, 6): False, (20, 7): False,
             (20, 8): False, (20, 9): False, (20, 10): False, (20, 11): False, (20, 12): False, (20, 13): False,
             (20, 14): False, (20, 15): False, (20, 16): False, (20, 17): False, (20, 18): False, (20, 19): False,
             (20, 20): False, (20, 21): False, (20, 22): False, (20, 23): False, (20, 24): False, (21, 0): False,
             (21, 1): False, (21, 2): False, (21, 3): False, (21, 4): False, (21, 5): False, (21, 6): False,
             (21, 7): False, (21, 8): False, (21, 9): False, (21, 10): False, (21, 11): False, (21, 12): False,
             (21, 13): False, (21, 14): False, (21, 15): False, (21, 16): False, (21, 17): False, (21, 18): False,
             (21, 19): False, (21, 20): False, (21, 21): False, (21, 22): False, (21, 23): False, (21, 24): False,
             (22, 0): False, (22, 1): False, (22, 2): False, (22, 3): False, (22, 4): False, (22, 5): False,
             (22, 6): False, (22, 7): False, (22, 8): False, (22, 9): False, (22, 10): False, (22, 11): False,
             (22, 12): False, (22, 13): False, (22, 14): False, (22, 15): False, (22, 16): False, (22, 17): False,
             (22, 18): False, (22, 19): False, (22, 20): False, (22, 21): False, (22, 22): False, (22, 23): False,
             (22, 24): False, (23, 0): False, (23, 1): False, (23, 2): False, (23, 3): False, (23, 4): False,
             (23, 5): False, (23, 6): False, (23, 7): False, (23, 8): False, (23, 9): False, (23, 10): False,
             (23, 11): False, (23, 12): False, (23, 13): False, (23, 14): False, (23, 15): False, (23, 16): False,
             (23, 17): False, (23, 18): False, (23, 19): False, (23, 20): False, (23, 21): False, (23, 22): False,
             (23, 23): False, (23, 24): False, (24, 0): False, (24, 1): False, (24, 2): False, (24, 3): False,
             (24, 4): False, (24, 5): False, (24, 6): False, (24, 7): False, (24, 8): False, (24, 9): False,
             (24, 10): False, (24, 11): False, (24, 12): False, (24, 13): False, (24, 14): False, (24, 15): False,
             (24, 16): False, (24, 17): False, (24, 18): False, (24, 19): False, (24, 20): False, (24, 21): False,
             (24, 22): False, (24, 23): False, (24, 24): False}
        game.print_board(character_stats, board)
        expected = \
            f"\n+-----------------------------------------------+\n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f"+--------------------[     ]--------------------+\n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f"+--------------------[     ]--------------------+\n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . $ . . . . . . . . . . . . \n" \
            f"+-----------------------------------------------+\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_regular_board(self, mock_stdout):
        character_stats = {'name': '', 'x_coordinate': 0, 'y_coordinate': 0, 'current_location': (0, 0),
                           'healing_landmarks': [(11, 17), (4, 7), (18, 11), (13, 1), (7, 21), (6, 5), (9, 18),
                                                 (8, 10)], 'height': 25, 'width': 25}
        board = game.make_board(character_stats)
        game.print_board(character_stats, board)
        expected = \
            f"\n+-----------------------------------------------+\n" \
            f"# . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . @ . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . @ . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . @ . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f"+--------------------[     ]--------------------+\n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . @ . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . @ . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f"+--------------------[     ]--------------------+\n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . @ . . . . . . . . . . . . . \n" \
            f". . . . . . . . . @ . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . @ . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . . . . . . . . . . . . . . \n" \
            f". . . . . . . . . . . . $ . . . . . . . . . . . . \n" \
            f"+-----------------------------------------------+\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
