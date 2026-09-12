from gebäude import Gebäude

class Wohnhaus(Gebäude):
    def __init__(self, adresse = "unbekannt", preis = 0.0, baujahr = 0, anzahlWohnungen = 0):
         super().__init__(adresse, preis, baujahr)
         self.__anzahlWohnungen = anzahlWohnungen

    def get_anzahlWohnungen(self):
        return self.__anzahlWohnungen

    def set_anzahlWohnungen(self, value):
        self.__anzahlWohnungen = value