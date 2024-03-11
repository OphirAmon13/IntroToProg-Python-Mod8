# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: This file tests the presentation_classes.py file
# Change Log: Ophir Amon, 3/11/2024
# ------------------------------------------------------------------------------------------ #

# Import necessary functions
import unittest
from unittest.mock import patch
from presentation_classes import IO

# Tests the IO class
class TestIO(unittest.TestCase):

    # Initializing data
    def setUp(self):
        self.employee_data = []
    
    def tearDown(self):
        pass

    # Tests if input_employee_data works properly
    def test_input_employee_data(self):
        with patch("builtins.input", side_effect=("John", "Doe", "2024-03-11", 3)):
            IO.input_employee_data(self.employee_data)
            self.assertEqual(self.employee_data[0].first_name, "John")
            self.assertEqual(self.employee_data[0].last_name, "Doe")
            self.assertEqual(self.employee_data[0].review_date, "2024-03-11")
            self.assertEqual(self.employee_data[0].review_rating, 3)
            length_of_employee_list = len(self.employee_data)
            self.assertEqual(length_of_employee_list, 1)

    # Tests if function will add data given invalid first name
    def test_input_data_invalid_first_name(self):
        with patch("builtins.input", side_effect=("123", "Doe", "2024-03-11", 3)):
            IO.input_employee_data(self.employee_data)
            self.assertEqual(len(self.employee_data), 0)

    # Tests if function will add data given invalid last name
    def test_input_data_invalid_last_name(self):
        with patch("builtins.input", side_effect=("John", "123", "2024-03-11", 3)):
            IO.input_employee_data(self.employee_data)
            self.assertEqual(len(self.employee_data), 0)

    # Tests if function will add data given invalid review date
    def test_input_data_invalid_review_date(self):
        with patch("builtins.input", side_effect=("John", "Doe", "20-03-11", 3)):
            IO.input_employee_data(self.employee_data)
            self.assertEqual(len(self.employee_data), 0)

    # Tests if function will add data given invalid review rating
    def test_input_data_invalid_review_rating(self):
        with patch("builtins.input", side_effect=("John", "Doe", "2024-03-11", "three")):
            IO.input_employee_data(self.employee_data)
            self.assertEqual(len(self.employee_data), 0)


