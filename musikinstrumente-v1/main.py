from musikinstrument import Musikinstrument

instrument =Musikinstrument("PRS Custom 24 BW", "PRS") # Objekt anlegen

def main():
    instrument.set_preis(3998.00)
    print(instrument.get_daten())

main() # Ausführen des Programms