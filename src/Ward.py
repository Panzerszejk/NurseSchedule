class Ward:
    def __init__(self):
        self.nurses=list()
        self.constraints=list()

    def add_nurse(self, nurse):
        self.nurses.append(nurse)

    def delete_nurse(self, nurse):
        self.nurses.remove(nurse)

    def add_constraint(self, constraint):
        self.constraints.append(constraint)

    def delete_constraint(self, constraint):
        self.constraints.remove(constraint)

    def get_nurses(self):
        return self.nurses

    def get_constraints(self):
        return self.constraints

    def sort_nurses(self):
        __temp__=sorted(self.nurses, key=lambda nurse: nurse.number)
        self.nurses=__temp__

    def sort_constraints(self):
        __temp__=sorted(self.constraints, key=lambda constraint: constraint.number)
        self.constraints=__temp__

    def print_initials(self,number):
        return(self.nurses[number].name[0],self.nurses[number].surname[0])

