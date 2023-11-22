
from Reader import Reader
from ErrorHandler import RaiseError
from Tokens import TYPE
# CARLU=''
NUM_LIGNE=0
INDEX = 0
NOMBRE = None
MAXINT= 32767
CHAINE=''
MAXLENSTR=500000
TestPathComments = "./CommentsTest.txt"
TestPathNumberTest = "./NumberTest.txt"
TestPathProgram = "./ExampleProg.txt"
class SyntaxAnalayser():

    def __init__(self,program_file_path):
        self.prog = Reader(program_file_path).content
        while True:
            self.LIRE_CAR()




    def LIRE_CAR(self):
        # global CARLU
        global NUM_LIGNE
        global INDEX
        
        if not self.end():
            match self.prog[INDEX]:
                
                case '\n':
                    NUM_LIGNE+=1
                    INDEX += 1
                    
                case ' '|'    ':
                    self.SAUTER_SEPARATEUR()
                    
                case '{':
                    self.SAUTER_COMMENT()
                case '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9':
                    self.RECO_ENTIER()
                    print("Nombre",NOMBRE)
                case '\'':
                    self.RECO_CHAINE()
                case _:
                    print(self.prog[INDEX])
                    INDEX += 1
            

            if not self.end():
                print(self.prog[INDEX])
            else:
                RaiseError.END_OF_FILE()
        else:
            RaiseError.END_OF_FILE()


    def is_seperateur(self):
         global INDEX
         return (self.prog[INDEX] == ' ' )| (self.prog[INDEX] == '    ') | (self.prog[INDEX] == '\n')
    # def is_comment(self):
    #     return self.prog[INDEX] == '{'
 
    def SAUTER_SEPARATEUR(self):
        global INDEX
        while not self.end() and self.is_seperateur() :
            INDEX+=1
    
    def SAUTER_COMMENT(self):
        global INDEX 
        counter = 1
        while counter != 0 :  

            if not self.end():
                print('dans commentaire',self.prog[INDEX])
                print(counter)
                if self.prog[INDEX] == '{':
                    counter += 1      
                elif self.prog[INDEX] == '}':
                    counter -= 2
                INDEX += 1
            else:
                break
        if (counter !=0):
            RaiseError.OPEN_COMMENT_FIELD()


    def is_entier(self) : 
        return (self.prog[INDEX] == '0') |( self.prog[INDEX] == '1') | (self.prog[INDEX] == '2')| (self.prog[INDEX] == '3') | (self.prog[INDEX] == '4') | (self.prog[INDEX] == '5') | (self.prog[INDEX] == '6') | (self.prog[INDEX] == '7') | (self.prog[INDEX] == '8')| (self.prog[INDEX] == '9') 

    def end(self):
        return INDEX >= len(self.prog)  

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
        return (TYPE.ent ,NOMBRE)

    def RECO_CHAINE(self):
        CHAINE =""
        global INDEX
    
        while not self.end():
            
            CHAINE+=self.prog[INDEX]
            INDEX+=1
            while not self.end() and self.prog[INDEX] != '\'':
                CHAINE+=self.prog[INDEX]
                INDEX+=1
            if not self.end():
                if self.prog[INDEX] == '\'':
                    if not self.end() and self.prog[INDEX+1] != '\'':
                        INDEX+=1
                        CHAINE+=self.prog[INDEX]
                        if len(CHAINE) > MAXLENSTR:
                            print('CHAINE = ',CHAINE)
                            RaiseError.MAX_LEN_STR_REACHED()
                        else : 
                            print('CHAINE = ',CHAINE)
                            return (TYPE.ch , CHAINE)
                        break
                    elif not self.end() :
                        CHAINE += '\"'
                        INDEX+=1

        if len(CHAINE) > MAXLENSTR:
            print('CHAINE = ',CHAINE)
            RaiseError.MAX_LEN_STR_REACHED()
        else : 
            print('CHAINE = ',CHAINE)
        return (TYPE.ch , CHAINE)
    


    def RECO_SYMB(self):
        global INDEX
        if self.prog[INDEX] ==';' :
            return TYPE.ptvirg
        elif self.prog[INDEX] == '.':
            return TYPE.point
        elif self.prog[INDEX] == '(':
            return TYPE.parouv
        elif self.prog[INDEX] == ')':
            return TYPE.parfer
        elif self.prog[INDEX] == '<':
            if self.prog[INDEX+1] == '=' : 
                return TYPE.infe
            elif self.prog[INDEX+1] == '>' :
                return TYPE.diff
            else :
                return TYPE.inf
        elif self.prog[INDEX] == '>':
            if self.prog[INDEX+1] == '=' : 
                return TYPE.supe
            else :
                return TYPE.sup
        elif self.prog[INDEX] == '=':
            return TYPE.eg
        elif self.prog[INDEX] == '+':
            return TYPE.plus
        elif self.prog[INDEX] == '-':
            return TYPE.moins
        elif self.prog[INDEX] == '*':
            return TYPE.mult
        elif self.prog[INDEX] == '/':
            return TYPE.divi
        elif self.prog[INDEX] == ':':
            if self.prog[INDEX+1] == '=':
                return TYPE.aff
            else :
                return TYPE.deuxpts
        elif self.prog[INDEX] == 'supe':
            return 'point'
        elif self.prog[INDEX] == '.':
            return 'point'
        elif self.prog[INDEX] == '.':
            return 'point'
        





######################Test#########################


#sy = SyntaxAnalayser(TestPathProgram)
print(SyntaxAnalayser.RECO_CHAINE('Ayoub is incroyable'))
