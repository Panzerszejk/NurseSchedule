from .Schedule import Schedule
from .Week import Week
from .ReferenceTable import ReferenceTable
import numpy as np
import random as ran
import sys

"""
    Now this code as coarse as  possible, and will be "objectified" next week
"""
def assignWeekends(sched):          #DZIALA GIT
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

def assignNightShifts(sch):                 #dziala git
    unassignedNurses = [x for x in range(15)]
    tripleShifts = [x for x in range(2)]
    pointer = 0
    mistakes = 0
    while unassignedNurses and pointer <= 33:
        temp = ran.randint(0,len(unassignedNurses)-1)
        nurseNo = unassignedNurses.pop(temp)
        if checkN(sch, pointer, nurseNo) and checkN(sch, pointer + 1, nurseNo):
            if tripleShifts and unassignedNurses:
                getsTrips = ran.randint(0, len(unassignedNurses) - len(tripleShifts))          #sprawdzic jeszcze raz
                if(getsTrips == len(unassignedNurses) - len(tripleShifts) and checkN(sch, pointer+2, nurseNo)):
                    sch.scheduleList[pointer][nurseNo] = 'N'
                    sch.scheduleList[pointer+1][nurseNo] = 'N'
                    sch.scheduleList[pointer+2][nurseNo] = 'N'
                    sch.scheduleList[pointer+3][nurseNo] = 'x'
                    sch.scheduleList[pointer+4][nurseNo] = 'x'
                    t = tripleShifts.pop()
                    pointer += 3
                    blockColumn(sch, nurseNo, 'N')
                else:
                    if pointer < 32:
                        sch.scheduleList[pointer][nurseNo] = 'N'
                        sch.scheduleList[pointer+1][nurseNo] = 'N'
                        sch.scheduleList[pointer+2][nurseNo] = 'x'
                        sch.scheduleList[pointer+3][nurseNo] = 'x'
                        pointer += 2
                        blockColumn(sch, nurseNo, 'N')
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
                    blockColumn(sch, nurseNo, 'N')
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

def blockE(sched,i,j):
    if(sched.scheduleList[i][j] == '-'):
        return 'nE'
    if(sched.scheduleList[i][j] == 'nD'):
        return 'nED'
    if(sched.scheduleList[i][j] == 'nL'):
        return 'nEL'
    if(sched.scheduleList[i][j] == 'nN'):
        return 'nEN'
    if(sched.scheduleList[i][j] == 'nDL'):
        return 'nEDL'
    if(sched.scheduleList[i][j] == 'nDN'):
        return'nEDN'
    if(sched.scheduleList[i][j] == 'nLN'):
        return 'nELN'
    if(sched.scheduleList[i][j] == 'nDLN'):
        return 'x'
    if(sched.scheduleList[i][j] == 'E'):
        return 'E'
    if(sched.scheduleList[i][j] == 'D'):
        return 'D'
    if(sched.scheduleList[i][j] == 'L'):
        return 'L'
    if(sched.scheduleList[i][j] == 'N'):
        return 'N'
    if(sched.scheduleList[i][j] == 'x'):
        return 'x'
    return 'x'

def blockD(sched,i,j):
    if(sched.scheduleList[i][j] == '-'):
        return 'nD'
    if(sched.scheduleList[i][j] == 'nE'):
        return 'nED'
    if(sched.scheduleList[i][j] == 'nL'):
        return 'nDL'
    if(sched.scheduleList[i][j] == 'nN'):
        return 'nDN'
    if(sched.scheduleList[i][j] == 'nEL'):
        return 'nEDL'
    if(sched.scheduleList[i][j] == 'nEN'):
        return 'nEDN'
    if(sched.scheduleList[i][j] == 'nLN'):
        return 'nDLN'
    if(sched.scheduleList[i][j] == 'nELN'):
        return 'x'
    if(sched.scheduleList[i][j] == 'E'):
        return 'E'
    if(sched.scheduleList[i][j] == 'D'):
        return 'D'
    if(sched.scheduleList[i][j] == 'L'):
        return 'L'
    if(sched.scheduleList[i][j] == 'N'):
        return 'N'
    if(sched.scheduleList[i][j] == 'x'):
        return 'x'
    return 'x'

