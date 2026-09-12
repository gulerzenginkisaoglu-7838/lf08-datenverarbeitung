from gebäude import Gebäude

class Lagerhalle(Gebäude):
    def __init__(self, adresse = "unbekannt", preis = 0.0, baujahr = 0, lagerfläche = 0.0):
        super().__init__(adresse, preis, baujahr)
        self.__lagerfläche = lagerfläche

    def get_lagerfläche(self):
        return self.__lagerfläche

    def set_lagerfläche(self, value):
        self.__lagerfläche = value