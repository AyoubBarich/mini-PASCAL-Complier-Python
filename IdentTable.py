from Pointer import Pointer
from Ident import Ident,variable,constant
from Tokens import TYPE_IDENT
NB_IDENT_MAX = 100


class IdentTable():
    # Functionallity :
    # creation of an entry if  new Ident
    # Search dor Ident
    # Entry :
    #     Ident and the information assciated wit this Ident
    #     number of info is depandent on type of Ident (CONST ,FUNC ,ETC)   

    def __init__(self) -> None:
        self.table_ident = {}

    def insert(self,ident :Ident):
        self.table_ident[ident.get_name()] = ident
    def search(self,ident:Ident):
        return self.table_ident.get(ident.get_name())


# table = IdentTable()
# x = constant('x',4)
# y = constant('y',6)
# table.insert(x)
# table.insert(y)
# table.insert(variable('z',x))
# table.insert(variable('w',y))


        
# print(table.search(x))