def blockL(sched,i,j):
    if(sched.scheduleList[i][j] == '-'):
        return 'nL'
    if(sched.scheduleList[i][j] == 'nE'):
        return 'nEL'
    if(sched.scheduleList[i][j] == 'nD'):
        return 'nDL'
    if(sched.scheduleList[i][j] == 'nN'):
        return 'nLN'
    if(sched.scheduleList[i][j] == 'nED'):
        return 'nEDL'
    if(sched.scheduleList[i][j] == 'nDN'):
        return 'nDLN'
    if(sched.scheduleList[i][j] == 'nEN'):
        return 'nELN'
    if(sched.scheduleList[i][j] == 'nEDL'):
        return 'x'
    if(sched.scheduleList[i][j] == 'E'):
        return 'E'
    if(sched.scheduleList[i][j] == 'D'):
        return 'D'
    if(sched.scheduleList[i][j] == 'L'):
        return 'L'
    if(sched.scheduleList[i][j] == 'N'):
        return 'N'
    if(sched.scheduleList[i][j] == 'x'):
        return 'x'
    return 'x'

def blockN(sched,i,j):
    if(sched.scheduleList[i][j] == '-'):
        return 'nN'
    if(sched.scheduleList[i][j] == 'nE'):
        return 'nEN'
    if(sched.scheduleList[i][j] == 'nD'):
        return 'nDN'
    if(sched.scheduleList[i][j] == 'nL'):
        return 'nLN'
    if(sched.scheduleList[i][j] == 'nED'):
        return 'nEDN'
    if(sched.scheduleList[i][j] == 'nEL'):
        return 'nELN'
    if(sched.scheduleList[i][j] == 'nDL'):
        return 'nDLN'
    if(sched.scheduleList[i][j] == 'nEDL'):
        return 'x'
    if(sched.scheduleList[i][j] == 'E'):
        return 'E'
    if(sched.scheduleList[i][j] == 'D'):
        return 'D'
    if(sched.scheduleList[i][j] == 'L'):
        return 'L'
    if(sched.scheduleList[i][j] == 'N'):
        return 'N'
    if(sched.scheduleList[i][j] == 'x'):
        return 'x'
    return 'x'

def blockRow(sched, i, value):
    if value == 'E':
        for j in range(16):
            sched.scheduleList[i][j] = blockE(sched,i,j)
    if value == 'D':
        for j in range(16):
            sched.scheduleList[i][j] = blockD(sched,i,j)
    if value == 'L':
        for j in range(16):
            sched.scheduleList[i][j] = blockL(sched,i,j)
    if value == 'N':
        for j in range(16):
            sched.scheduleList[i][j] = blockN(sched,i,j)
    return sched

def blockColumn(sched, j, value):
    if value == 'E':
        for i in range(35):
            sched.scheduleList[i][j] = blockE(sched,i,j)
    if value == 'D':
        for i in range(35):
            sched.scheduleList[i][j] = blockD(sched,i,j)
    if value == 'L':
        for i in range(35):
            sched.scheduleList[i][j] = blockL(sched,i,j)
    if value == 'N':
        for i in range(35):
            sched.scheduleList[i][j] = blockN(sched,i,j)
    return sched
#PRZYSZLA KLASA CHECKER

def checkE(sched, i ,j):
    if(checkEmpty(sched,i,j) and (sched.scheduleList[i][j] != 'nE' and  sched.scheduleList[i][j] != 'nED' and sched.scheduleList[i][j] != 'nEL' and sched.scheduleList[i][j] != 'nEN' and sched.scheduleList[i][j] != 'nEDL' and sched.scheduleList[i][j] != 'nELN' and sched.scheduleList[i][j] != 'nEDN' and sched.scheduleList[i][j] != 'x')):
        return True
    else:
        return False

def checkD(sched, i ,j):
    if(checkEmpty(sched,i,j)  and (sched.scheduleList[i][j] != 'nD' and  sched.scheduleList[i][j] != 'nED' and sched.scheduleList[i][j] != 'nDL' and sched.scheduleList[i][j] != 'nDN' and sched.scheduleList[i][j] != 'nEDL' and sched.scheduleList[i][j] != 'nDLN' and sched.scheduleList[i][j] != 'nEDN' and sched.scheduleList[i][j] != 'x')):
        return True
    else:
        return False

def checkL(sched, i ,j):
    if(checkEmpty(sched,i,j) and (sched.scheduleList[i][j] != 'nL' and  sched.scheduleList[i][j] != 'nDL' and sched.scheduleList[i][j] != 'nEL' and sched.scheduleList[i][j] != 'nLN' and sched.scheduleList[i][j] != 'nELN' and sched.scheduleList[i][j] != 'nDLN' and sched.scheduleList[i][j] != 'nEDL' and sched.scheduleList[i][j] != 'x')):
        return True
    else:
        return False

def checkN(sched, i, j):
    if(checkEmpty(sched,i,j) and (sched.scheduleList[i][j] != 'nN' and  sched.scheduleList[i][j] != 'nDN' and sched.scheduleList[i][j] != 'nLN' and sched.scheduleList[i][j] != 'nEN' and sched.scheduleList[i][j] != 'nEDN' and sched.scheduleList[i][j] != 'nELN' and sched.scheduleList[i][j] != 'nDLN' and sched.scheduleList[i][j] != 'x')):
        return True
    else:
        return False

