
class Pointer:
    def __init__(self,adresse=None) -> None:
        self.adresse = adresse

    def get_adresse(self):
        return self.adresse
    
    def __str__(self) -> str:
        return str(self.adresse)