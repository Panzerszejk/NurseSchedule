#from .Generator import Generator
from .Schedule import Schedule

class Blocker:
    def blockE(self, sched,i,j):
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

    def blockD(self, sched,i,j):
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

    def blockL(self, sched,i,j):
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

    def blockN(self, sched,i,j):
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

    def blockRow(self, sched, i, value):
        if value == 'E':
            for j in range(16):
                sched.scheduleList[i][j] = self.blockE(sched,i,j)
        if value == 'D':
            for j in range(16):
                sched.scheduleList[i][j] = self.blockD(sched,i,j)
        if value == 'L':
            for j in range(16):
                sched.scheduleList[i][j] = self.blockL(sched,i,j)
        if value == 'N':
            for j in range(16):
                sched.scheduleList[i][j] = self.blockN(sched,i,j)
        return sched

    def blockColumn(self, sched, j, value):
        if value == 'E':
            for i in range(35):
                sched.scheduleList[i][j] = self.blockE(sched,i,j)
        if value == 'D':
            for i in range(35):
                sched.scheduleList[i][j] = self.blockD(sched,i,j)
        if value == 'L':
            for i in range(35):
                sched.scheduleList[i][j] = self.blockL(sched,i,j)
        if value == 'N':
            for i in range(35):
                sched.scheduleList[i][j] = self.blockN(sched,i,j)
        return sched