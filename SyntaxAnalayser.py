
from Reader import Reader
from ErrorHandler import RaiseError
from Tokens import TYPE
import Tokens
import string
from IdentTable import IdentTable
from Ident import Ident
from UNILEX_TYPE import UNILEX_TYPE
# CARLU=''
NUM_LIGNE=0
INDEX = 0
NOMBRE = None
MAXINT= 32767
CHAINE=''
MAXLENSTR=50
LEN_MAX_IDENT = 20
TestPathComments = "./CommentsTest.txt"
TestPathNumberTest = "./NumberTest.txt"
TestPathProgram = "./ExampleProg.txt"
ALPHABET = list(string.ascii_letters)
TABLE_MOTS_RESERVES = ['CONST' ,'DEBUT','ECRIRE','FIN' ,'LIRE','PROGRAMME','VAR']
LAST_MOTCLE =""
TABLE_IDENT = IdentTable()
UNILEX= []

class SyntaxAnalayser():

    def __init__(self,program_file_path):
        
        
        self.prog = Reader(program_file_path).content
        while not self.end():
            self.CHAINE = CHAINE
            self.LIRE_CAR()
            
            
        
        

    # def INSERER_MOTS_RESERVES(self, mot):
    #     global TABLE_DE_MOTS_RESERVES
    #     TABLE_DE_MOTS_RESERVES.append(mot)
    #     return TABLE_DE_MOTS_RESERVES.sort()

    # def INITIALISER(self,program_file_path):
    #     global TABLE_DE_MOTS_RESERVES
    #     global NUM_LIGNE
    #     self.prog = Reader(program_file_path).content
    #     NUM_LIGNE = 0
    #     self.INSERER_MOTS_RESERVES('PROGRAMME')
    #     self.INSERER_MOTS_RESERVES('DEBUT')
    #     self.INSERER_MOTS_RESERVES('FIN')
    #     self.INSERER_MOTS_RESERVES('CONST')
    #     self.INSERER_MOTS_RESERVES('VAR')
    #     self.INSERER_MOTS_RESERVES('ECRIRE')
    #     self.INSERER_MOTS_RESERVES('LIRE')
    #     while True :
    #         self.LIRE_CAR()

    # def TERMINER(self):
    #     return self.folder.close() 




    def LIRE_CAR(self):
        # global CARLU
        global NUM_LIGNE
        global INDEX
        global UNILEX
        
       
        if  not self.end():

            match self.prog[INDEX]:
                
                case '\n':
                    
                    NUM_LIGNE+=1
                    print(f" -> sauter ligne \nNombre de ligne: {NUM_LIGNE}")
                    INDEX += 1 
                case ' '|'\t':
                    self.SAUTER_SEPARATEUR()
                case '{':
                    self.SAUTER_COMMENT()
                    #print(self.prog[INDEX])
                case '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9':
                    self.RECO_ENTIER()
                    UNILEX.append(UNILEX_TYPE(NOMBRE,TYPE.ent) )
                    #print("Nombre",NOMBRE)
                case '\'':
                    self.RECO_CHAINE()
                    UNILEX.append(UNILEX_TYPE(CHAINE,TYPE.ch))
                case _:
                    if self.prog[INDEX] in ALPHABET:
                        self.RECO_IDENT_OU_MOT_RESERVE()
                    self.RECO_SYMB()
                    INDEX+=1
            # if not self.end():
            #     print(self.prog[INDEX])
            # else:
            #     RaiseError.END_OF_FILE()
        else:
            RaiseError.END_OF_FILE()


    def is_seperateur(self):
         global INDEX
         return (self.prog[INDEX] == ' ' )| (self.prog[INDEX] == '\t') | (self.prog[INDEX] == '\n')
    # def is_comment(self):
    #     return self.prog[INDEX] == '{'
 
    def SAUTER_SEPARATEUR(self):
        global INDEX
        print(f"{self.prog[INDEX]} -> Separateur")
        while not self.end() and self.is_seperateur() :
            INDEX+=1
        
    
    def SAUTER_COMMENT(self):
        global INDEX 
        COMMENT =""
        counter = 1
        while counter != 0 :  

            if not self.end():
                COMMENT += self.prog[INDEX]
                #print('dans commentaire',self.prog[INDEX])
                #print(counter)
                if self.prog[INDEX] == '{':
                    counter += 1      
                elif self.prog[INDEX] == '}':
                    counter -= 2
                INDEX += 1
        print(f"Sauter Commentaire : {COMMENT}")
            
        if(counter != 0 ):
            RaiseError.OPEN_COMMENT_FIELD()


    def is_entier(self) : 
        return (self.prog[INDEX] == '0') |( self.prog[INDEX] == '1') | (self.prog[INDEX] == '2')| (self.prog[INDEX] == '3') | (self.prog[INDEX] == '4') | (self.prog[INDEX] == '5') | (self.prog[INDEX] == '6') | (self.prog[INDEX] == '7') | (self.prog[INDEX] == '8')| (self.prog[INDEX] == '9') 

    def end(self):
        global CHAINE
        return CHAINE=='FIN' 

    def RECO_ENTIER(self) :
        global INDEX
        global NOMBRE
        x =''
        while (self.is_entier()) :            
            if not self.end():
                x+=self.prog[INDEX]
                INDEX += 1 
            else:
                RaiseError.END_OF_FILE()
        NOMBRE = int(x)
        if NOMBRE > MAXINT:
            RaiseError.MAXINT()
        print(f"{NOMBRE} -> ent")
        return TYPE.ent 
    

    def RECO_CHAINE(self):
        global INDEX
        global CHAINE
        INDEX+=1
        #CHAINE = self.prog[INDEX]
        CHAINE =""

        while not self.end():
            #print("CHAINE",CHAINE)
            #print("Prog",self.prog[INDEX])
            while self.prog[INDEX] =="\'":
                INDEX+=1
            
                if self.prog[INDEX] !="\'":
                    #print("RETT")
                    if len(CHAINE)> MAXLENSTR:
                        RaiseError.MAX_LEN_STR_REACHED()
                    else:
                        print(f"{CHAINE} -> ch")
                        return TYPE.ch
                INDEX+=1
                break
                
            while self.prog[INDEX] !="\'":
                CHAINE += self.prog[INDEX]
                INDEX +=1

                


    def RECO_IDENT_OU_MOT_RESERVE(self):
        global INDEX
        global CHAINE
        global LAST_MOTCLE
        global UNILEX
        CHAINE = ""
        def EST_MOT_RESERVE(mot):
            return mot in TABLE_MOTS_RESERVES

        while self.condition():
            CHAINE += (self.prog[INDEX]).upper()
            INDEX +=1 
        if len(CHAINE)> LEN_MAX_IDENT:
            RaiseError.MAX_LEN_IDENT_REACHED()

        if EST_MOT_RESERVE(CHAINE):
            print(f"{CHAINE} -> motcle")
            LAST_MOTCLE = CHAINE
            UNILEX.append(UNILEX_TYPE(CHAINE,TYPE.motcle))
            return TYPE.motcle
        TABLE_IDENT.insert(Ident(CHAINE),Tokens.get_type_from_chaine(LAST_MOTCLE))
        print(f"{CHAINE} -> indent")
        print(f"Current Table Ident : {TABLE_IDENT}")
        UNILEX.append(UNILEX_TYPE(CHAINE,TYPE.ident))
        return TYPE.ident
        
    def condition(self):
        global INDEX
        global ALPHABET
        return self.prog[INDEX] in ALPHABET or self.is_entier() or self.prog[INDEX] == "_"

        
        




    # def RECO_CHAINE(self):
    #     CHAINE =''
    #     global INDEX
    
    #     while not self.end():
    #         CHAINE+=self.prog[INDEX]
    #         INDEX+=1
    #         while not self.end() and self.prog[INDEX] != '\'':
    #             CHAINE+=self.prog[INDEX]
    #             INDEX+=1
    #         if not self.end():
    #             if self.prog[INDEX] == '\'':
    #                 if not self.end() and self.prog[INDEX+1] != '\'':
    #                     INDEX+=1
    #                     CHAINE+=self.prog[INDEX]
    #                     break
    #                 elif not self.end() :
    #                     CHAINE += '\"'
    #                     INDEX+=1


    #     if len(CHAINE) > MAXLENSTR:
    #         print('CHAINE = ',CHAINE)
    #         RaiseError.MAX_LEN_STR_REACHED()
    #     print('CHAINE = ',CHAINE)
    #     return (TYPE.ch , CHAINE)         break
        



                
    def RECO_SYMB(self):
        global INDEX
        global UNILEX
        match self.prog[INDEX]:
            case ';' :
                print(f"{self.prog[INDEX]} -> ptvirg")
                UNILEX.append(UNILEX_TYPE(self.prog[INDEX], TYPE.ptvirg))
                return TYPE.ptvirg
            case '.':
                print(f"{self.prog[INDEX]} -> point")
                UNILEX.append(UNILEX_TYPE(self.prog[INDEX],TYPE.point))
                return TYPE.point
            case '(':
                print(f"{self.prog[INDEX]} -> parouv")
                UNILEX.append(UNILEX_TYPE(self.prog[INDEX],TYPE.parouv))
                return TYPE.parouv
            case ')':
                print(f"{self.prog[INDEX]} -> parenf")
                UNILEX.append(UNILEX_TYPE(self.prog[INDEX],TYPE.parenf))
                return TYPE.parenf
            case '<':
                if self.prog[INDEX+1] == '=' : 
                    print(f"{self.prog[INDEX]} -> infe")
                    UNILEX.append(UNILEX_TYPE(">=",TYPE.infe))
                    INDEX+=1
                    return TYPE.infe
                elif self.prog[INDEX+1] == '>' :
                    print(f"{self.prog[INDEX]} -> diff")
                    UNILEX.append(UNILEX_TYPE("<>",TYPE.diff))
                    INDEX+=1
                    return TYPE.diff
                else :
                    print(f"{self.prog[INDEX]} -> inf")
                    UNILEX.append(UNILEX_TYPE(self.prog[INDEX], TYPE.inf))
                    return TYPE.inf
            case '>':
                if self.prog[INDEX+1] == '=' : 
                    print(f">= -> supe")
                    UNILEX.append(UNILEX_TYPE(">=",TYPE.supe))
                    INDEX +=1
                    return TYPE.supe
                else :
                    print(f"> -> sup")
                    UNILEX.append(UNILEX_TYPE(">" , TYPE.sup))
                    return TYPE.sup
            case '=':
                print(f"{self.prog[INDEX]} -> eg")
                UNILEX.append(UNILEX_TYPE(self.prog[INDEX],TYPE.eg))
                return TYPE.eg
            case '+':
                print(f"{self.prog[INDEX]} -> plus")
                UNILEX.append(UNILEX_TYPE(self.prog[INDEX],TYPE.plus))
                return TYPE.plus
            case '-':
                print(f"{self.prog[INDEX]} -> moins")
                UNILEX.append(UNILEX_TYPE(self.prog[INDEX],TYPE.moins))
                return TYPE.moins
            case '*':
                print(f"{self.prog[INDEX]} -> mult")
                UNILEX.append(UNILEX_TYPE(self.prog[INDEX],TYPE.mult))
                return TYPE.mult
            case '/':
                print(f"{self.prog[INDEX]} -> divi")
                UNILEX.append(UNILEX_TYPE(self.prog[INDEX],TYPE.divi))
                return TYPE.divi
            case ':':
                if self.prog[INDEX+1] == '=':
                    INDEX +=1
                    print(f":= -> aff")
                    UNILEX.append(UNILEX_TYPE(":=",TYPE.aff))
                    return TYPE.aff
                else :
                    print(f"{self.prog[INDEX]} -> deuxpts")
                    UNILEX.append(UNILEX_TYPE(self.prog[INDEX],TYPE.deuxpts))
                    return TYPE.deuxpts

    def ANALEX(self,unit:UNILEX_TYPE):
        global UNILEX 
        print(UNILEX)
        try:
            index_unit = UNILEX.index(unit)
            print(index_unit)
            UNILEX.pop(index_unit)
            return UNILEX[index_unit]
        except :
            RaiseError.UNILEX_NOT_FOUND()
            


       

           
        
                






######################Test#########################

