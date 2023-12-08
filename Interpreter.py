
class Interpreter:
    def __init__(self,ASSM,PO_CODE,SOM_PLEX,MEM_VAR,PILEX,CO) -> None:
        self.ASSM = ASSM
        self.PO_CODE = PO_CODE
        self.SOM_PLEX = SOM_PLEX
        self.MEM_VAR = MEM_VAR
        self.PILEX = PILEX
        self.CO = CO

    def INTERPRET(self):
        
        while self.PO_CODE[self.CO] != 13:
            match self.PO_CODE[self.CO] :
                case 0:
                    self.ADDI()
                case 1:
                    self.SOUS()
                case 2:
                    self.MULT()
                case 3:
                    self.DIVI()
                case 4:
                    self.MOIN()
                case 5:
                    self.AFFE()
                case 6:
                    self.LIRE()
                case 7:
                    self.ECRL()
                case 8:
                    self.ECRE()
                case 9:
                    self.ECRC()
                case 11:
                    self.EMPI()
                case 12:
                    self.CONT()
                case 13:
                    self.STOP()
                case None:
                    break
        
                
    def ADDI(self):
        self.PILEX[self.SOM_PLEX-1] = self.PILEX[self.SOM_PLEX-1] + self.PILEX[self.SOM_PLEX]
        self.SOM_PLEX = self.SOM_PLEX-1
        self.CO = self.CO +1
    def SOUS(self):
        self.PILEX[self.SOM_PLEX-1] = self.PILEX[self.SOM_PLEX-1] - self.PILEX[self.SOM_PLEX]
        self.SOM_PLEX = self.SOM_PLEX-1
        self.CO = self.CO +1
    def MULT(self):
        self.PILEX[self.SOM_PLEX-1] = int(self.PILEX[self.SOM_PLEX-1]) * int(self.PILEX[self.SOM_PLEX])
        self.SOM_PLEX = self.SOM_PLEX-1
        self.CO = self.CO +1
    def DIVI(self):
        if self.PILEX[self.SOM_PLEX]==0:
            print("division par 0")
        self.PILEX[self.SOM_PLEX-1] = self.PILEX[self.SOM_PLEX-1] / self.PILEX[self.SOM_PLEX]
        self.SOM_PLEX = self.SOM_PLEX-1
        self.CO = self.CO +1
    def MOIN(self):
        self.PILEX[self.SOM_PLEX] = - self.PILEX[self.SOM_PLEX]
        self.CO = self.CO +1
    def AFFE(self):
        self.MEM_VAR[self.SOM_PLEX-1] = self.PILEX[self.SOM_PLEX]
        self.SOM_PLEX = self.SOM_PLEX-2
        self.CO = self.CO +1
    def LIRE(self):
        self.MEM_VAR[self.PILEX[self.SOM_PLEX]] = input()
        self.SOM_PLEX = self.SOM_PLEX-1
        self.CO = self.CO +1
    def ECRL(self):
        print('\n')
        self.CO = self.CO +1
    def ECRE(self):
        print(self.PILEX[self.SOM_PLEX])
        self.SOM_PLEX = self.SOM_PLEX -1
        self.CO = self.CO+1
    def ECRC(self):
        
        j =1
        ch = chr(self.PO_CODE[self.CO+j])
        text = ""
        while ch != chr(10):
            text+=ch 
            j+=1
            ch= chr(self.PO_CODE[self.CO+j])  
        self.CO = self.CO+1+j
        print(text)
    def EMPI(self):
        self.SOM_PLEX = self.SOM_PLEX +1
        self.PILEX[self.SOM_PLEX] = self.PO_CODE[self.CO +1]
        self.CO = self.CO +2
    def CONT(self):
        if isinstance(self.PILEX[self.SOM_PLEX],str):
            self.PILEX[self.SOM_PLEX] = self.MEM_VAR[self.PILEX[self.SOM_PLEX]].get_attribute()
            self.CO = self.CO +1
        else:
            self.PILEX[self.SOM_PLEX] = self.MEM_VAR[self.PILEX[self.SOM_PLEX]]
            self.CO = self.CO +1
    def STOP(self):
        exit(0)


