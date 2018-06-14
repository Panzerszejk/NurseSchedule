#from .Generator import Generator
from .SymbolTable import SymbolTable
from .Schedule import Schedule

class Blocker:
    def blockE(self, sched,i,j):
        symbol = str(sched.scheduleList[i][j])
        index = SymbolTable.symbols.index(symbol)
        sched.scheduleList[i][j] = SymbolTable.eSymbolsBlocked[index]
        return sched

    def blockD(self, sched,i,j):
        symbol = str(sched.scheduleList[i][j])
        index = SymbolTable.symbols.index(symbol)
        sched.scheduleList[i][j] = SymbolTable.dSymbolsBlocked[index]
        return sched

    def blockL(self, sched,i,j):
        symbol = str(sched.scheduleList[i][j])
        index = SymbolTable.symbols.index(symbol)
        sched.scheduleList[i][j] = SymbolTable.lSymbolsBlocked[index]
        return sched

    def blockN(self, sched,i,j):
        symbol = str(sched.scheduleList[i][j])
        index = SymbolTable.symbols.index(symbol)
        sched.scheduleList[i][j] = SymbolTable.nSymbolsBlocked[index]
        return sched

    def blockRow(self, sched, i, value):
        if value == "E":
            for j in range(16):
                sched = self.blockE(sched,i,j)
        if value == "D":
            for j in range(16):
                sched = self.blockD(sched,i,j)
        if value == "L":
            for j in range(16):
                sched = self.blockL(sched,i,j)
        if value == "N":
            for j in range(16):
                sched = self.blockN(sched,i,j)
        return sched

    def blockColumn(self, sched, j, value):
        if value == "E":
            for i in range(35):
                sched = self.blockE(sched,i,j)
        if value == "D":
            for i in range(35):
                sched = self.blockD(sched,i,j)
        if value == "L":
            for i in range(35):
                sched = self.blockL(sched,i,j)
        if value == "N":
            for i in range(35):
                sched = self.blockN(sched,i,j)
        return sched
