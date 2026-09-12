from musikinstrument import Musikinstrument

class Gitarre(Musikinstrument):
    def __init__(self, modell = "unbekannt", hersteller = "unbekannt", preis = 0.0, größe = "unbekannt"):
        super().__init__(modell, hersteller, preis)
        self.__größe = größe

    def get_größe(self):
        return self.__größe

    def set_größe(self, value):
        self.__größe = value

    def get_daten(self):
        daten = "Modell: " + self._modell + "\n" + \
                "Hersteller: " + self._hersteller + "\n" + \
                "Größe: " + self.__größe + "\n" + "Preis: " + \
                str(self._preis)
        return daten