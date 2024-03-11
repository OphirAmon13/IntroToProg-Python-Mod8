# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: This file runs all the code 
# from other files in the folder
# Change Log: Ophir Amon, 3/11/2024
# ------------------------------------------------------------------------------------------ #

# Import necessary functions
import processing_classes
import presentation_classes
from data_classes import Employee


# Define the Data Variables and constants

FILE_NAME: str = "EmployeeRatings.json"
MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Enter new employee rating data.
    2. Show current employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''
employees: list = []  # a table of employees data
menu_choice = ""

if __name__ == "__main__":

    Employee("aasd", "Adsfa", "2020-01-02", -1)    

    # Reads any data from file
    processing_classes.FileProcessor.read_data_from_file(FILE_NAME, employees)


    while True:
        # Present the menu of choices
        presentation_classes.IO.output_menu(MENU)
        menu_choice = presentation_classes.IO.input_menu_choice()
           
        # Checks the user's menu choice against different cases           
        match menu_choice:
            case "1":
                # Allows user to add employee data
                presentation_classes.IO.input_employee_data(employees)  
            case "2":
                # Prints the current data
                presentation_classes.IO.output_employee_data(employees)
            case "3":
                # Adds data to file
                processing_classes.FileProcessor.write_data_to_file(FILE_NAME, employees)
            case "4":
                # Exits program
                presentation_classes.IO.quit_program()
            case _:
                # Handles all other inputs
                print("ERROR: Please select a valid option")
