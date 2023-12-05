
from Tokens import TYPE_IDENT,TYPE
from ErrorHandler import RaiseError
import SyntaxAnalayser
from UNILEX_TYPE import UNILEX_TYPE


class Procedure:
    def __init__(self,path) -> None:
        
        self.SyntaxAnalayser=SyntaxAnalayser
        self.Analyzed_Program=self.SyntaxAnalayser.SyntaxAnalayser(path)
        self.UNILEX_LIST=self.SyntaxAnalayser.UNILEX
        
    def ANALEX(self,Unit):
        try:
            index_unit = self.UNILEX_LIST.index(Unit)
            self.UNILEX_LIST.pop(index_unit)
            return self.UNILEX_LIST[index_unit]
        except :
            RaiseError.UNILEX_NOT_FOUND()
            



    def RUN(self):
        for unit in self.UNILEX_LIST:
            match unit:
                case UNILEX_TYPE("LIRE", TYPE.motcle):
                    print(self.LECTURE(unit))
            
    
    def INSTRUCTION(self,UNILEX):
        return self.AFFECTATION(UNILEX) or self.LECTURE(UNILEX) or self.ECRITURE(UNILEX) or self.BLOC(UNILEX)
    

    def AFFECTATION(self,UNILEX):
        if UNILEX.type == TYPE.ident:
            UNILEX = self.ANALEX(UNILEX)
            if (UNILEX.type == TYPE.aff):
                UNILEX = self.ANALEX(UNILEX)
                return self.EXP(UNILEX)
            else :
                RaiseError.SYNTAX_ERROR_AFF_SYMB()
                return False
        else:
            RaiseError.SYNTAX_ERROR_AFF_IDENT()
            return False
    



    def LECTURE(self,UNILEX):
        fin = None
        erreur = None
        
        if ((UNILEX.type == TYPE.motcle) and (UNILEX.name == "LIRE" )):
            print(UNILEX)
            
            UNILEX = self.ANALEX(UNILEX)
            if (UNILEX.type == TYPE.parouv):
                print(UNILEX)
                UNILEX = self.ANALEX(UNILEX)
                print(UNILEX)
                if (UNILEX.type == TYPE.ident):
                    print("here",UNILEX)
                    UNILEX = self.ANALEX(UNILEX)
                    print("here",UNILEX)
                    fin = False
                    erreur = False

                    if (UNILEX.type == TYPE.virg):
                            
                        UNILEX = self.ANALEX(UNILEX)
                            
                        if (UNILEX.type == TYPE.ident ):
                                UNILEX = self.ANALEX(UNILEX)
                        else : 
                            fin = True
                            erreur = False
                    else:
                        fin = True

                    while not fin:
                        if (UNILEX.type == TYPE.virg):
                                
                            UNILEX = self.ANALEX(UNILEX)
                            
                            if (UNILEX.type == TYPE.ident ):
                                    UNILEX = self.ANALEX(UNILEX)
                            else : 
                                fin = True
                                erreur = True
                        else:
                            fin = True
                    if erreur:
                        RaiseError.SYNTAX_ERR_LECT_IDENT()
                        return False 
                    
                    elif UNILEX.type == TYPE.parenf:
                        UNILEX = self.ANALEX(UNILEX)
                        return True
                    
                    else:
                        print(UNILEX)
                        RaiseError.SYNTAX_ERR_LECT_PARENF()
                        return False
                else:
                    RaiseError.SYNTAX_ERR_LECT_IDENT()
                    return False
            else:
                RaiseError.SYNTAX_ERR_LECT_PAROUV()
                return False
            
        else:
            RaiseError.SYNTAX_ERR_ERR_LIRE()
            return False

    def ECRITURE(self,UNILEX:UNILEX_TYPE):
        fin = None 
        erreur = None
        if(UNILEX.equals(UNILEX("ECRIRE",TYPE.motcle))):
            UNILEX = self.ANALEX()
            if (UNILEX.type == TYPE.parouv ):
                UNILEX = self.ANALEX(UNILEX)
                erreur = False
                if (self.ECR_EXP):
                    UNILEX = self.ANALEX(UNILEX)
                    fin = False
                    if(UNILEX.type == TYPE.virg):
                        UNILEX = self.ANALEX(UNILEX)
                        erreur = not self.ECR_EXP()
                        if(erreur):
                            fin = True
                    else:
                        fin = True
                while not fin:
                    if (self.ECR_EXP):
                        UNILEX = self.ANALEX(UNILEX)
                        fin = False
                        if(UNILEX.type == TYPE.virg):
                            UNILEX = self.ANALEX(UNILEX)
                            erreur = not self.ECR_EXP()
                            if(erreur):
                                fin = True
                        else:
                            fin = True
                if erreur:
                    RaiseError.SYNTAX_ERR_ECT_EXP()
                    return False
                elif UNILEX.type == TYPE.parenf :
                    UNILEX = self.ANALEX(UNILEX)
                    return True
                else:
                    RaiseError.SYNTAX_ERR_ECR_PARENF()
                    return False
            else:
                RaiseError.SYNTAX_ERR_ECR_PAROUV()
                return False
        else:
            RaiseError.SYNTAX_ERR_ECR_MOTCLE()
            return False
                
            



    def BLOC(self):
        return

    

Procedure("./ExampleProg.txt").RUN()