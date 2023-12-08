from Pointer import Pointer
from Ident import Ident,variable,constant, programme
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
        self.MEME_VAR ={}

    def insert(self,ident :Ident):
            match ident.get_type():
                case TYPE_IDENT.variable:
                    self.add(ident)
                    self.MEME_VAR[ident.get_attribute()] = ident
                case TYPE_IDENT.constant:
                    self.add(ident)
                    self.MEME_VAR[ident.get_attribute()] = ident

            
            # case TYPE_IDENT.prog:
            #     self.add(programme(ident))

        
    def search(self,ident:Ident):
        return self.table_ident.get(ident.get_name())
    


    def add(self,ident:Ident):

        self.table_ident[ident.get_name()] = ident
       


    def __str__(self) -> str:
        res = ""
        for key in self.table_ident:
            res += key + " --> "
            res += str(self.table_ident[key].get_attribute())
            res += "\n"
        return res
            
    def contains(self,var):
        print(self.MEME_VAR)
        list_of_Names = [(varis.name)  for varis in self.MEME_VAR.values()]
        return var in list_of_Names

# table = IdentTable()
# x = constant('x',4)
# y = constant('y',6)
# table.insert(x)
# table.insert(y)
# table.insert(variable('z',x))
# table.insert(variable('w',y))


        
# print(table.search(x))