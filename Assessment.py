class Assessment:
    def __init__(self,assessment_name,weight = "Undefined",mark = 0.0):
        self.name = assessment_name
        self.weight = weight
        self.mark = mark

    def __eq__(self, obj):
        return isinstance(obj, Assessment) and obj.name == self.name
    def __str__(self):
        return self.name
    
    def update_weight(self,weight):
        self.weight = weight