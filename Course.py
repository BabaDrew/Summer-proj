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
        #Allows the user to add in assessment title for courses they have added
        print("Now please enter the assessments for this course\nQuick Menu (Please only enter the number itself):")
        print("0. Exit")
        for num, key in enumerate(menu.keys()):                 #Shows menu from Enums with pre-determined titles for the user to use 
            print(str(num + 1) + '. ' + menu[key])
        print("Or enter any other assessment titles directly.")
        count = 0
        while True:

            a = input("Enter assessment {0}: ".format((count + 1)))
            if a == '0':
                break
            elif a in menu:
                print(menu[a], "added.")
                self.assessments_dict.setdefault(menu[a], Assessment(menu[a]))
            else:
                self.assessments_dict.setdefault(a, Assessment(a))
                print(a, "added.")
            count += 1

        print("Course Assessment Titles Entry Complete.")

    def assessment_parameters(self, assessment_obj: Assessment):
        # Allows the user to enter in the net weightage, no. of times assessment is tested, weightage of each assessment
        # and no. of dropped assessments for the assessments they have added
        valid_input = False
        while not valid_input:
            try:
                weight = float(input("Enter Net weightage for " + assessment_obj.name + ": "))
                freq = int(input("Enter number of times this assessment is tested: "))
                if freq != 1:  # If 1 frequency no need to worry                #Also maybe add 'and freq>1' because we don't to get this when freq=0
                    each_weight = float(input("Enter weightage of each {0}: ".format(assessment_obj.name)))
                    drops = int(input("Enter number of assessments dropped: "))
                else:
                    each_weight = weight
                    drops = 0

                if weight < 0 or freq < 0 or each_weight < 0 or drops < 0:
                    print("No attribute for an assessment can be negative!")
                else:
                    if drops <= freq and ((freq - drops) * each_weight) == weight:
                        assessment_obj.update_weight(weight)
                        assessment_obj.update_freq(freq)
                        assessment_obj.update_each_weight(each_weight)
                        assessment_obj.update_drops(drops)
                        assessment_obj.need_entry = False
                        valid_input = True
                        print("Successful entry for " + assessment_obj.name + ".",end="\n\n")
                    else:
                        print("Attributes entered incorrectly, please try again")
            except ValueError:
                print("You did not enter a number!")

    def initiate_distribution(self):

        self.add_assessment()

        # Course Distribution
        print("Please enter the weight for the assessments entered.")
        for assessment_obj in self.assessments_dict.values():
            if assessment_obj.need_entry is True:
                self.assessment_parameters(assessment_obj)
        print("Course Assessment Weighting Entry Complete.")

    def edit_or_modify_assessment(self):
        # find the already existed assessment and change its grades weight
        while True:
            name = input("If you would like to exit, enter 0.\nIf you would like to add more assessments, enter '1'.\
                         \nIf you would like to edit an assessment weighting, enter the assessment name directly: ")
            if name == '0':
                break
            elif name == '1':
                self.initiate_distribution()
            elif name in self.assessments_dict.keys():
                print(name, "is selected.")
                ans = input("Do you wish to delete this assessment (1) or change its grade distribution (2)? ")
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
                    self.assessment_parameters(assess)
            else:
                print("'" + name + "' is not in this course assessment list, please try again.")

    def print_assessments(self):
        for num, assessment in enumerate(self.assessments_list):
            print(str(num + 1) + '. ' + assessment)

    def __str__(self):
        assessments = ""
        for a in self.assessments_dict.values():
            spacing = 29 - len(a.name)
            assessments += f'├─────────────────────────────────┤\n│ {a.name}:{a.weight:-{spacing}}% │\n'
        return f"╒═════════════════════════════════╕\n│ {self.name}                        │\n" \
            + assessments + "╘═════════════════════════════════╛"
