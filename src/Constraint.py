class Constraint:
    def __init__(self, number=None, weight=None):
        self.weight = weight
        self.number = number

    def set_weight(self,weight):
        self.weight=weight

    def get_weight(self):
        return self.weight

    def set_number(self,number):
        self.number=number

    def get_number(self):
        return self.number