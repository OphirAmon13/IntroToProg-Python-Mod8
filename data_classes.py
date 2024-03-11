# ------------------------------------------------------------------------------------------ #
# Title: Assignment08
# Desc: This file contains all object classes
# Change Log: Ophir Amon, 3/11/2024
# ------------------------------------------------------------------------------------------ #

# Import necessary functions
import datetime

class Person: # Creates the Person object

    # Initializes the Person object
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name,self.last_name}"

    @property
    def first_name(self):
        return self.__first_name.title()
    
    @first_name.setter
    def first_name(self, value: str):
        if not value:
            raise Exception("ERROR: Employee first name cannot be empty")
        if not value.isalpha():
            raise ValueError("The first name should not contain numbers.")
        else:
            self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name.title()
    
    @last_name.setter
    def last_name(self, value: str):
        if not value:
            raise Exception("ERROR: Employee last name cannot be empty")
        if not value.isalpha():
            raise ValueError("The last name should not contain numbers.")
        else:
            self.__last_name = value

class Employee(Person): # Creates the Employee object which inherits from the Person class

    # Initializes the Employee object
    def __init__(self, first_name: str = "", last_name: str = "", review_date: datetime.date = "1900-01-01", review_rating: int = 3):
        super().__init__(first_name, last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    def __str__(self):
        return f"{self.first_name,self.last_name,self.review_date,self.review_rating}"
    
    def __repr__(self):
        return self.__str__()

    @property
    def review_date(self):
        return self.__review_date

    @review_date.setter
    def review_date(self, value):
        try:
            date_format = "%Y-%m-%d"
            bool(datetime.datetime.strptime(value, date_format))
            self.__review_date = value
        except ValueError:
            raise ValueError("Date entered was not valid, day is out of range of month")
        except:
            raise Exception("Date entered was not valid, format must be YYYY-MM-DD")

    @property
    def review_rating(self):
        return self.__review_rating
    
    @review_rating.setter
    def review_rating(self, value):
        if (type(value) is int) and (value >= 1 and value <= 5):
            self.__review_rating = value
        
        else:
            try:
                if not value.isdigit():
                    raise ValueError("Review rating must be an integer.")
                if int(value) < 1 or int(value) > 5:
                    raise Exception("Review rating must be from 1-5")
                self.__review_rating = int(value)
            except ValueError:
                raise ValueError("Error saving review rating.")
        
            

        