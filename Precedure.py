
from Tokens import TYPE_IDENT,TYPE
from ErrorHandler import RaiseError
import SyntaxAnalayser
from UNILEX_TYPE import UNILEX_TYPE
from Ident import constant , variable,Ident
from IdentTable import IdentTable
from CodeGenrator import CodeGenrator
from Interpreter import Interpreter
import copy

TAILLE_MAX_MEM = 100
global UNILEX 
class Procedure:
    global UNILEX
    def __init__(self,path) -> None:
        self.path = path
        self.SyntaxAnalayser=SyntaxAnalayser
        self.Analyzed_Program=self.SyntaxAnalayser.SyntaxAnalayser(path)
        self.UNILEX_LIST=self.SyntaxAnalayser.UNILEX
        self.identTable = IdentTable()
        self.NOMBRE_LIST = self.Analyzed_Program.NOMBER_LIST
        self.CHAINE_LIST = self.Analyzed_Program.CHAINE_LIST
        self.PO_CODE = [None]*TAILLE_MAX_MEM
        self.CO = 0
        self.PILOP = [None]*TAILLE_MAX_MEM
        self.SOM_PILOP = 0
        self.ASSM_FILE_PATH = ""
        self.PILEX = [None]*TAILLE_MAX_MEM
        self.SOM_PILEX = -1
        self.PO_CODE_COPY = None

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
                    #print(self.LECTURE(unit))
            
    
    def INSTRUCTION(self):
        global UNILEX
        return self.AFFECTATION() or self.LECTURE() or self.ECRITURE() or self.BLOC()
    

    def AFFECTATION(self):
        global UNILEX
        #print(UNILEX)
        if UNILEX.type == TYPE.ident:
            self.PO_CODE[self.CO] = 11
            self.PO_CODE[self.CO+1] = self.identTable.table_ident[UNILEX.name].get_attribute()
            self.CO = self.CO+2
            if self.IS_DECLARED(UNILEX.name):
                UNILEX = self.ANALEX(UNILEX)
                #print("debug41",UNILEX)
                if (UNILEX.type == TYPE.aff):
                    UNILEX = self.ANALEX(UNILEX)
                    #print("debug47",UNILEX)
                    if self.EXP():
                        self.PO_CODE[self.CO] = 5
                        self.CO +=1 
                        return True
                    else : 
                        return False
                else :
                    RaiseError.SYNTAX_ERR_AFF_SYMB()
                    return False
            else: 
                RaiseError.SYNTAX_ERR_AFF_VAR_NOT_DECLARED()
                return False
        else:
            RaiseError.SYNTAX_ERR_AFF_IDENT()
            return False
    



    def LECTURE(self):
        global UNILEX
        fin = None
        erreur = None
        #print("debug61",UNILEX)
        if ((UNILEX.type == TYPE.motcle) and (UNILEX.name == "LIRE" )):
            #print(UNILEX)
            
            UNILEX = self.ANALEX(UNILEX)
            if (UNILEX.type == TYPE.parouv):
                #print(UNILEX)
                UNILEX = self.ANALEX(UNILEX)
                #print(UNILEX)
                if (UNILEX.type == TYPE.ident):
                    self.PO_CODE[self.CO] = 11
                    self.PO_CODE[self.CO+1] = self.identTable.table_ident[UNILEX.name].get_attribute()
                    self.PO_CODE[self.CO+2] = 6
                    self.CO +=3 
                    UNILEX = self.ANALEX(UNILEX)
                    #print("here",UNILEX)
                    fin = False
                    erreur = False

                    if (UNILEX.type == TYPE.virg):
                            
                        UNILEX = self.ANALEX(UNILEX)
                            
                        if (UNILEX.type == TYPE.ident ):
                                self.PO_CODE[self.CO] = 11
                                self.PO_CODE[self.CO+1] = self.identTable.table_ident[UNILEX.name].get_attribute()
                                self.PO_CODE[self.CO+2] = 6
                                self.CO +=3 
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
                                    self.PO_CODE[self.CO] = 11
                                    self.PO_CODE[self.CO+1] = self.identTable.table_ident[UNILEX.name].get_attribute()
                                    self.PO_CODE[self.CO+2] = 6
                                    self.CO +=3 
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
                        #print("please", UNILEX)
                        return True
                    
                    else:
                        #print(UNILEX)
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

    def ECRITURE(self):
        global UNILEX
        fin = None 
        erreur = None
        if (UNILEX.name=="ECRIRE") :
            #print("debug132",UNILEX)
            
            UNILEX = self.ANALEX(UNILEX)
            if (UNILEX.type == TYPE.parouv ):
                #print("debug135",UNILEX)
                UNILEX = self.ANALEX(UNILEX)
                erreur = False
                Presence_exp = False
                if (self.ECR_EXP()):
                    Presence_exp =True
                    #print("debug139",UNILEX)
                    #print(self.UNILEX_LIST)
                    UNILEX = self.ANALEX(UNILEX)
                    
                    #print("debug140",UNILEX)
                    fin = False
                    if(UNILEX.type == TYPE.virg):
                        UNILEX = self.ANALEX(UNILEX)
                        erreur = not self.ECR_EXP()
                        #print("debug151",UNILEX,erreur)
                        if(erreur):
                            fin = True
                        if (UNILEX.type == TYPE.parenf):
                            fin = True
                    else:
                        fin = True
                    while not fin:
                            
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
                    if not Presence_exp :
                        self.PO_CODE[self.CO] = 7
                        self.CO += 1 
                   
                    UNILEX = self.ANALEX(UNILEX)
                    #print("he",UNILEX)
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
        global UNILEX
        fin = None 
        erreur = None
        
        if (UNILEX==UNILEX_TYPE("DEBUT",TYPE.motcle)):
            
            UNILEX = self.ANALEX(UNILEX)
            
            if self.INSTRUCTION():
                #UNILEX = self.ANALEX(UNILEX)
                #print("debug189",UNILEX)
                fin = False
                erreur = False
                if (UNILEX.type == TYPE.ptvirg):
                    #print("debug193",UNILEX)
                    UNILEX = self.ANALEX(UNILEX)
                    #print("debug195",UNILEX)
                    erreur = not self.INSTRUCTION()
                    
                    #print("debug198",UNILEX)
                    if erreur :
                        fin = True
                else :
                    fin = True
                #print("debug203",fin)
                while not fin :
                    #print("debug209",UNILEX)
                    if (UNILEX.type == TYPE.ptvirg):
                        #print("debug212",UNILEX)
                        UNILEX = self.ANALEX(UNILEX)
                        #print("debug214",UNILEX)
                        erreur = not self.INSTRUCTION()
                        #print("debug215",UNILEX)
                        #UNILEX = self.ANALEX(UNILEX)
                        #print("debug217",UNILEX,erreur)
                        
                        if erreur :
                            fin = True
                    else :
                        fin = True

                if UNILEX == UNILEX_TYPE("FIN",TYPE.motcle):
                    #print("he")
                    return True
                elif erreur :
                    RaiseError.SYNTAX_ERR_BLOC_NOT_INST()
                    return False
                else :
                    RaiseError.SYNTAX_ERR_BLOC_PTVIRG()
                    return False
            else:
                RaiseError.SYNTAX_ERR_BLOC_NOT_INST()
                return False
        else:
            RaiseError.SYNTAX_ERR_BLOC_DEBUT_EXPECTED()
            return False
        
    def PROG(self):
        global UNILEX
        fin = None
        erreur1 = None
        erreur2 = None
        #print(UNILEX)
       
        if(UNILEX==UNILEX_TYPE("PROGRAMME",TYPE.motcle)):
            UNILEX = self.ANALEX(UNILEX)
            #print(UNILEX)
            if(UNILEX.type == TYPE.ident):
                UNILEX = self.ANALEX(UNILEX)
                #print(UNILEX)
                if(UNILEX.type == TYPE.ptvirg):
                    UNILEX = self.ANALEX(UNILEX)
                    #print(UNILEX)
                    erreur2 = not self.DECL_VAR()
                    erreur1 = not self.DECL_CONST() 
                    if self.BLOC():
                        UNILEX = self.ANALEX(UNILEX)
                        #print("HEHE")
                        if(UNILEX.type == TYPE.point):
                            self.PO_CODE[self.CO] = 13
                            self.CO +=1
                            return True
                        else:
                            RaiseError.SYNTAX_ERR_PROG_OPEN()
                            return False
                    else:
                        RaiseError.SYNTAX_ERR_PROG_BLOC_EXPECTED()
                else:
                    RaiseError.SYNTAX_ERR_PROG_PTVIRG()
                    return False
            else:
                RaiseError.SYNTAX_ERR_PROG_IDENT_EXPECTED()
                return False
        else:
            RaiseError.SYNATX_ERR_PROG_MISSIG_KEYWORD()
            return False

    def DECL_CONST(self):
        global UNILEX
        fin = None
        erreur1 = None
        erreur2 = None
        erreur3 = None
        nom_constante = ""
        #print(UNILEX)
        if (UNILEX == UNILEX_TYPE("CONST",TYPE.motcle)):
            UNILEX = self.ANALEX(UNILEX)
            #print("debug298",UNILEX)
            if(UNILEX.type == TYPE.ident):
                nom_constante = UNILEX.name
                UNILEX = self.ANALEX(UNILEX)
                #print("debug301",UNILEX)
                if(UNILEX.type == TYPE.eg):
                    UNILEX = self.ANALEX(UNILEX)
                    #print("debug304",UNILEX)
                    if(UNILEX.type == TYPE.ent)or (UNILEX.type == TYPE.ch):
                        if self.DEFINIR_CONSTANTE(nom_constante,UNILEX.type):
                            fin = False
                            erreur1 = False
                            erreur2 = False
                            erreur3 = False
                            UNILEX = self.ANALEX(UNILEX)
                            #print("debug311",UNILEX)

                            if (UNILEX.type == TYPE.virg):
                                UNILEX = self.ANALEX(UNILEX)
                                if(UNILEX.type == TYPE.ident):
                                    nom_constante = UNILEX.name
                                    UNILEX = self.ANALEX(UNILEX)
                                    if(UNILEX.type == TYPE.eg):
                                        UNILEX = self.ANALEX(UNILEX)
                                        if(UNILEX.type == TYPE.ent or UNILEX.type == TYPE.ch):
                                            if self.DEFINIR_CONSTANTE(nom_constante,UNILEX.type):
                                                UNILEX = self.ANALEX(UNILEX)
                                                fin = True 
                                            else:
                                                fin = False
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
                                        nom_constante = UNILEX.name
                                        UNILEX = self.ANALEX(UNILEX)
                                        if(UNILEX.type == TYPE.eg):
                                            UNILEX = self.ANALEX(UNILEX)
                                            if(UNILEX.type == TYPE.ent or UNILEX.type == TYPE.ch):
                                                if self.DEFINIR_CONSTANTE(nom_constante,UNILEX.type):
                                                    UNILEX = self.ANALEX(UNILEX)
                                                    fin = True 
                                                else :
                                                   fin = False
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
            #print("debug387", UNILEX)
            RaiseError.SYNTAX_ERR_CONST_MOTCLE_EXPECTED()
            return False

    def DECL_VAR(self):
        global UNILEX
        fin = None
        erreur1= None
        nom_var =""
        #print(UNILEX)
        
        if (UNILEX == UNILEX_TYPE("VAR", TYPE.motcle)):

            UNILEX = self.ANALEX(UNILEX)
            #print("debug386",UNILEX)
            if(UNILEX.type == TYPE.ident):
                nom_var = UNILEX.name
                if(self.DEFINIR_VAR(nom_var,UNILEX.type)):
                    fin = False
                    erreur1 = False
                    UNILEX = self.ANALEX(UNILEX)

                    if(UNILEX.type == TYPE.virg):
                        fin = False
                        erreur1 = False
                        
                        UNILEX = self.ANALEX(UNILEX)
                        #print("debug414",UNILEX)
                        if(UNILEX.type == TYPE.ident):
                            nom_var = UNILEX.name
                            #print("debug417",UNILEX)
                            if(self.DEFINIR_VAR(nom_var,UNILEX.type)):
                                #print("debug418",UNILEX)
                                UNILEX = self.ANALEX(UNILEX)
                                fin = False
                            else:
                                fin = True
                        else:
                            #print("debug425",UNILEX)
                            fin = True
                            erreur1 = True
                    else :
                        fin = True
                        
                    while not fin:
                        #print("debug432",UNILEX)
                        if UNILEX.type == TYPE.virg:
                            UNILEX = self.ANALEX(UNILEX)
                            if(UNILEX.type == TYPE.ident):
                                nom_var = UNILEX.name
                                if(self.DEFINIR_VAR(nom_var,UNILEX.type)):
                                    UNILEX = self.ANALEX(UNILEX)
                                    fin = False
                                else:
                                    fin = True
                            else:
                                fin = True
                                erreur1 = True
                        else:
                            UNILEX = self.ANALEX(UNILEX)
                            
                            fin = True
                
                if erreur1:
                    RaiseError.SYNTAX_ERR_VAR_IDENT_EXPECTED()
                    return False
                elif UNILEX.type == TYPE.ptvirg:
                    

                    UNILEX = self.ANALEX(UNILEX)
                    #print("debug398",UNILEX,"DECL_VAR finished")
                    #print(UNILEX)
                    return True
                else:
                    RaiseError.SYNTAX_ERR_VAR_OPENFIELD()
                    return False
            else:
                RaiseError.SYNTAX_ERR_IDENT_EXPECTED()
                return False
        else:
            RaiseError.SYNTAX_ERR_VAR_INCORRECT()
            return False



        
    def ECR_EXP(self):
        global UNILEX
        if self.EXP() :
            self.PO_CODE[self.CO] = 8
            self.CO += 1
            return True
        elif UNILEX.type == TYPE.ch:
            #print(self.CO,"*********")
            self.PO_CODE[self.CO] = 9
            self.CO +=1
            #print(self.PO_CODE,"*********")
            for i in range(len(UNILEX.name)):
                self.PO_CODE[self.CO+i] = ord(UNILEX.name[i])
            self.PO_CODE[self.CO+len(UNILEX.name)] = 10
            self.CO = self.CO+len(UNILEX.name)+1
            #print("debug421",UNILEX)
            
            return True
        
        else :
            return False
        
    def EXP(self):
        global UNILEX
        if self.TERME():
            #print("debug432",UNILEX)
            if self.SUITE_TERME():
                #UNILEX = self.ANALEX(UNILEX)
                return True
            else:
                
                return True
        else:
            #print("debug437",UNILEX)
            return False
    
    def SUITE_TERME(self):
        global UNILEX
        if UNILEX.type  == TYPE.parenf:
            #print("debug454",UNILEX)
            return False
        if self.OP_BIN():
            #print("****************",self.PO_CODE)

            UNILEX = self.ANALEX(UNILEX)

            #print("debug444",UNILEX)
            if self.EXP():
                self.PO_CODE[self.CO]=self.PILOP[self.SOM_PILOP]
                self.SOM_PILOP = self.SOM_PILOP-1
                self.CO = self.CO+1 
                    
                #UNILEX = self.ANALEX(UNILEX)
                #print("debug455",UNILEX)
                return True
            else:
                RaiseError.SYNTAX_ERR_SUITE_TERME_EXP_EXPEDCTED()
                return False
        else:
            return True
        

    def TERME(self):
        global UNILEX
        #print("debug447",UNILEX)
        if (UNILEX.type == TYPE.ent ):
            self.PO_CODE[self.CO] = 11
            self.PO_CODE[self.CO+1] = int(UNILEX.name)
            self.CO = self.CO+2 
            UNILEX = self.ANALEX(UNILEX)
            return True
        if UNILEX.type == TYPE.ident:
            self.PO_CODE[self.CO] = 11
            self.PO_CODE[self.CO+1] = self.identTable.table_ident[UNILEX.name].get_attribute()
            self.PO_CODE[self.CO+2] = 12
            self.CO = self.CO+3 
            UNILEX = self.ANALEX(UNILEX)

            #print("debug453",UNILEX)
            return True
        if UNILEX.type == TYPE.moins:
            self.SOM_PILOP =  self.SOM_PILOP +1
            self.PILOP[self.SOM_PILOP] = 1 
            UNILEX = self.ANALEX(UNILEX)
            if (self.TERME()):
                UNILEX = self.ANALEX(UNILEX)
                return True
            else:
                RaiseError.SYNTAX_ERR_TERME_TERME_EXPECTED()
                return False
        
        if UNILEX.type == TYPE.parouv:
            UNILEX = self.ANALEX(UNILEX)
            if self.EXP():
                UNILEX = self.ANALEX(UNILEX)
                if UNILEX.type  == TYPE.parenf:
                    UNILEX = self.ANALEX(UNILEX)
                    return True
                else:
                    RaiseError.SYNTAX_ERR_TERME_PAROUV_EXPECTED()
                    return False
            else:
                
                RaiseError.SYNTAX_ERR_TERME_EXP_INCORRECT()
                return False 
        RaiseError.SYNTAX_ERR_TERME_INCORRECT_FORMAT()
        return False
        

        
    def OP_BIN(self):
        global UNILEX
        #print("debug497",UNILEX)
        match UNILEX.type:
            case TYPE.plus:
                self.SOM_PILOP =  self.SOM_PILOP +1
                self.PILOP[self.SOM_PILOP] = 0
            case TYPE.moins:
                self.SOM_PILOP =  self.SOM_PILOP +1
                self.PILOP[self.SOM_PILOP] = 1 
            case TYPE.mult:
                self.SOM_PILOP =  self.SOM_PILOP +1
                self.PILOP[self.SOM_PILOP] = 2 
            case TYPE.divi:
                self.SOM_PILOP =  self.SOM_PILOP +1
                self.PILOP[self.SOM_PILOP] = 3 
        return UNILEX.type == TYPE.plus or UNILEX.type == TYPE.moins or UNILEX.type == TYPE.mult or UNILEX.type == TYPE.divi




    def ANASYNT(self):
        global UNILEX
        UNILEX = self.UNILEX_LIST[0]
        if (self.PROG()):
            #print(self.NOMBRE_LIST)
            self.PO_CODE_COPY = copy.copy(self.PO_CODE)
            #print(self.PO_CODE)
            #print("Your programme is correct")
        else: 
             RaiseError.SYNTAX_ERR()


    def DEFINIR_CONSTANTE(self,nom ,type):
        if (self.identTable.search(Ident(nom))):
            RaiseError.DEFINIR_CONSTANTE_ALREADY_DEFINED()
            return False
        if type == TYPE.ent   :
            const = constant(nom,self.NOMBRE_LIST.pop(0))
            self.identTable.insert(const)
            return True
        if type == TYPE.ch :
            const = constant(nom,self.CHAINE_LIST.pop(0))
            self.identTable.insert(const)
            return True
    def DEFINIR_VAR(self, nom, type):
        #print("debug581",UNILEX)
        if(self.identTable.search(Ident(nom)) ):
            RaiseError.DEFINIR_VAR_ALREADY_DEFINED()
            return False
        if type == TYPE.ident:
            #print("debug585",UNILEX)
            var = variable(nom,len(self.identTable.MEME_VAR))
            self.identTable.insert(var)
            return True
        

        
    def IS_DECLARED(self,var):
        return self.identTable.contains(var)

    def GENERAT_CODE(self):
        genrator = CodeGenrator(self.identTable.MEME_VAR,self.PO_CODE,self.path)
        self.ASSM_FILE_PATH = f"{self.path}.cod"
        genrator.Gen()

    def EXECUTE(self):
        interpreter = Interpreter(self.ASSM_FILE_PATH,self.PO_CODE_COPY,self.SOM_PILEX,self.identTable.MEME_VAR,self.PILEX,0)
        interpreter.INTERPRET() 




    
# pro = Procedure("./Exemple2.pop")
# pro.ANASYNT()
# pro.GENERAT_CODE()
# pro.EXECUTE()
