# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: This file tests the processing_classes.py file
# Change Log: Ophir Amon, 3/11/2024
# ------------------------------------------------------------------------------------------ #

# Import necessary functions
from unittest import TestCase
import tempfile
import json
import data_classes as data
from processing_classes import FileProcessor

# Tests the FileProcessor class
class TestFileProcessor(TestCase):

    # Creates temporary file
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def tearDown(self):
            self.temp_file.close()

    # Tests if read_data_from_file works properly
    def test_read_data_from_file(self):
        sample_data = [
            {"first_name": "John", "last_name": "Doe", "review_date": "2024-03-11", "review_rating": 3},
            {"first_name": "Alice", "last_name": "Smith", "review_date": "2024-01-01", "review_rating": 4},
        ]

        # Populate the temp file
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        FileProcessor.read_data_from_file(self.temp_file_name, self.employee_data)

        # Test cases
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].first_name, "John")
        self.assertEqual(self.employee_data[0].last_name, "Doe")
        self.assertEqual(self.employee_data[0].review_date, "2024-03-11")
        self.assertEqual(self.employee_data[0].review_rating, 3)
        self.assertEqual(self.employee_data[1].first_name, "Alice")
        self.assertEqual(self.employee_data[1].last_name, "Smith")
        self.assertEqual(self.employee_data[1].review_date, "2024-01-01")
        self.assertEqual(self.employee_data[1].review_rating, 4)

    # Tests if read_data_from_file throws exception if file does not exist
    def test_read_data_from_file_invalid(self): 

        FileProcessor.read_data_from_file(file_name="fake_name.json", employee_data=self.employee_data) 
        self.assertRaises(FileNotFoundError)
        


    # Tests if write_data_to_file works properly
    def test_write_data_to_file(self):

        # Create sample data
        sample_employee = [
            data.Employee("John", "Doe", "2024-03-11", 3),
            data.Employee("Alice", "Smith", "2024-01-01", 4)
        ]

        FileProcessor.write_data_to_file(self.temp_file_name, sample_employee)

        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        # Test cases
        self.assertEqual(len(file_data), len(sample_employee))
        self.assertEqual(file_data[0]["first_name"], "John")
        self.assertEqual(file_data[0]["last_name"], "Doe")
        self.assertEqual(file_data[0]["review_date"], "2024-03-11")
        self.assertEqual(file_data[0]["review_rating"], 3)
        self.assertEqual(file_data[1]["first_name"], "Alice")
        self.assertEqual(file_data[1]["last_name"], "Smith")
        self.assertEqual(file_data[1]["review_date"], "2024-01-01")
        self.assertEqual(file_data[1]["review_rating"], 4)