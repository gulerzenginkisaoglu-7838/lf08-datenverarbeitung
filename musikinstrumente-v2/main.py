from gitarre import Gitarre
from saxophon import Saxophon

gitarre = Gitarre("PRS Custom 24 BW", "PRS", 3998.00) # Objekt anlegen
saxophon = Saxophon("Yahmaha YAS-280S", "Yamaha", 1179.00) # Objekt anlegen

def main():
    gitarre.set_größe("4/4")
    print(gitarre.get_daten())
    saxophon.set_stimmung("Eb")
    print(saxophon.get_daten())

main() # Ausführen des Programms