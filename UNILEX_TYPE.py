from Tokens import TYPE
from dataclasses import dataclass
@dataclass
class UNILEX_TYPE:
    name : str
    type : TYPE
    def __init__(self,name,type):
        self.name = name 
        self.type = type
    def __str__(self):
        
        return f"<name : {self.name} ,type : {self.type} >"
