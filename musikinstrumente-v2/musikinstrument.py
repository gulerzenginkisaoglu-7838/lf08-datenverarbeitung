from abc import ABC, abstractmethod

class Musikinstrument:
    _modell = "unbekannt"
    _hersteller = "unbekannt"
    _preis = 0.0
    #-----------------------------------------------------------
    # Konstruktors der Klasse
    #-----------------------------------------------------------
    def __init__(self, modell = "unbekannt", hersteller = "unbekannt", preis = 0.0):
        self._modell = modell
        self._hersteller = hersteller
        self._preis = preis

    #-----------------------------------------------------------
    # Getter und Setter der Klasse
    #-----------------------------------------------------------
    def get_modell(self):
        return self.__modell

    def set_modell(self, value):
        self.__modell = value

    def get_hersteller(self):
        return self.__hersteller

    def set_hersteller(self, value):
        self.__hersteller = value

    def get_preis(self):
        return self.__preis

    def set_preis(self, value):
        self.__preis = value
    #------------------------------------------------------------
    # Methoden
    #-----------------------------------------------------------
    @abstractmethod
    def get_daten(self):
        pass




