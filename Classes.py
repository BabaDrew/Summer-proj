import csv
from tabulate import tabulate
import re # Enter 'pip install re' in your command line/terminal if you don't have this

course_letters = ['AGHE', 'ANAT', 'ANIM', 'ANSH', 'APSC', 'ARAB', 'ARTC', 'ARTF', 'ARTH', 'ARTL', 'ASCX',
                  'ASTR', 'BADR', 'BCHM', 'BIOL', 'BIOM', 'BLCK', 'BMED', 'BMIF', 'BWRC', 'CANC', 'CBME',
                  'CHEE', 'CHEM', 'CHIN', 'CIL', 'CISC', 'CIVL', 'CLAS', 'CLST', 'CMAS', 'CMPE', 'COCA',
                  'COGS', 'COMM', 'COMP', 'CRSS', 'CURR', 'CUST', 'CWRI', 'DDHT', 'DEVS', 'DRAM', 'ECON',
                  'EDST', 'EERL', 'ELEC', 'EMPR', 'ENCH', 'ENGL', 'ENIN', 'ENPH', 'ENSC', 'EPID', 'FILM',
                  'FOCI', 'FOUN', 'FREN', 'FRST', 'GENG', 'GEOE', 'GEOL', 'GNDS', 'GPHY', 'GREK', 'GRMN',
                  'HEBR', 'HIST', 'HLTH', 'HPE', 'ICL', 'IDIS', 'INDG', 'INTN', 'INTS', 'INUK', 'ITLN',
                  'JAPN', 'JWST', 'KHS', 'KNPE', 'LANG', 'LATN', 'LAW', 'LIBS', 'LING', 'LISC', 'LLCU',
                  'LSM', 'MAPP', 'MATH', 'MECH', 'MEDS', 'MGMT', 'MICR', 'MINE', 'MIR', 'MNTC', 'MUTH',
                  'NSCI', 'NURS', 'PACT', 'PATH', 'PHAR', 'PHGY', 'PHIL', 'PHMI', 'PHYS', 'POLS', 'PORT',
                  'PPEC', 'PRAC', 'PROF', 'PSYC', 'QGSP', 'RELS', 'REPD', 'RHBS', 'RHL', 'SCCS', 'SOCY',
                  'SOFT', 'SPAN', 'STAM', 'STAT', 'SURP', 'TMED', 'WRIT']

pattern = r"([A-Za-z]{3,4})\s?\d{3}"  # A-Z that occurs 3 to 4 times, with an optional space, and 3 digits

menu = {'1': 'Attendance', '2': 'Participation', '3': 'Quizzes', '4': 'Assignments', '5': 'Term Tests',
        '6': 'Midterms', '7': 'Exam', '8': 'Final Project'}

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
            response = input("Is this accurate? Enter 'y'/'n': ")
            if response == 'y':
                confirm_entry = True
            elif response == 'n':
                course.remove_assessment()
            else:
                print("Invalid entry")

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

class Course:
    def __init__(self, course_code):
        self.name = course_code
        if course_code[-4] != ' ':
            self.name = course_code[:-3] + " " + course_code[-3:]
        self.current_grade: float = 0.0
        self.grade_distribution = []
        self.assessments = []

        # Unit for the course
        unit_check = False
        while not unit_check:
            try:
                unit = float(input("Enter the number of units for this course: "))
                if not (unit == 0.0 or unit == 1.5 or unit == 3.0 or unit == 6.0):
                    print("Invalid unit amounts entered")
                else:
                    self.unit = unit
                    unit_check = True
            except ValueError:
                print("You did not enter a number!")
    def initiate_distribution(self):
        # Course Distribution
        print("Now please enter the assessments for this course\nQuick Menu (Please only enter the number itself):")
        print("0. Exit")
        for num, key in enumerate(menu.keys()):
            print(str(num + 1) + '. ' + menu[key])
        print("Or enter any other assessment titles directly\nAssessment: ",end="")
        a = ""
        counter = 0
        while True:
            a = input()
            if a == '0':
                break
            elif a in menu:
                self.grade_distribution.append(Assessment(menu[a]))
            else:
                self.grade_distribution.append(Assessment(a))
        print("Course Assessment Titles Entry Complete.")

        print("Please enter the weight for the assessments entered: ")
        for assessment in self.grade_distribution:
            valid_input = False
            while not valid_input:
                try:
                    weight = float(input("Enter weight for "+assessment.name + ": "))
                    if weight < 0:
                        print("Weight for an assessment cannot be negative!")
                    else:
                        assessment.weight = weight
                        valid_input = True
                except ValueError:
                    print("You did not enter a number!")
        print("Course Assessment Weighting Entry Complete.")
        for assessment in self.grade_distribution:
            self.assessments.append(assessment.name)


    def remove_assessment(self):
        while True:
            a = input("Enter the complete assessment name you would like to remove (0 to exit): ")
            if a == '0':
                break
            elif a in self.assessments:
                print(a, "is removed.")
                self.grade_distribution.remove(Assessment(a))
                self.assessments.remove(a)
            else:
                print("Invalid input")

    def print_assessments(self):
        for num,assessment in enumerate(self.grade_distribution):
            print(str(num + 1) + '. ' + assessment)

    def __str__(self):
        assessments = ""
        for a in self.grade_distribution:
            assessments += f'├─────────────────────────────────┤\n│ {a.name}:{a.weight:-{29-len(a.name)}}% │\n'
        return f"╒═════════════════════════════════╕\n│ {self.name}                        │\n"\
                + assessments + "╘═════════════════════════════════╛"

class Assessment:
    def __init__(self,assessment_name,weight = 0.0):
        self.name = assessment_name
        self.weight = weight

    def __eq__(self, obj):
        return isinstance(obj, Assessment) and obj.name == self.name
    def __str__(self):
        return self.name