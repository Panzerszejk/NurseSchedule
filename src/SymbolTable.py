"""
This class may have strange form. It consists of 5 sets of symbols. First one consists all Symbols used by Generator class.
Further lists consist of the same symbols, after "blocking" certain symbol by Blocker class.
Blocker class uses certain symbols to prevent assigning certain shift types. Lists: eSymbolsBlocked, dSymbolsBlocked, lSymbolsBlocked and nSymbolsBlocked
are the basic symbol list with modified symbols to prevent assigning shifts determined by the first letter of their names.
example: eSymbolsBlocked is a symbols list that has symbols of preventing Early shifts whenever possible, so "-" -> "nE", "nL" -> "nEL" and so on.
"""


class SymbolTable:
    symbols = ["-", "E", "D", "L", "N", "nE", "nD", "nL", "nN", "nED", "nEL", "nEN", "nDL", "nDN", "nLN", "nDLN", \
               "nELN", "nEDN", "nEDL", "x"]  # all symbols
    emptySymbols = ["-", "nE", "nD", "nL", "nN", "nED", "nEL", "nEN", "nDL", "nDN", "nLN", "nDLN", "nELN", "nEDN", \
                    "nEDL"]  # symbols that can be overwritten
    occupiedSymbols = ["x", "E", "D", "L", "N"]  # symbols that cannot be overwritten

    notESymbols = ["nE", "nED", "nEL", "nEN", "nELN", "nEDN", "nEDL" ]  # symbols blocking Early shifts
    notDSymbols = ["nD", "nED", "nDL", "nDN", "nDLN", "nEDN", "nEDL"]  # symbols blocking Day shifts
    notLSymbols = ["nL", "nEL", "nDL", "nLN", "nDLN", "nELN", "nEDL"]  # symbols blocking Late shifts
    notNSymbols = ["nN", "nEN", "nDN", "nLN", "nDLN", "nELN", "nEDN"]  # symbols blocking Night shifts

    eSymbolsBlocked = ["nE", "E", "D", "L", "N", "nE", "nED", "nEL", "nEN", "nED", "nEL", \
                       "nEN", "nEDL", "nEDN", "nELN", "x", "nELN", "nEDN", "nEDL",
                       "x"]  # list of symbols after blocking Early shifts
    dSymbolsBlocked = ["nD", "E", "D", "L", "N", "nED", "nD", "nDL", "nDN", "nED", "nEDL", \
                       "nEDN", "nDL", "nDN", "nDLN", "nDLN", "x", "nEDN", "nEDL", "x"]
    lSymbolsBlocked = ["nL", "E", "D", "L", "N", "nEL", "nDL", "nL", "nLN", "nEDL", "nEL", \
                       "nELN", "nDL", "nDLN", "nLN", "nDLN", "nELN", "x", "nEDL", "x"]
    nSymbolsBlocked = ["nN", "E", "D", "L", "N", "nEN", "nDN", "nLN", "nN", "nEDN", "nELN", \
                       "nEN", "nDLN", "nDN", "nLN", "nDLN", "nELN", "nEDN", "x", "x"]
