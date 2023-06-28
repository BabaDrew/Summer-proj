class Assessment:
    def __init__(self,assessment_name,freq=0, drops=0, each_weight=0, weight = "Undefined",mark = 0.0,):
        self.name = assessment_name
        self.weight = weight
        self.mark = mark
        self.freq=freq
        self.drops=drops
        self.each_weight=each_weight

    def __eq__(self, obj):
        return isinstance(obj, Assessment) and obj.name == self.name
    def __str__(self):
        return self.name
    
    def update_weight(self,weight):
        self.weight = weight
    def update_freq(self,freq):
        self.freq=freq
    def update_drops(self,drops):
        self.drops=drops
    def update_each_weight(self,each_weight):
        self.each_weight= each_weight
    