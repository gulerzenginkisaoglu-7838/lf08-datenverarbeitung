from musikinstrument import Musikinstrument

class Saxophon(Musikinstrument):
    def __init__(self, modell = "unbekannt", hersteller = "unbekannt", preis = 0.0, stimmung = "unbekannt"):
        super().__init__(modell, hersteller, preis)
        self.__stimmung = stimmung

    def get_stimmung(self):
        return self.__stimmung

    def set_stimmung(self, value):
        self.__stimmung = value

    def get_daten(self):
        daten = "Modell: " + self._modell + "\n" + \
                "Hersteller: " + self._hersteller + "\n" + \
                "Stimmung: " + self.__stimmung + "\n" + "Preis: " + \
                str(self._preis)
        return daten