import Enums
import Assessment_Class


menu = Enums.menu
Assessment =Assessment_Class.Assessment

class Course:
    def __init__(self, course_code):
        self.name = course_code
        if course_code[-4] != ' ':
            self.name = course_code[:-3] + " " + course_code[-3:]
        self.current_grade: float = 0.0
        self.grade_distribution = []
        self.assessments_list = []
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
                self.assessment_dict.setdefault(menu[a],Assessment(menu[a]))
            else:
                self.assessment_dict.setdefault(a,Assessment(a))
        print("Course Assessment Titles Entry Complete.")

        print("Please enter the weight for the assessments entered: ")
        for assessment_obj in self.assessments_dict.values:
            valid_input = False
            while not valid_input:
                try:
                    weight = float(input("Enter weight for "+assessment_obj.__str__ + ": "))
                    if weight < 0:
                        print("Weight for an assessment cannot be negative!")
                    else:
                        assessment_obj.update_weight(weight)
                        valid_input = True
                except ValueError:
                    print("You did not enter a number!")
        print("Course Assessment Weighting Entry Complete.")   
            

    def modify_assessment_distribution(self):
        
        while True:
            name = input("Please enter the assessment name you want to edit its weight(0 to exit):")
            assessment_index = -1
            if name == '0':
                break
            elif name in self.assessments_list:
                print(name, "is selected.")
                assessment_index = self.assessments_list.index(name)
            else:
                print(name," is not in this course assessment list, please try again")
            
            valid_input = False
            while not valid_input:
                try:
                    new_weight = float(input("Enter weight for "+Assessment.name + ": "))
                    if new_weight < 0:
                        print("Weight for an assessment cannot be negative!")
                    else:
                        self.grade_distribution[assessment_index].moditfy_weight(new_weight)
                        valid_input = True
                except ValueError:
                    print("You did not enter a number!")

    def remove_assessment(self):
        while True:
            a = input("Enter the complete assessment name you would like to remove (0 to exit): ")
            if a == '0':
                break
            elif a in self.assessments_list:
                print(a, "is removed.")
                self.grade_distribution.remove(Assessment(a))
                self.assessments_list.remove(a)  
            else:
                print("Invalid input")

    def print_assessments(self):
        for num,assessment in enumerate(self.assessments_list):
            print(str(num + 1) + '. ' + assessment)
           
    def __str__(self):
        assessments = ""
        for a in self.grade_distribution:
            assessments += f'├─────────────────────────────────┤\n│ {a.name}:{a.weight:-{29-len(a.name)}}% │\n'
        return f"╒═════════════════════════════════╕\n│ {self.name}                        │\n"\
                + assessments + "╘═════════════════════════════════╛"