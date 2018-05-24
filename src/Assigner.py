import random as ran
from .Checker import Checker
from .Blocker import Blocker

class Assigner:
    def assignWeekends(self, sched):          #DZIALA GIT
        for i in range(16):
            weekends = [5,12,19,26,33]
            temp = weekends.pop(ran.randint(0, len(weekends) - 1))
            sched.scheduleList[temp-1][i] = 'nN'
            sched.scheduleList[temp][i] = 'x'
            sched.scheduleList[temp + 1][i] = 'x'
            temp = weekends.pop(ran.randint(0, len(weekends) - 1))
            sched.scheduleList[temp-1][i] = 'nN'
            sched.scheduleList[temp][i] = 'x'
            sched.scheduleList[temp + 1][i] = 'x'
        return sched

    def assignNightShifts(self, sch):                 #dziala git
        ch = Checker()
        bl = Blocker()
        unassignedNurses = [x for x in range(15)]
        tripleShifts = [x for x in range(2)]
        pointer = 0
        mistakes = 0
        while unassignedNurses and pointer <= 33:
            temp = ran.randint(0,len(unassignedNurses)-1)
            nurseNo = unassignedNurses.pop(temp)
            if ch.checkN(sch, pointer, nurseNo) and ch.checkN(sch, pointer + 1, nurseNo):
                if tripleShifts and unassignedNurses:
                    getsTrips = ran.randint(0, len(unassignedNurses) - len(tripleShifts))          #sprawdzic jeszcze raz
                    if(getsTrips == len(unassignedNurses) - len(tripleShifts) and ch.checkN(sch, pointer+2, nurseNo)):
                        sch.scheduleList[pointer][nurseNo] = 'N'
                        sch.scheduleList[pointer+1][nurseNo] = 'N'
                        sch.scheduleList[pointer+2][nurseNo] = 'N'
                        sch.scheduleList[pointer+3][nurseNo] = 'x'
                        sch.scheduleList[pointer+4][nurseNo] = 'x'
                        t = tripleShifts.pop()
                        pointer += 3
                        bl.blockColumn(sch, nurseNo, 'N')
                    else:
                        if pointer < 32:
                            sch.scheduleList[pointer][nurseNo] = 'N'
                            sch.scheduleList[pointer+1][nurseNo] = 'N'
                            sch.scheduleList[pointer+2][nurseNo] = 'x'
                            sch.scheduleList[pointer+3][nurseNo] = 'x'
                            pointer += 2
                            bl.blockColumn(sch, nurseNo, 'N')
                        else:
                            sch.scheduleList[pointer][nurseNo] = 'N'
                            sch.scheduleList[pointer+1][nurseNo] = 'N'

                else:
                    if pointer < 32:
                        sch.scheduleList[pointer][nurseNo] = 'N'
                        sch.scheduleList[pointer+1][nurseNo] = 'N'
                        sch.scheduleList[pointer+2][nurseNo] = 'x'
                        sch.scheduleList[pointer+3][nurseNo] = 'x'
                        pointer += 2
                        bl.blockColumn(sch, nurseNo, 'N')
                    else:
                        sch.scheduleList[pointer][nurseNo] = 'N'
                        sch.scheduleList[pointer+1][nurseNo] = 'N'
            else:
                pass
                """
                mistakes += 1
                if mistakes > 15:
                    assignNightShifts(kopia)"""
        else:
            return sch
        return sch

    def assignE(self, sched, ref, i, j):
        ch = Checker()
        bl = Blocker()
        if ch.checkE(sched, i , j) and ref.ref[i][0] > 0:
            sched.scheduleList[i][j] = 'E'
            ref.ref[i][0] -= 1
            if ref.ref[i][0] == 0:
                bl.blockRow(sched, i, 'E')
        return sched, ref

    def assignD(self, sched, ref, i, j):
        ch = Checker()
        bl = Blocker()
        if ch.checkD(sched, i , j) and ref.ref[i][1] > 0:
            sched.scheduleList[i][j] = 'D'
            ref.ref[i][1] -= 1
            if ref.ref[i][1] == 0:
                bl.blockRow(sched, i, 'D')
        return sched, ref

    def assignL(self, sched, ref, i, j):
        ch = Checker()
        bl = Blocker()
        if ch.checkL(sched, i , j) and ref.ref[i][2] > 0:
            sched.scheduleList[i][j] = 'L'
            ref.ref[i][2] -= 1
            if ref.ref[i][2] == 0:
                bl.blockRow(sched, i, 'L')
        return sched, ref

    def assignShifts(self, sched, ref, week):
        ch = Checker()
        for i in range(35):
            nursesLeft = [x for x in range(16)]
            if ref.ref[i][0] > 0:
                nurse = nursesLeft.pop(ran.randint(0,len(nursesLeft)-1))     #sprawdzic jeszcze raz
                if ch.checkE(sched, i , nurse):
                    sched, ref = self.assignE(sched, ref, i , nurse)

            if ref.ref[i][1] > 0:
                nurse = nursesLeft.pop(ran.randint(0,len(nursesLeft)-1))
                if ch.checkD(sched, i , nurse):
                    sched, ref = self.assignD(sched, ref, i , nurse)

            if ref.ref[i][2] > 0:
                nurse = nursesLeft.pop(ran.randint(0,len(nursesLeft)-1))
                if ch.checkL(sched, i , nurse):
                    sched, ref = self.assignL(sched, ref, i , nurse)
                    """ if ref.ref[i][0] > 0 or ref.ref[i][1] > 0 or ref.ref[i][2] > 0:
                sched,ref = assignShifts(sched, ref, week)"""
        return sched,ref