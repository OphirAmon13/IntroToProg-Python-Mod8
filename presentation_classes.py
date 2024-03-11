# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: This file contains all functions
# that deals with inputs/outputs
# Change Log: Ophir Amon, 3/11/2024
# ------------------------------------------------------------------------------------------ #

# Import necessary functions
import data_classes
from datetime import datetime

class IO: # Stores all functions that have to do with inputs/outputs

    # Function to output error message whereever needed
    @staticmethod
    def output_error_messages(message: str, error: Exception = None): 
        print(message)
        print(f"Error detail: {error}")

    # Function that prints the menu options
    @staticmethod
    def output_menu(menu: str): # Prints the menu of options
        print(menu)

    # Function that stores the user's menu choice 
    @staticmethod
    def input_menu_choice():  
        return input("Please enter a menu option (1-4): ")

    # Function that allows user to add employees to the data
    @staticmethod
    def input_employee_data(employee_data: list): # Adds user to database
        try:
            employee_first_name = input("Enter the employee's first name: ")
            employee_last_name = input("Enter the employee's last name: ")
            review_date = input("Please enter the review date (YYYY-MM-DD): ")
            review_rating = input("Please enter the review rating (1-5): ")
            new_employee = data_classes.Employee(employee_first_name, employee_last_name, review_date, review_rating)
        except Exception as error_message:
            IO.output_error_messages("There was a non-specific error when adding data!", error_message)
            return
            
        employee_data.append(new_employee) # Adds employees to list of all employee data
        print(employee_data)

    # Function that prints out the current data
    @staticmethod
    def output_employee_data(employee_data: list): # Presents all information to the user
        print("First Name \tLast Name \tReview Date \tReview Rating")
        for employee in employee_data:
            print(f"{employee.first_name} \t\t{employee.last_name} \t\t{employee.review_date} \t\t{employee.review_rating}")

    # Function that ends the program
    @staticmethod
    def quit_program(): # Ends the program
        exit()