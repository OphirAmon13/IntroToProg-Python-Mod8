# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: This file tests the data_classes.py file
# Change Log: Ophir Amon, 3/11/2024
# ------------------------------------------------------------------------------------------ #

# Import necessary functions
import unittest
from data_classes import Person, Employee

# Testing the Person class
class TestPerson(unittest.TestCase):

    # Tests initialization of a Person
    def test_person_init(self):
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    # Tests Person.first_name
    def test_person_first_name(self):
        person = Person("Jane", "Doe")
        self.assertEqual(person.first_name, "Jane")

    # Tests if exception is thrown with invalid first name
    def test_person_invalid_first_name(self):
        with self.assertRaises(ValueError):
            Person("123", "Doe")

    # Tests Person.last_name
    def test_person_last_name(self):
        person = Person("Jane", "Doe")
        self.assertEqual(person.last_name, "Doe")

    # Tests if exception is thrown with invalid first name
    def test_person_invalid_last_name(self):
        with self.assertRaises(ValueError):
            Person("John", "123")

# Testing the Employee class
class TestEmployee(unittest.TestCase):

    # Tests initialization of a Employee
    def test_employee_init(self):
        employee = Employee("Jane", "Doe", "2023-03-11", 5)
        self.assertEqual(employee.first_name, "Jane")
        self.assertEqual(employee.last_name, "Doe")
        self.assertEqual(employee.review_date, "2023-03-11")
        self.assertEqual(employee.review_rating, 5)

    # Tests Employee.first_name
    def test_employee_first_name(self):
        employee = Employee("Jane", "Doe")
        self.assertEqual(employee.first_name, "Jane")

    # Tests if exception is thrown with invalid first name   
    def test_employee_invalid_first_name(self):
        with self.assertRaises(ValueError):
            Employee("123", "Doe")

    # Tests Employee.first_name
    def test_employee_last_name(self):
        employee = Employee("Jane", "Doe")
        self.assertEqual(employee.last_name, "Doe")

    # Tests if exception is thrown with invalid last name
    def test_employee_invalid_last_name(self):
        with self.assertRaises(ValueError):
            Employee("Jane", "123")

    # Tests Employee.review_date
    def test_employee_review_date(self):
        employee = Employee("Jane", "Doe", "2023-03-11", 5)
        self.assertEqual(employee.review_date, "2023-03-11")

    # Tests if exceptions are thrown with invalid review dates    
    def test_employee_invalid_review_date(self):
        with self.assertRaises(Exception):
            Employee("Jane", "Doe", "20-03-11", 5)
        with self.assertRaises(ValueError):
            Employee("Jane", "Doe", "2023-02-29", 5)

    # Tests Employee.review_rating
    def test_employee_review_rating(self):
        employee1 = Employee("Jane", "Doe", "2023-03-11", 1)
        self.assertEqual(employee1.review_rating, 1)
        employee2 = Employee("Jane", "Doe", "2023-03-11", 2)
        self.assertEqual(employee2.review_rating, 2)
        employee3 = Employee("Jane", "Doe", "2023-03-11", 3)
        self.assertEqual(employee3.review_rating, 3)
        employee4 = Employee("Jane", "Doe", "2023-03-11", 4)
        self.assertEqual(employee4.review_rating, 4)
        employee5 = Employee("Jane", "Doe", "2023-03-11", 5)
        self.assertEqual(employee5.review_rating, 5)
        employee6 = Employee("Jane", "Doe", "2023-03-11", "1")
        self.assertEqual(employee6.review_rating, 1)
        employee7 = Employee("Jane", "Doe", "2023-03-11", "3")
        self.assertEqual(employee7.review_rating, 3)

    # Tests if exceptions are thrown with invalid review ratings 
    def test_employee_invalid_review_rating(self):
        with self.assertRaises(Exception):
            Employee("Jane", "Doe", "2023-03-11", -1)
        with self.assertRaises(Exception):
            Employee("Jane", "Doe", "2023-03-11", 0)
        with self.assertRaises(Exception):
            Employee("Jane", "Doe", "2023-03-11", 6)
        with self.assertRaises(Exception):
            Employee("Jane", "Doe", "2023-03-11", "-1")
        with self.assertRaises(Exception):
            Employee("Jane", "Doe", "2023-03-11", "0")
        with self.assertRaises(Exception):
            Employee("Jane", "Doe", "2023-03-11", "6")
        with self.assertRaises(ValueError):
            Employee("Jane", "Doe", "2023-03-11", "five")
        with self.assertRaises(ValueError):
            Employee("Jane", "Doe", "2023-03-11", "")



