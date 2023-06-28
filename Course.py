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
        print("Or enter any other assessment titles directly ", end="")
        count=0
        while True:
            
            a = input("Enter assessment Choice {0}:".format((count+1)))
            if a == '0':
                break
            elif a in menu:
                self.assessments_dict.setdefault(menu[a], Assessment(menu[a]))
            else:
                self.assessments_dict.setdefault(a, Assessment(a))
        print("Course Assessment Titles Entry Complete.")
    def trial_func(self,assessment_obj,valid_input):
        
        while not valid_input:
                try:
                    weight = float(input("Enter Net weightage for " + assessment_obj.name + ": "))
                    freq=int(input("Enter number of times this assessment is testsed:"))
                    each_weight=float(input("Enter weightage of each {0} ".format(assessment_obj.name)))
                    drops=int(input("Enter number of assessments dropped:"))
                    if weight < 0 or freq<0 or each_weight<0 or drops<0:
                        print("No attribute for an assessment can be negative!")
                        
                    else:
                        if drops<=freq and ((freq-drops)*each_weight)==weight:
                            assessment_obj.update_weight(weight)
                            assessment_obj.update_freq(freq)
                            assessment_obj.update_each_weight(each_weight)
                            assessment_obj.update_drops(drops)
                            valid_input = True

                        else:
                            print("Attributes entered incorrectly please try again")
                            
                except ValueError:
                    print("You did not enter a number!")

    def assessment_parameters(self):
        valid_input=False
        for assessment_obj in self.assessments_dict.values():
            valid_input = False
            if assessment_obj.weight != 'Undefined':
                valid_input = True
            self.trial_func(assessment_obj,valid_input)

    def initiate_distribution(self):
        self.add_assessment()
        # Course Distribution
        print("Please enter the weight for the assessments entered: ")
        self.assessment_parameters()
        print("Course Assessment Weighting Entry Complete.")

    def edit_or_modify_assessment(self):
        # find the already existed assessment and change its grades weight
        while True:
            name = input("If you would like to exit, enter 0.\nIf you would like to add more assessments, enter '1'.\
                         \nIf you would like to edit an assessment, enter the assessment name directly: ")
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
                    self.trial_func(assess,valid_input=False)
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
