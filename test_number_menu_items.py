"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 28, 2021
"""

from unittest import TestCase
import game


class Test(TestCase):

    def test_return_list(self):
        menu_items = ["Quit", "North", "South", "East", "West"]
        numbered_menu = game.number_menu_items(menu_items)
        self.assertIsInstance(numbered_menu, list)

    def test_menu_items_are_tuples(self):
        menu_items = ["Yes", "No"]
        numbered_menu = game.number_menu_items(menu_items)
        menu_items_yes, menu_items_no = numbered_menu
        self.assertTrue(type(menu_items_yes) is tuple and type(menu_items_no) is tuple)

    def test_starting_index_is_zero(self):
        menu_items = ["Yes", "No"]
        numbered_menu = game.number_menu_items(menu_items)
        first_menu_items, second_menu_items = numbered_menu
        first_index, first_item = first_menu_items
        self.assertEqual(first_index, 0)

    def test_ending_index_is_correct(self):
        menu_items = ["Yes", "No"]
        numbered_menu = game.number_menu_items(menu_items)
        first_menu_items, second_menu_items = numbered_menu
        second_index, second_item = second_menu_items
        self.assertEqual(second_index, 1)

    def test_menu_item_is_correct(self):
        menu_items = ["Yes", "No"]
        numbered_menu = game.number_menu_items(menu_items)
        first_menu_items, second_menu_items = numbered_menu
        second_index, second_item = second_menu_items
        self.assertEqual(second_item, "No")
