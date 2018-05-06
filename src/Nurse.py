class Nurse:
    def __init__(self, number, name, surname, maxShifts, minShifts, workingNights=True):
        self.number = number
        self.name = name
        self.surname = surname
        self.maxShifts = maxShifts
        self.minShifts = minShifts
        self.workingNights = workingNights

    def get_minShifts(self):
        return self.minShifts

    def get_maxShifts(self):
        return self.maxShifts

    def has_nights(self):
        return self.workingNights

    def get_number(self):
        return self.number