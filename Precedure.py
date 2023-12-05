
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
                
            



    def BLOC(self,UNILEX:UNILEX_TYPE):
        fin = None 
        erreur = None
        if (UNILEX.equals(UNILEX_TYPE("DEBUT",TYPE.motcle))):
            UNILEX = self.ANALEX(UNILEX)
            if self.INSTRUCTION(UNILEX):
                UNILEX = self.ANALEX(UNILEX)
                fin = False
                erreur = False
                if (UNILEX.type == TYPE.ptvirg):
                    UNILEX = self.ANALEX(UNILEX)
                    erreur = not self.INSTRUCTION(UNILEX)
                    UNILEX = self.ANALEX(UNILEX)
                    if erreur :
                        fin = True
                else :
                    fin = True
                while not fin :
                    if (UNILEX.type == TYPE.ptvirg):
                        UNILEX = self.ANALEX(UNILEX)
                        erreur = not self.INSTRUCTION(UNILEX)
                        UNILEX = self.ANALEX(UNILEX)
                        if erreur :
                            fin = True
                    else :
                        fin = True
                if erreur :
                    RaiseError.SYNTAX_ERR_BLOC_NOT_INST()
                    return False
                elif UNILEX == UNILEX_TYPE("FIN",TYPE.motcle):
                    UNILEX = self.ANALEX(UNILEX)
                    return True
                else :
                    RaiseError.SYNTAX_ERR_BLOC_PTVIRG()
                    return False
            else:
                RaiseError.SYNTAX_ERR_BLOC_NOT_INST()
                return False
        else:
            RaiseError.SYNTAX_ERR_BLOC_DEBUT_EXPECTED()
            return False
        
    def PROG(self,UNILEX:UNILEX_TYPE):
        fin = None
        erreur1 = None
        erreur2 = None
        if(UNILEX==UNILEX_TYPE("PROGRAMME",TYPE.motcle)):
            UNILEX = self.ANALEX(UNILEX)
            if(UNILEX.type == TYPE.ident):
                UNILEX = self.ANALEX(UNILEX)
                if(UNILEX.type == TYPE.ptvirg):
                    UNILEX = self.ANALEX(UNILEX)
                    erreur1 = not self.DECL_CONST(UNILEX) 
                    erreur2 = not self.DECL_VAR(UNILEX)
                    self.BLOC(UNILEX)
                    if(UNILEX.type == TYPE.point):
                        return True
                    else:
                        RaiseError.SYNTAX_ERR_PROG_OPEN()
                        return False
                else:
                    RaiseError.SYNTAX_ERR_PROG_PTVIRG()
                    return False
            else:
                RaiseError.SYNTAX_ERR_PROG_IDENT_EXPECTED()
                return False
        else:
            RaiseError.SYNATX_ERR_PROG_MISSIG_KEYWORD()
            return False
    def DECL_CONST(self,UNILEX):
        fin = None
        erreur1 = None
        erreur2 = None
        erreur3 = None
        if (UNILEX == UNILEX_TYPE("CONST",TYPE.motcle)):
            UNILEX = self.ANALEX(UNILEX)
            if(UNILEX.type == TYPE.ident):
                UNILEX = self.ANALEX(UNILEX)
                if(UNILEX.type == TYPE.eg):
                    UNILEX = self.ANALEX(UNILEX)
                    if(UNILEX.type == TYPE.ent)or (UNILEX.type == TYPE.ch):
                        fin = False
                        erreur1 = False
                        erreur2 = False
                        erreur3 = False
                        UNILEX = self.ANALEX(UNILEX)

                        if (UNILEX.type == TYPE.virg):
                            UNILEX = self.ANALEX(UNILEX)
                            if(UNILEX.type == TYPE.ident):
                                UNILEX = self.ANALEX(UNILEX)
                                if(UNILEX.type == TYPE.eg):
                                    UNILEX = self.ANALEX(UNILEX)
                                    if(UNILEX.type == TYPE.ent or UNILEX.type == TYPE.ch):
                                        UNILEX = self.ANALEX(UNILEX)
                                        fin = True 
                                    else :
                                        erreur1 = True
                                else:
                                    erreur2 = True
                            else :
                                erreur3 =True
                        else:
                            fin = True
                        while not fin:
                            if (UNILEX.type == TYPE.virg):
                                UNILEX = self.ANALEX(UNILEX)
                                if(UNILEX.type == TYPE.ident):
                                    UNILEX = self.ANALEX(UNILEX)
                                    if(UNILEX.type == TYPE.eg):
                                        UNILEX = self.ANALEX(UNILEX)
                                        if(UNILEX.type == TYPE.ent or UNILEX.type == TYPE.ch):
                                            UNILEX = self.ANALEX(UNILEX)
                                            fin = True 
                                        else :
                                            erreur1 = True
                                    else:
                                        erreur2 = True
                                else :
                                    erreur3 =True
                            else:
                                fin = True
                        if erreur1:
                            RaiseError.SYNTAX_ERR_CONST_TYPE()
                            return False
                        if erreur2:
                            RaiseError.SYNTAX_ERR_CONST_EG_EXPECTED()
                            return False
                        if erreur3 :
                            RaiseError.SYNTAX_ERR_CONST_IDENT_EXPECTED()
                            return False
                        elif UNILEX.type == TYPE.ptvirg:
                            UNILEX = self.ANALEX(UNILEX)
                            return True
                        else:
                            RaiseError.SYNTAX_ERR_CONST_PTVIRG()
                            return False
                        
                    else:
                        RaiseError.SYNTAX_ERR_CONST_TYPE()
                        return False
                else:
                    RaiseError.SYNTAX_ERR_CONST_EG_EXPECTED()
                    return False
            else:
                RaiseError.SYNTAX_ERR_CONST_IDENT_EXPECTED()
                return False
        else:
            RaiseError.SYNTAX_ERR_CONST_MOTCLE_EXPECTED()
            return False

    def DECL_VAR():
        return
    def ECR_EXP():
        return
    def EXP():
        return
    def SUITE_TERME():
        return
    def TERME():
        return
    def OP_BIN():
        return







    

Procedure("./ExampleProg.txt").RUN()