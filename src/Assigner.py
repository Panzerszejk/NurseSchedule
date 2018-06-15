import random as ran
from .Checker import Checker
from .Blocker import Blocker

class Assigner:
    def calculateWeek(self, j):
        return j//7

    def assignWeekends(self, sched):          #DZIALA GIT, a wlasnie ze nie
        """                                     dyntka, nie losuje sie tak jakbym chciał, bo randint jest glupi
        nurses = [x for x in range(15)]
        for i in range(15):
            nurses.append(i)
        a = b = 0
        while a == b:
            a = ran.randint(0,5) - 1
            b = ran.randint(0,5) - 1
        tab = [6 for x in range(5)]
        #tab[a] = 7
        #tab[b] = 7
        for i in range(5):
            for j in range(tab[i]):
                nur = ran.randint(0,len(nurses) - 1)
                numer = nurses.pop(nur)
                weekends = [5,12,19,26,33]
                temp = weekends.pop(ran.randint(0, len(weekends) - 1))
                sched.scheduleList[temp-1][numer] = 'nN'
                sched.scheduleList[temp][numer] = 'x'
                sched.scheduleList[temp + 1][numer] = 'x'
        return sched
        """
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

    def assignNightShifts(self, sch, shift):                 #dziala git
        ch = Checker()
        bl = Blocker
        unassignedNurses = [x for x in range(15)]
        pointer = 0
        for i in range(5):
            for j in range(2):
                temp = ran.randint(0,len(unassignedNurses)-1)
                nurseNo = unassignedNurses.pop(temp)
                if ch.checkN(sch, pointer, nurseNo) and ch.checkN(sch, pointer + 1, nurseNo):
                    sch.scheduleList[pointer][nurseNo] = 'N'
                    sch.scheduleList[pointer+1][nurseNo] = 'N'
         #           shift.table[nurseNo][self.calculateWeek(pointer)] -= 1
          #          shift.table[nurseNo][self.calculateWeek(pointer+1)] -= 1
                    sch.scheduleList[pointer+2][nurseNo] = 'x'
                    sch.scheduleList[pointer+3][nurseNo] = 'x'
                    pointer += 2
                    #bl.blockColumn(sch, nurseNo, "N")
            if pointer == 32 and ch.checkN(sch, pointer, nurseNo) and ch.checkN(sch, pointer + 1, nurseNo) and ch.checkN(sch, pointer + 2, nurseNo):
                temp = ran.randint(0,len(unassignedNurses)-1)
                nurseNo = unassignedNurses.pop(temp)
                sch.scheduleList[pointer][nurseNo] = 'N'
                sch.scheduleList[pointer+1][nurseNo] = 'N'
                sch.scheduleList[pointer+2][nurseNo] = 'N'
         #       shift.table[nurseNo][self.calculateWeek(pointer)] -= 1
         #       shift.table[nurseNo][self.calculateWeek(pointer+1)] -= 1
         #       shift.table[nurseNo][self.calculateWeek(pointer+2)] -= 1
                pointer += 3
                #bl.blockColumn(sch, nurseNo, 'N')
            elif ch.checkN(sch, pointer, nurseNo) and ch.checkN(sch, pointer + 1, nurseNo) and ch.checkN(sch, pointer + 2, nurseNo):
                temp = ran.randint(0,len(unassignedNurses)-1)
                nurseNo = unassignedNurses.pop(temp)
                sch.scheduleList[pointer][nurseNo] = 'N'
                sch.scheduleList[pointer+1][nurseNo] = 'N'
                sch.scheduleList[pointer+2][nurseNo] = 'N'
                sch.scheduleList[pointer+3][nurseNo] = 'x'
                sch.scheduleList[pointer+4][nurseNo] = 'x'
        #        shift.table[nurseNo][self.calculateWeek(pointer)] -= 1
        #        shift.table[nurseNo][self.calculateWeek(pointer+1)] -= 1
        #        shift.table[nurseNo][self.calculateWeek(pointer+2)] -= 1
                pointer += 3
                #bl.blockColumn(sch, nurseNo, 'N')
        return sch, shift

    def assignE(self, sched, ref, shift, i, j):
        ch = Checker()
        bl = Blocker()
        week = self.calculateWeek(j)
        if ch.checkEmpty(sched, i, j) and  ch.checkE(sched, i , j) and ref.ref[i][0] > 0 and shift.table[j][week]>0:
            sched.scheduleList[i][j] = 'E'
            ref.ref[i][0] -= 1
        #    shift.table[j][week] -= 1
            if ref.ref[i][0] == 0:
                bl.blockRow(sched, i, 'E')
        return sched, ref, shift

    def assignD(self, sched, ref, shift, i, j):
        ch = Checker()
        bl = Blocker()
        week = self.calculateWeek(j)
        if ch.checkEmpty(sched, i, j) and ch.checkD(sched, i , j) and ref.ref[i][1] > 0 and shift.table[j][week]>0:
            sched.scheduleList[i][j] = 'D'
            ref.ref[i][1] -= 1
       #     shift.table[j][week] -= 1
            if ref.ref[i][1] == 0:
                bl.blockRow(sched, i, 'D')
        return sched, ref, shift

    def assignL(self, sched, ref, shift, i, j):
        ch = Checker()
        bl = Blocker()
        week = self.calculateWeek(j)
        if ch.checkEmpty(sched, i, j) and  ch.checkL(sched, i , j) and ref.ref[i][2] > 0 and shift.table[j][week]>0:
            sched.scheduleList[i][j] = 'L'
            if(i<34):
                sched.scheduleList[i+1][j] = 'nL'
         #   shift.table[j][week] -= 1
            ref.ref[i][2] -= 1
            if ref.ref[i][2] == 0:
                bl.blockRow(sched, i, 'L')
        return sched, ref, shift

    def assignShifts(self, sched, ref, shift, week):
        ch = Checker()
        for i in range(35):
            nursesLeft = [x for x in range(16)]
            if ref.ref[i][0] > 0:
                nurse = nursesLeft.pop(ran.randint(0,len(nursesLeft)-1))     #sprawdzic jeszcze raz
                if ch.checkE(sched, i , nurse) and ch.checkEmpty(sched, i, nurse):
                    sched, ref, shift = self.assignE(sched, ref, shift, i , nurse)

            if ref.ref[i][1] > 0:
                nurse = nursesLeft.pop(ran.randint(0,len(nursesLeft)-1))
                if ch.checkD(sched, i , nurse) and ch.checkEmpty(sched, i, nurse):
                    sched, ref, shift  = self.assignD(sched, ref, shift, i , nurse)

            if ref.ref[i][2] > 0:
                nurse = nursesLeft.pop(ran.randint(0,len(nursesLeft)-1))
                if ch.checkL(sched, i , nurse) and ch.checkEmpty(sched, i, nurse):
                    sched, ref, shift  = self.assignL(sched, ref, shift, i , nurse)
                    """ if ref.ref[i][0] > 0 or ref.ref[i][1] > 0 or ref.ref[i][2] > 0:
                sched,ref = assignShifts(sched, ref, week)"""
        return sched,ref, shift
