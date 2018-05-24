from .Schedule import Schedule

class Checker:
    def checkE(self, sched, i ,j):
        if(self.checkEmpty(sched,i,j) and (sched.scheduleList[i][j] != 'nE' and  sched.scheduleList[i][j] != 'nED' and sched.scheduleList[i][j] != 'nEL' and sched.scheduleList[i][j] != 'nEN' and sched.scheduleList[i][j] != 'nEDL' and sched.scheduleList[i][j] != 'nELN' and sched.scheduleList[i][j] != 'nEDN' and sched.scheduleList[i][j] != 'x')):
            return True
        else:
            return False

    def checkD(self, sched, i ,j):
        if(self.checkEmpty(sched,i,j)  and (sched.scheduleList[i][j] != 'nD' and  sched.scheduleList[i][j] != 'nED' and sched.scheduleList[i][j] != 'nDL' and sched.scheduleList[i][j] != 'nDN' and sched.scheduleList[i][j] != 'nEDL' and sched.scheduleList[i][j] != 'nDLN' and sched.scheduleList[i][j] != 'nEDN' and sched.scheduleList[i][j] != 'x')):
            return True
        else:
            return False

    def checkL(self, sched, i ,j):
        if(self.checkEmpty(sched,i,j) and (sched.scheduleList[i][j] != 'nL' and  sched.scheduleList[i][j] != 'nDL' and sched.scheduleList[i][j] != 'nEL' and sched.scheduleList[i][j] != 'nLN' and sched.scheduleList[i][j] != 'nELN' and sched.scheduleList[i][j] != 'nDLN' and sched.scheduleList[i][j] != 'nEDL' and sched.scheduleList[i][j] != 'x')):
            return True
        else:
            return False

    def checkN(self, sched, i, j):
        if(self.checkEmpty(sched,i,j) and (sched.scheduleList[i][j] != 'nN' and  sched.scheduleList[i][j] != 'nDN' and sched.scheduleList[i][j] != 'nLN' and sched.scheduleList[i][j] != 'nEN' and sched.scheduleList[i][j] != 'nEDN' and sched.scheduleList[i][j] != 'nELN' and sched.scheduleList[i][j] != 'nDLN' and sched.scheduleList[i][j] != 'x')):
            return True
        else:
            return False

    def checkEmpty(self, sched, i, j):
        if(i < 35 or j < 16):
            if(sched.scheduleList[i][j] == '-' or (sched.scheduleList[i][j] != 'E' and  sched.scheduleList[i][j] != 'D' and sched.scheduleList[i][j] != 'L' and sched.scheduleList[i][j] != 'N')):
                return True
        else:
            return False
    def check(self, sched, value, i, j):
        if self.checkEmpty(sched, i, j):
            if value == 'E':
                if self.checkE(sched, value, i, j):
                    return True
            elif value == 'D':
                if self.checkD(sched, value, i, j):
                    return True
            elif value == 'L':
                if self.checkL(sched, value, i, j):
                    return True
            elif value == 'N':
                if self.checkN(sched, value, i, j):
                    return True
            else:
                return False

    def checkAll(self, sched, i, j):
        if not self.checkE(sched, i, j) or not self.checkD(sched, i, j) or not self.checkL(sched, i, j) or not self.checkN(sched, i, j):
            return True
        else:
            return False

    def weekCheck(self, sched, week, j):
        counter = 0
        for i in range(7):
            # print(week * 7 + i, j)
            if sched.scheduleList[week * 7 + i][j] == 'E' or sched.scheduleList[week * 7 + i][j] == 'D' or sched.scheduleList[week * 7 + i][j] == 'L' or sched.scheduleList[week * 7 + i][j] == 'N':
                counter +=1
        return counter
    # koniec checkerow