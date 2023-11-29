from Tokens import TYPE_IDENT, TYPE
from abc import ABCMeta ,abstractmethod

class Ident :
    __metaclass__ = ABCMeta
    @abstractmethod
    def get_attribute(self) : raise NotImplementedError
    @abstractmethod
    def get_type(self) : raise NotImplementedError
    @abstractmethod
    def get_name(self):
        return self.name
    def __init__(self,name) -> None:
        self.name = name

class variable(Ident):
    def __init__(self,name,adress="0X0000F") -> None:
        self.name = name
        self.adress = adress
    
    def get_attribute(self):
        return self.adress
    def get_type(self):
        return TYPE_IDENT.variable
    
class constant(Ident):
    def __init__(self, name , value) -> None:
        self.name = name
        self.value = value
    def get_attribute(self):
        return self.value
    def get_type(self):
        return TYPE_IDENT.constant
    
class programme(Ident):
    def __init__(self, name, block ) -> None:
        self.name = name
        self.block = block
    def get_attribute(self):
        return self.block
    def get_type(self):
        return TYPE_IDENT.PROG
# class function(Ident):
#     def __init__(self,name,nbparam) :
#         self.name = name
#         self.nbparam = nbparam
#     def get_attribute(self):
#         return self.nbparam
#     def get_type(self):
#         return 