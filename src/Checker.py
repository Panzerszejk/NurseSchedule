from .Schedule import Schedule
from .SymbolTable import SymbolTable

class Checker:
    def checkE(self, sched, i ,j):
        symbol = sched.scheduleList[i]
        goofyList = [sched.scheduleList[i]]
        result1 =  any(symbol in goofyList for symbol in SymbolTable.occupiedSymbols)
        result2 =  any(symbol in goofyList for symbol in SymbolTable.notESymbols)
        #       ['-',  'E',   'D',   'L',   'N',   'nE',  'nD', 'nL', 'nN', 'nED', 'nEL', 'nEN','nDL','nDN','nLN','nDLN','nELN','nEDN','nEDL', 'x']
        lista = [True, False, False, False, False, False, True, True, True, False, False, False, True, True, True, True, False, False, False, False]
        cond = not(result1 or result2)
        if cond:
            return True
        else:
            return False

    def checkD(self, sched, i ,j):
        symbol = sched.scheduleList[i]
        goofyList = [sched.scheduleList[i]]
        result1 =  any(symbol in goofyList for symbol in SymbolTable.occupiedSymbols)
        result2 =  any(symbol in goofyList for symbol in SymbolTable.notDSymbols)
        #       ['-',  'E',   'D',   'L',   'N',   'nE',  'nD', 'nL', 'nN', 'nED', 'nEL', 'nEN','nDL','nDN','nLN','nDLN','nELN','nEDN','nEDL', 'x']
        lista = [True, False, False, False, False, False, True, True, True, False, False, False, True, True, True, True, False, False, False, False]
        cond = not(result1 or result2)
        if cond:
            return True
        else:
            return False

    def checkL(self, sched, i ,j):
        symbol = sched.scheduleList[i]
        goofyList = [sched.scheduleList[i]]
        result1 =  any(symbol in goofyList for symbol in SymbolTable.occupiedSymbols)
        result2 =  any(symbol in goofyList for symbol in SymbolTable.notLSymbols)
        #       ['-',  'E',   'D',   'L',   'N',   'nE',  'nD', 'nL', 'nN', 'nED', 'nEL', 'nEN','nDL','nDN','nLN','nDLN','nELN','nEDN','nEDL', 'x']
        lista = [True, False, False, False, False, False, True, True, True, False, False, False, True, True, True, True, False, False, False, False]
        cond = not(result1 or result2)
        if cond:
            return True
        else:
            return False

    def checkN(self, sched, i, j):
        symbol = sched.scheduleList[i]
        goofyList = [sched.scheduleList[i]]
        result1 =  any(symbol in goofyList for symbol in SymbolTable.occupiedSymbols)
        result2 =  any(symbol in goofyList for symbol in SymbolTable.notNSymbols)
        #       ['-',  'E',   'D',   'L',   'N',   'nE',  'nD', 'nL', 'nN', 'nED', 'nEL', 'nEN','nDL','nDN','nLN','nDLN','nELN','nEDN','nEDL', 'x']
        lista = [True, False, False, False, False, False, True, True, True, False, False, False, True, True, True, True, False, False, False, False]
        cond = not(result1 or result2)
        if cond:
            return True
        else:
            return False

    def checkEmpty(self, sched, i, j):
        if(i < 35 or j < 16):
            if(sched.scheduleList[i][j] == '-' or (sched.scheduleList[i][j] != 'E' and  sched.scheduleList[i][j] != 'D' and sched.scheduleList[i][j] != 'L' and sched.scheduleList[i][j] != 'N' and sched.scheduleList[i][j] != 'x' )):
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
            if sched.scheduleList[week * 7 + i][j] == 'E' or sched.scheduleList[week * 7 + i][j] == 'D' \
                    or sched.scheduleList[week * 7 + i][j] == 'L' or sched.scheduleList[week * 7 + i][j] == 'N':
                counter +=1
        return counter