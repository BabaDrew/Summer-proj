import csv
from tabulate import tabulate
import re # Enter 'pip install re' in your command line/terminal if you don't have this
import Enums
import Course

pattern = Enums.pattern
course_letters = Enums.course_letters
Course = Course.Course

class User:
    def __init__(self, name):
        self.name = name
        self.cur_year = 2023
        self.display_year = str(self.cur_year) +"-"+str(self.cur_year+1)
        self.courses = []

    def change_name(self, name):
        self.name = name

    def update_year(self):
        self.cur_year += 1
        self.display_year = str(self.cur_year) +"-"+str(self.cur_year+1)

    def add_course(self):
        # Course Name Valid Check
        valid_course = False
        while not valid_course:
            course_name = input("Enter the course name: ").upper()
            match = re.search(pattern, course_name)
            if match is not None:
                if match.group(1) in course_letters:
                    valid_course = True
                else:
                    print("The Course Code You Entered Does Not Exist")
            else:
                print("Invalid Entry for Course")

        # Create Course Object
        course = Course(course_name)
        course.initiate_distribution()

        # Add the details of this course
        confirm_entry = False
        while confirm_entry is False:
            print("Please verify if the following assessments are input correctly:")
            print(course)
            response = input("Is this accurate? Enter 'y' or 'n': ")
            if response == 'y':
                confirm_entry = True
            elif response == 'n':
                course.edit_or_modify_assessment()
            else:
                print("Invalid response. Please only enter 'y' or 'n'.")

        ''' not sure how this will work yet
        with open('course_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([course_name, course.grade_distribution])
        '''
        print("Course added successfully!")
        self.courses.append(course)

    def view_courses(self):
        courses = ""
        for c in self.courses:
            unit = f'{c.unit:.2f}'
            courses += f'├──────────┼──────────────┤\n│ {c.name} │{unit.center(14)}│\n'
        print("╒══════════╤══════════════╕\n│  Course  │  Unit Values │\n"+courses+"╘══════════╧══════════════╛")

