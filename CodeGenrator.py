import os

class CodeGenrator:

    def __init__(self,MEM_VAR,PO_CODE,filename) -> None:
        self.filename = filename
        self.MEM_VAR = MEM_VAR
        self.codes = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.PO_CODE = PO_CODE
        self.file = open(f"./out/{filename}.cod","w") 
    
    def Gen(self):
        self.file.write(f"{len(self.MEM_VAR)} mot(s) réservé(s) pour les variables globales\n")
        while self.PO_CODE != []:
            match self.PO_CODE.pop(0) :
                case 0:
                    self.file.write("ADDI\n")
                case 1:
                    self.file.write("SOUS\n")
                case 2:
                    self.file.write("MULT\n")
                case 3:
                    self.file.write("DIVI\n")
                case 4:
                    self.file.write("MOIN\n")
                case 5:
                    self.file.write("AFFE\n")
                case 6:
                    self.file.write("LIRE\n")
                case 7:
                    self.file.write("ECRL\n")
                case 8:
                    self.file.write("ECRE\n")
                case 9:
                    line ="ECRC \'"
                    code = self.PO_CODE.pop(0)
                    while  code not in self.codes:
                        line+=chr(code)
                        code = self.PO_CODE.pop(0)
                    

                    line +="\'"
                    
                    self.file.write(line) 
                    self.file.write(" FINC\n")

                case 11:
                    line = "EMPI "
                    
                  
                    line += str(self.PO_CODE.pop(0))
                    
                
                    line += "\n"
                    self.file.write(line)

                case 12:
                    self.file.write("CONT\n")
                case 13:
                    self.file.write("STOP\n")
                    self.file.close()
                case None:
                    break
        os.system(f"cat ./out/{self.filename}.cod")
            
                