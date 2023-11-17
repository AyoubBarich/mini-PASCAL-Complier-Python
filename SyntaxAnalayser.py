
from Reader import Reader
from ErrorHandler import RaiseError
from Tokens import TYPE
# CARLU=''
NUM_LIGNE=0
INDEX = 0
NOMBRE = None
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
        
        if INDEX < len(self.prog):
            match self.prog[INDEX]:
                case '\n':
                    NUM_LIGNE+=1
                    
                case ' '|'    ':
                    self.SAUTER_SEPARATEUR()
                    
                case '{':
                    self.SAUTER_COMMENT()
                case '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9':
                    self.RECO_ENTIER()
                    print("Nombre",NOMBRE)

            if INDEX < len(self.prog):
                print(self.prog[INDEX])
            else:
                RaiseError.END_OF_FILE()
            INDEX += 1
        else:
            RaiseError.END_OF_FILE()


    def is_seperateur(self):
         global INDEX
         
         return (self.prog[INDEX] == ' ' )| (self.prog[INDEX] == '    ') | (self.prog[INDEX] == '\n')
    # def is_comment(self):
    #     return self.prog[INDEX] == '{'
 
    def SAUTER_SEPARATEUR(self):
        global INDEX
        while INDEX < len(self.prog) and self.is_seperateur() :
            INDEX+=1
    
    def SAUTER_COMMENT(self):
        global INDEX 
        counter = 1
        while counter != 0 :  
            if INDEX < len(self.prog):
                if self.prog[INDEX] == '{':
                    counter += 1      
                elif self.prog[INDEX] == '}':
                    counter -= 1
                INDEX += 1
            else:
                break;
        if (counter !=1):
            RaiseError.OPEN_COMMENT_FIELD()


    def is_entier(self) : 
        return (self.prog[INDEX] == '0') |( self.prog[INDEX] == '1') | (self.prog[INDEX] == '2')| (self.prog[INDEX] == '3') | (self.prog[INDEX] == '4') | (self.prog[INDEX] == '5') | (self.prog[INDEX] == '6') | (self.prog[INDEX] == '7') | (self.prog[INDEX] == '8')| (self.prog[INDEX] == '9') 

    def RECO_ENTIER(self) :
        global INDEX
        global NOMBRE
        x= [self.prog[INDEX]]
        while ( self.is_entier()) :
            print(x)
            INDEX += 1 
            if INDEX < len(self.prog):
                x.append(self.prog[INDEX])
            else:
                RaiseError.END_OF_FILE()
        
        return (TYPE.ent ,NOMBRE)


                
            
            

       

           
        
                






######################Test#########################


sy =SyntaxAnalayser(TestPathNumberTest)

