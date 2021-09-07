"""
Name: Kelly Olsson & Hannah Kuo
Student number: A01030513 & A01068509
Date: March 27, 2021
"""

from unittest import TestCase
import game


class TestHealingLandmarks(TestCase):

    def test_correct_list_length(self):
        character_stats = {}
        game.healing_landmarks(character_stats)
        actual = character_stats["healing_landmarks"]
        self.assertEqual(len(actual), 8)

    def test_correct_value_range(self):
        character_stats = {}
        game.healing_landmarks(character_stats)
        healing_landmarks_list = character_stats["healing_landmarks"]
        first_tuple, second_tuple, third_tuple, fourth_tuple, fifth_tuple, sixth_tuple, seventh_tuple, eighth_tuple \
            = healing_landmarks_list
        x_coordinate_in_first_tuple, y_coordinate_in_first_tuple = first_tuple
        x_coordinate_in_second_tuple, y_coordinate_in_second_tuple = second_tuple
        x_coordinate_in_third_tuple, y_coordinate_in_third_tuple = third_tuple
        x_coordinate_in_fourth_tuple, y_coordinate_in_fourth_tuple = fourth_tuple
        x_coordinate_in_fifth_tuple, y_coordinate_in_fifth_tuple = fifth_tuple
        x_coordinate_in_sixth_tuple, y_coordinate_in_sixth_tuple = sixth_tuple
        x_coordinate_in_seventh_tuple, y_coordinate_in_seventh_tuple = seventh_tuple
        x_coordinate_in_eighth_tuple, y_coordinate_in_eighth_tuple = eighth_tuple
        all_values_list = [x_coordinate_in_first_tuple, y_coordinate_in_first_tuple,
                           x_coordinate_in_second_tuple, y_coordinate_in_second_tuple,
                           x_coordinate_in_third_tuple, y_coordinate_in_third_tuple,
                           x_coordinate_in_fourth_tuple, y_coordinate_in_fourth_tuple,
                           x_coordinate_in_fifth_tuple, y_coordinate_in_fifth_tuple,
                           x_coordinate_in_sixth_tuple, y_coordinate_in_sixth_tuple,
                           x_coordinate_in_seventh_tuple, y_coordinate_in_seventh_tuple,
                           x_coordinate_in_eighth_tuple, y_coordinate_in_eighth_tuple]
        for values in all_values_list:
            self.assertTrue(1 <= values <= 23)

    def test_unique_values(self):
        user_stats = {"player_hp": 30}
        game.healing_landmarks(user_stats)
        healing_landmarks_list = user_stats["healing_landmarks"]
        first_tuple, second_tuple, third_tuple, fourth_tuple, fifth_tuple, sixth_tuple, seventh_tuple, eighth_tuple \
            = healing_landmarks_list
        x_coordinate_in_first_tuple, y_coordinate_in_first_tuple = first_tuple
        x_coordinate_in_second_tuple, y_coordinate_in_second_tuple = second_tuple
        x_coordinate_in_third_tuple, y_coordinate_in_third_tuple = third_tuple
        x_coordinate_in_fourth_tuple, y_coordinate_in_fourth_tuple = fourth_tuple
        x_coordinate_in_fifth_tuple, y_coordinate_in_fifth_tuple = fifth_tuple
        x_coordinate_in_sixth_tuple, y_coordinate_in_sixth_tuple = sixth_tuple
        x_coordinate_in_seventh_tuple, y_coordinate_in_seventh_tuple = seventh_tuple
        x_coordinate_in_eighth_tuple, y_coordinate_in_eighth_tuple = eighth_tuple
        x_coordinate_number_list = [x_coordinate_in_first_tuple, x_coordinate_in_second_tuple,
                                    x_coordinate_in_third_tuple, x_coordinate_in_fourth_tuple,
                                    x_coordinate_in_fifth_tuple, x_coordinate_in_sixth_tuple,
                                    x_coordinate_in_seventh_tuple, x_coordinate_in_eighth_tuple]
        y_coordinate_number_list = [y_coordinate_in_first_tuple, y_coordinate_in_second_tuple,
                                    y_coordinate_in_third_tuple, y_coordinate_in_fourth_tuple,
                                    y_coordinate_in_fifth_tuple, y_coordinate_in_sixth_tuple,
                                    y_coordinate_in_seventh_tuple, y_coordinate_in_eighth_tuple]
        for x_coordinate_values in x_coordinate_number_list:
            for y_coordinate_values in y_coordinate_number_list:
                self.assertTrue(x_coordinate_number_list.count(x_coordinate_values) == 1 and
                                y_coordinate_number_list.count(y_coordinate_values) == 1)

    def test_healing_landmarks_is_list(self):
        character_stats = {}
        game.healing_landmarks(character_stats)
        healing_landmarks_list = character_stats["healing_landmarks"]
        self.assertTrue(type(healing_landmarks_list) is list)

    def test_tuples_in_list(self):
        player_stats = {}
        game.healing_landmarks(player_stats)
        healing_landmarks_list = player_stats["healing_landmarks"]
        first_tuple, second_tuple, third_tuple, fourth_tuple, fifth_tuple, sixth_tuple, seventh_tuple, eighth_tuple \
            = healing_landmarks_list
        self.assertTrue(type(first_tuple) is tuple and type(second_tuple) is tuple and type(third_tuple) is tuple and
                        type(fourth_tuple) is tuple and type(fifth_tuple) is tuple and type(sixth_tuple) is tuple and
                        type(seventh_tuple) is tuple and type(eighth_tuple) is tuple)
