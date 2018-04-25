class ConstraintChecker:
    def __init__(self,schedule=None):
        self.totalWeight=0
        self.schedule=schedule

    def check(self, constraint):
        if constraint.number == 1:
            pass
            self.totalWeight+=constraint.weight
        elif constraint.number == 3:
            pass
            self.totalWeight+=constraint.weight
        elif constraint.number == 5:
            pass
            self.totalWeight+=constraint.weight
        elif constraint.number == 7:
            pass
            self.totalWeight+=constraint.weight
        elif constraint.number == 9:
            pass
            self.totalWeight+=constraint.weight
        elif constraint.number == 13:
            pass
            self.totalWeight+=constraint.weight

    def get_totalWeight(self):
        return self.totalWeight

    def set_totalWeight(self,weight):
        self.totalWeight=weight

    def import_schedule(self,schedule):
        self.schedule=schedule