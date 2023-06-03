import Enums
import Assessment

menu = Enums.menu
Assessment = Assessment.Assessment


class Course:
    def __init__(self, course_code):
        self.name = course_code
        if course_code[-4] != ' ':
            self.name = course_code[:-3] + " " + course_code[-3:]
        self.current_grade: float = 0.0
        self.assessments_dict = {}

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

    def add_assessment(self):
        print("Now please enter the assessments for this course\nQuick Menu (Please only enter the number itself):")
        print("0. Exit")
        for num, key in enumerate(menu.keys()):
            print(str(num + 1) + '. ' + menu[key])
        print("Or enter any other assessment titles directly\nAssessment: ", end="")
        while True:
            a = input()
            if a == '0':
                break
            elif a in menu:
                self.assessments_dict.setdefault(menu[a], Assessment(menu[a]))
            else:
                self.assessments_dict.setdefault(a, Assessment(a))
        print("Course Assessment Titles Entry Complete.")

    def initiate_distribution(self):
        self.add_assessment()
        # Course Distribution
        print("Please enter the weight for the assessments entered: ")
        for assessment_obj in self.assessments_dict.values():
            valid_input = False
            if assessment_obj.weight != 'Undefined':
                valid_input = True
            while not valid_input:
                try:
                    weight = float(input("Enter weight for " + assessment_obj.name + ": "))
                    if weight < 0:
                        print("Weight for an assessment cannot be negative!")
                    else:
                        assessment_obj.update_weight(weight)
                        valid_input = True
                except ValueError:
                    print("You did not enter a number!")
        print("Course Assessment Weighting Entry Complete.")

    def edit_or_modify_assessment(self):
        # find the already existed assessment and change its grades weight
        while True:
            name = input("If you would like to exit, enter 0.\nIf you would like to add more assessments, enter '1'.\
                         \nIf you would like to edit and assessment, enter the assessment name directly.")
            if name == '0':
                break
            elif name == '1':
                self.initiate_distribution()
            elif name in self.assessments_dict.keys():
                print(name, "is selected.")
                ans = input("Do you wish to delete this assessment (1) or change its weight (2)? ")
                while not (ans == '0' or ans == '1' or ans == '2'):
                    ans = input("Invalid Input. Please only enter '1' or '2'.\
                    \nDo you wish to delete this assessment (1) or change its weight (2)? ")
                if ans == '0':
                    break
                elif ans == '1':
                    print(name, "is removed.")
                    self.assessments_dict.pop(name)
                elif ans == '2':
                    assess = self.assessments_dict.get(name)
                    valid_input = False
                    while not valid_input:
                        try:
                            new_weight = float(input("Enter weight for " + assess.name + ": "))
                            if new_weight < 0:
                                print("Weight for an assessment cannot be negative!")
                            else:
                                self.assessments_dict.get(name).update_weight(new_weight)
                                valid_input = True
                        except ValueError:
                            print("You did not enter a number!")
            else:
                print("'" + name + "' is not in this course assessment list, please try again.")

    def print_assessments(self):
        for num, assessment in enumerate(self.assessments_list):
            print(str(num + 1) + '. ' + assessment)

    def __str__(self):
        assessments = ""
        for a in self.assessments_dict.values():
            assessments += f'├─────────────────────────────────┤\n│ {a.name}:{a.weight:-{29 - len(a.name)}}% │\n'
        return f"╒═════════════════════════════════╕\n│ {self.name}                        │\n" \
            + assessments + "╘═════════════════════════════════╛"