def checkEmpty(sched, i, j):
    if(i < 35 or j < 16):
        if(sched.scheduleList[i][j] == '-' or (sched.scheduleList[i][j] != 'E' and  sched.scheduleList[i][j] != 'D' and sched.scheduleList[i][j] != 'L' and sched.scheduleList[i][j] != 'N')):
            return True
    else:
        return False

def check(sched, value, i, j):
    if checkEmpty(sched, i, j):
        if value == 'E':
            if checkE(sched, value, i, j):
                return True
        elif value == 'D':
            if checkD(sched, value, i, j):
                return True
        elif value == 'L':
            if checkL(sched, value, i, j):
                return True
        elif value == 'N':
            if checkN(sched, value, i, j):
                return True
        else:
            return False

def checkAll(sched, i, j):
    if not checkE(sched, i, j) or not checkD(sched, i, j) or not checkL(sched, i, j) or not checkN(sched, i, j):
        return True
    else:
        return False

def weekCheck(sched, week, j):
    counter = 0
    for i in range(7):
        # print(week * 7 + i, j)
        if sched.scheduleList[week * 7 + i][j] == 'E' or sched.scheduleList[week * 7 + i][j] == 'D' or sched.scheduleList[week * 7 + i][j] == 'L' or sched.scheduleList[week * 7 + i][j] == 'N':
            counter +=1
    return counter
# koniec checkerow

def assignE(sched, ref, i, j):
    if checkE(sched, i , j) and ref.ref[i][0] > 0:
        sched.scheduleList[i][j] = 'E'
        ref.ref[i][0] -= 1
        if ref.ref[i][0] == 0:
            blockRow(sched, i, 'E')
    return sched, ref

def assignD(sched, ref, i, j):
    if checkD(sched, i , j) and ref.ref[i][1] > 0:
        sched.scheduleList[i][j] = 'D'
        ref.ref[i][1] -= 1
        if ref.ref[i][1] == 0:
            blockRow(sched, i, 'D')
    return sched, ref

def assignL(sched, ref, i, j):
    if checkL(sched, i , j) and ref.ref[i][2] > 0:
        sched.scheduleList[i][j] = 'L'
        ref.ref[i][2] -= 1
        if ref.ref[i][2] == 0:
            blockRow(sched, i, 'L')
    return sched, ref

def assignShifts(sched, ref, week):
    for i in range(35):
        nursesLeft = [x for x in range(16)]
        if ref.ref[i][0] > 0:
            nurse = nursesLeft.pop(ran.randint(0,len(nursesLeft)-1))     #sprawdzic jeszcze raz
            if checkE(sched, i , nurse):
                sched, ref = assignE(sched, ref, i , nurse)

        if ref.ref[i][1] > 0:
            nurse = nursesLeft.pop(ran.randint(0,len(nursesLeft)-1))
            if checkD(sched, i , nurse):
                sched, ref = assignD(sched, ref, i , nurse)

        if ref.ref[i][2] > 0:
            nurse = nursesLeft.pop(ran.randint(0,len(nursesLeft)-1))
            if checkL(sched, i , nurse):
                sched, ref = assignL(sched, ref, i , nurse)
                """ if ref.ref[i][0] > 0 or ref.ref[i][1] > 0 or ref.ref[i][2] > 0:
            sched,ref = assignShifts(sched, ref, week)"""
    return sched,ref

def cleanup(sched):         #DZIALA GIT
    for i in range(35):
        for j in range(16):
            if (sched.scheduleList[i][j] == 'E' or  sched.scheduleList[i][j] == 'D' or sched.scheduleList[i][j] == 'L' or sched.scheduleList[i][j] == 'N'):
                pass
            else:
                sched.scheduleList[i][j] = '-'
    return sched

class Generator:
    def generate(self, ward, sched=None):
        sys.setrecursionlimit(10000)
        output = Schedule() #write data to output object
        if sched is None:
            output = Schedule()
            ref = ReferenceTable()
            output = assignWeekends(output)
            output = assignNightShifts(output)
            for i in range(5):
                output, ref = assignShifts(output, ref, i)
            output = cleanup(output)
            #display(ref)
            output.displayer.display()
        elif isinstance(sched, Week):
            week=sched  #namechange for consistency, not necessary
            #code for imported week parameter call (data from previous week)
        elif isinstance(sched, Schedule):
            pass
            #code for imported schedule parameter call (data from whole previous schedule)
        return output

#sched is an object of class Week or Schedule depending on what is imported!
