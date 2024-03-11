# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: This file contains all functions 
# that deal with external files
# Change Log: Ophir Amon, 3/11/2024
# ------------------------------------------------------------------------------------------ #

# Import necessary functions
import json
from json.decoder import JSONDecodeError
import data_classes
import presentation_classes

class FileProcessor: # Stores all functions that have to do with .json files
    
    # Function that reads and prints the data from a file
    @staticmethod
    def read_data_from_file(file_name: str, employee_data: list):
        print(file_name)
        try:
            with open(file_name, "r") as file:
                print("First Name \tLast Name \tReview Date \tReview Rating")
                loaded_employee_table = json.load(file)
                for item in loaded_employee_table:
                        new_employee = data_classes.Employee(item["first_name"], item["last_name"], item["review_date"], item["review_rating"])
                        employee_data.append(new_employee)
                        print(f"{new_employee.first_name} \t\t{new_employee.last_name} \t\t{new_employee.review_date} \t\t{new_employee.review_rating}")
        except FileNotFoundError as error_message:
            presentation_classes.IO.output_error_messages(f"There was an error finding the {file_name} file!", error_message)
        except JSONDecodeError as error_message:
            presentation_classes.IO.output_error_messages(f"There was an error reading the data from the {file_name} file!", error_message)
        except Exception as error_message:
            presentation_classes.IO.output_error_messages(f"There was an error reading the data from the {file_name} file!", error_message)
    
    # Function that saves data to a file
    @staticmethod
    def write_data_to_file(file_name: str, employee_data: list): # Saves all information to JSON file
        try:
            list_of_employees: list = []
            for employee in employee_data:
                employee_dict: dict = {
                    "first_name": employee.first_name,
                    "last_name": employee.last_name,
                    "review_date": employee.review_date,
                    "review_rating": employee.review_rating
                    }
                list_of_employees.append(employee_dict)

            with open(file_name, "w") as file:
                json.dump(list_of_employees, file)
                for employee in list_of_employees:
                    print(f"You have reviewed the employee, {employee['first_name']} {employee['last_name']}, on {employee['review_date']}, with a rating of {employee['review_rating']}.")
        except Exception as error_message:
            presentation_classes.IO.output_error_messages(f"There was an error saving the data to the {file_name} file!", error_message)