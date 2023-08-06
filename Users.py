import csv
from tabulate import tabulate
import re  # Enter 'pip install re' in your command line/terminal if you don't have this
import Enums
import Course

pattern = Enums.pattern
course_letters = Enums.course_letters
Course = Course.Course


class User:
    def __init__(self, name):
        self.name = name
        self.cur_year = 2023
        self.display_year = str(self.cur_year) + "-" + str(self.cur_year + 1)
        self.courses = [] # list of Course Objects

    def change_name(self, name):
        self.name = name

    def update_year(self):
        self.cur_year += 1
        self.display_year = str(self.cur_year) + "-" + str(self.cur_year + 1)

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
            if response == 'y' or response == 'Y':
                confirm_entry = True
            elif response == 'n' or response == 'N':
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

    def edit_course(self):
        # check if the course name is valid
        valid_courses = []
        for i in range(0, len(self.courses)):
            print(self.courses[i].name)
            valid_courses.append(self.courses[i].name)
        if len(valid_courses) == 0:
            print("You have no course registered yet!")
            return None

        course = None
        loop = True

        while loop:
            course_to_edit = input("Enter a course to edit from the above: ").upper()
            if len(course_to_edit) < 4:
                print("Invalid course entered!")
            else:
                if course_to_edit[-4] != " ":
                    course_to_edit = course_to_edit[:-3] + " " + course_to_edit[-3:]
                # course_to_edit is entered, check if in the current courses
                if course_to_edit in valid_courses:
                    loop = False
                    # Changing unit amount
                    course = self.courses[valid_courses.index(course_to_edit)]
                    print(course)
                    msg = "Change units from " + str(course.unit) + " to: "

                    valid = False
                    while not valid:
                        new_unit = input(msg)
                        try:
                            new_unit = float(new_unit)
                            if not (new_unit == 0.0 or new_unit == 1.5 or new_unit == 3.0 or new_unit == 6.0):
                                print("Invalid unit amounts entered")
                            else:
                                valid = True
                        except ValueError:
                            print("Invalid number of units entered")
                    old_unit = course.unit
                    course.unit = new_unit
                    print("Successfully updated units for", course.name, "from", old_unit, "to", new_unit)
                else:
                    print("Invalid course entered!")

                # Edit distribution
                print("Now proceeding with the edit of course grade distribution.")
                course.edit_or_modify_assessment()
        print(course)

    def view_courses(self, all=True):
        if all:
            courses = ""
            for c in self.courses:
                unit = f'{c.unit:.2f}'
                courses += f'├──────────┼──────────────┤\n│ {c.name} │{unit.center(14)}│\n'
            courses += "╘══════════╧══════════════╛"
            if len(self.courses) == 0:
                courses = "├─────────────────────────┤\n│No course registered yet!│\n╘═════════════════════════╛"
            print("╒══════════╤══════════════╕\n│  Course  │  Unit Values │\n" + courses)
        else:
            valid_courses = []
            
            if len(self.courses) == 0:
                print("There are no courses currently to view.")
                return
            for i in range(0, len(self.courses)):
                print(self.courses[i].name)
                valid_courses.append(self.courses[i].name)

            loop = True
            while loop:
                course_to_view = input("Enter a course to view from the above: ").upper()
                if len(course_to_view) < 4:
                    print("Invalid course entered!")
                else:
                    if course_to_view[-4] != " ":
                        course_to_view = course_to_view[:-3] + " " + course_to_view[-3:]
                    # course_to_edit is entered, check if in the current courses
                    if course_to_view in valid_courses:
                        print(self.courses[valid_courses.index(course_to_view)])
                        loop = False
                    else:
                        print("Invalid course entered!")
