# ==============================================================================
# LEHRMATERIAL: OBJEKTORIENTIERTE PROGRAMMIERUNG (OOP) WITH PYTHON
# DERS NOTU: PYTHON İLE NESNE YÖNELİMLİ PROGRAMLAMA (OOP)
# ==============================================================================
# Dieses Dokument enthält alle wichtigen OOP-Konzepte für die IHK-Prüfung.
# Bu belge, IHK sınavı için gerekli tüm önemli OOP kavramlarını içermektedir.
# ==============================================================================

from abc import ABC, abstractmethod


# ==============================================================================
# EN: BASIC TERMS / DE: GRUNDBEGRIFFE / TR: TEMEL TERİMLER
# ==============================================================================
#
# 1. Klasse (Sınıf / Şablon):
#    - DE: Ein Bauplan oder eine Vorlage für Objekte (z. B. "Telefon").
#    - TR: Nesneler üretmek için kullanılan bir şablon veya plandır (Örn: "Telefon").
#
# 2. Objekt / Instanz (Nesne / Örnek):
#    - DE: Ein konkretes Exemplar, das nach dem Bauplan der Klasse erstellt wurde.
#    - TR: Sınıf şablonuna göre hafızada gerçekten üretilen somut varlıktır (Örn: "iPhone 15").
#
# 3. Konstruktor (Yapıcı Metot -> __init__):
#    - DE: Eine spezielle Methode, die automatisch aufgerufen wird, wenn ein neues
#          Objekt erstellt wird. Sie initialisiert die Attribute.
#    - TR: Yeni bir nesne üretildiğinde otomatik olarak ilk çalışan özel metottur.
#          Nesnenin ilk özelliklerini (niteliklerini) hafızada hazırlar.
#
# 4. self:
#    - DE: Repräsentiert das aktuelle Objekt selbst. Wird benötigt, um auf
#          Attribute und Methoden innerhalb der Klasse zuzugreifen.
#    - TR: O an üzerinde çalışılan nesnenin kendisini temsil eder. Sınıf içindeki
#          özelliklere ve metotlara ulaşmak için ilk parametre olmak zorundadır.
#
# 5. "bewegt sich" & "gebelaut":
#    - DE: Typische Methodennamen in Kursen. "bewegt sich" bedeutet "bewegt sich"
#          ve "gebelaut" bedeutet "gibt einen Ton von sich".
#    - TR: Kurslarda sıkça kullanılan metot (aksiyon) isimleridir. "bewegt sich"
#          hareket etme eylemini, "gebelaut" ise ses çıkarma eylemini simüle eder.


# ==============================================================================
# DIE 4 GRUNDPRINZIPIEN DER OOP / OOP'NİN 4 TEMEL İLKESİ
# ==============================================================================

# ------------------------------------------------------------------------------
# PRINZIP 1: ABSTRAKTION (Soyutlama / Şablon Oluşturma)
# ------------------------------------------------------------------------------
# DE: Erstellt einen reinen Bauplan (Schnittstelle) ohne Details. Zwingt
#     Unterklassen dazu, bestimmte Methoden zu implementieren.
# TR: Detayları gizleyip sadece zorunlu kuralları içeren bir şablon sunar.
#     Alt sınıfları bu metotları yazmaya zorlar. Sınıf (ABC) sınıfından türetilir.

class TelefonSablonu(ABC):

    @abstractmethod
    def kilit_ac(self):
        # DE: Kein Inhalt (pass), da es nur eine Pflichtregel (Schnittstelle) ist.
        # TR: Gövdesi boştur (pass), çünkü bu sadece alt sınıflar için zorunlu bir kuraldır.
        pass


# ------------------------------------------------------------------------------
# PRINZIP 2: VERERBUNG (Kalıtım / Miras Alma)
# ------------------------------------------------------------------------------
# DE: Eine Unterklasse (Kindklasse) erbt alle Eigenschaften und Methoden einer
#     Basisklasse (Elternklasse). Verhindert Code-Duplizierung.
# TR: Bir alt sınıfın, üst sınıfın özellik ve metotlarını miras almasıdır.
#     Aynı kodların tekrar yazılmasını engeller. örn: IPhone(TelefonSablonu)

class IPhone(TelefonSablonu):

    # KONSURKTOR / YAPICI METOT
    def __init__(self, model, pil_sagligi):
        self.model = model  # DE: Normales Attribut / TR: Normal nitelik

        # ----------------------------------------------------------------------
        # PRINZIP 3: DATENKAPSELUNG (Kapsülleme / Gizlilik)
        # ----------------------------------------------------------------------
        # DE: Schützt sensible Daten vor direktem Zugriff von außen.
        #     Wird in Python mit zwei Unterstrichen (__) deklariert (Private).
        # TR: Hassas verilerin dışarıdan doğrudan değiştirilmesini engeller.
        #     Python'da özelliğin önüne iki alt tire (__) konularak gizlenir (Private).

        self.__pil_sagligi = pil_sagligi  # Private Attribut

    # DE: Getter-Methode: Erlaubt den sicheren, kontrollierten Zugriff auf private Daten.
    # TR: Getter Metodu: Gizli veriyi dışarıya güvenli ve kontrollü gösterme butonudur.
    def get_pil_durumu(self):
        return f"Pil Sağlığı: %{self.__pil_sagligi}"

    # ----------------------------------------------------------------------
    # PRINZIP 4: POLYMORPHIE (Çok Biçimlilik)
    # ----------------------------------------------------------------------
    # DE: Dieselbe Methode (kilit_ac) verhält sich in verschiedenen Klassen anders.
    # TR: Aynı isimdeki metodun, farklı sınıflarda farklı sonuçlar üretmesidir.

    def kilit_ac(self):
        # DE: Überschreibt die abstrakte Methode für iPhone (FaceID)
        # TR: Soyut metodu iPhone'a göre ezer / doldurur (FaceID kullanır)
        return f"{self.model} -> [FaceID] Yüz tarandı ve kilit açıldı! 🔓"


# Ein weiteres Beispiel für Polymorphie (Samsung nutzt denselben Methodennamen)
class Samsung(TelefonSablonu):
    def __init__(self, model):
        self.model = model

    def kilit_ac(self):
        # DE: Überschreibt die abstrakte Methode für Samsung (Fingerprint)
        # TR: Soyut metodu Samsung'a göre ezer / doldurur (Parmak izi kullanır)
        return f"{self.model} -> [Fingerprint] Parmak izi okundu ve kilit açıldı! 🔓"


# ==============================================================================
# TEST-BEREICH / ÇALIŞTIRMA VE TEST ALANI
# ==============================================================================
if __name__ == '__main__':
    print("--- OOP DERST NOTLARI TESTI START ---")

    # 1. Objekte erstellen (Konstruktor wird aktiv)
    # 1. Nesneleri oluşturma (Konstruktor tetiklenir)
    mein_iphone = IPhone("iPhone 15", 98)
    mein_samsung = Samsung("Galaxy S24")

    print("\n[1] Kapsülleme (Datenkapselung) Testi:")
    # print(mein_iphone.__pil_sagligi)
    # DE: FEHLER! Direktzugriff blockiert, da die Daten gekapselt sind.
    # TR: HATA! Doğrudan erişim engellenmiştir çünkü veri kapsüllenmiştir.

    # DE: Zugriff erfolgt sicher über die Getter-Methode
    # TR: Erişim sadece güvenli Getter metodu üzerinden yapılabilir:
    print(mein_iphone.get_pil_durumu())

    print("\n[2] Çok Biçimlilik (Polymorphie) Testi:")
    # DE: Beide Objekte nutzen 'kilit_ac', aber reagieren unterschiedlich.
    # TR: İki nesne de 'kilit_ac' komutunu alır ama farklı davranış sergiler.
    print(mein_iphone.kilit_ac())
    print(mein_samsung.kilit_ac())

    print("\n--- TEST ENDE ---")

# ==============================================================================
# WICHTIGE IHK-PRÜFUNGSTIPPS (ZWEISPRACHIG) / ÖNEMLI IHK SINAV IPUÇLARI
# ==============================================================================
#
# DE: Warum nutzt man abstrakte Klassen?
#     - Sie dienen als reine Architektur-Baupläne. Man kann von ihnen KEINE direkten
#       Objekte erzeugen (z. B. `test = TelefonSablonu()` wirft einen Fehler).
#     - Sie garantieren, dass große Entwicklerteams sich al alle Regeln halten.
#
# TR: Soyut sınıflar (Abstract Classes) neden kullanılır?
#     - Tamamen yazılım mimarisini kurmak (plan oluşturmak) için kullanılırlar.
#       Bu sınıflardan doğrudan nesne ÜRETİLEMEZ (Hata verir).
#     - Büyük yazılımcı ekiplerinin standartlara ve kurallara uymasını garanti eder.
#
# DE: Was ist der Unterschied zwischen Overriding (Überschreiben) und Overloading (Überladen)?
#     - Overriding: Eine Unterklasse definiert eine geerbte Methode völlig neu (wie oben gezeigt).
#     - Overloading: Dieselbe Methode existiert mehrmals mit unterschiedlichen Parametern (In Python nicht nativ unterstützt).
#
# TR: Overriding (Ezme) ve Overloading (Aşırı Yükleme) farkı nedir?
#     - Overriding: Alt sınıfın, üst sınıftan miras aldığı metodu tamamen yeniden yazmasıdır (Yukarıdaki kilit_ac gibi).
#     - Overloading: Aynı isimdeki metodun farklı parametrelerle birden fazla kez tanımlanmasıdır (Python bunu doğrudan desteklemez).
#
# ==============================================================================






"""from abc import ABC, abstractmethod

# ==========================================
# 1. ADIM: SOYUTLAMA (Abstraksiyon)
# ==========================================
# Telefon adında genel, soyut bir kural şablonu (Schnittstelle) kuruyoruz.
class TelefonSablonu(ABC):

    @abstractmethod
    def kilit_ac(self):
        # İçini boş bırakıyoruz (pass). Çünkü bu sadece bir ZORUNLULUK KURALI.
        # Bu şablonu kullanan herkes bu fonksiyonu yazmak ZORUNDA.
        pass

# ==========================================
# 2. ADIM: KALITIM (Vererbung) & KAPSÜLLEME (Kapselung)
# ==========================================
# iPhone sınıfını oluşturuyoruz ve yukarıdaki şablondan miras (Kalıtım) alıyoruz.
class IPhone(TelefonSablonu):

    # KONSTRUKTOR: Telefon ilk üretildiğinde (doğduğunda) çalışan yer.
    def __init__(self, model, pil_sagligi):
        self.model = model                    # Normal, dışarıdan görünen özellik
        self.__pil_sagligi = pil_sagligi      # KAPSÜLLEME: Önüne __ koyduk, GİZLEDİK! (Private)

    # Kapsüllediğimiz (gizlediğimiz) veriyi güvenli bir butonla dışarı gösterme (Getter)
    def pil_durumunu_goster(self):
        return f"Pil Sağlığı: %{self.__pil_sagligi}"

    # ==========================================
    # 3. ADIM: ÇOK BİÇİMLİLİK (Polymorphie)
    # ==========================================
    # Şablondaki zorunlu 'kilit_ac' kuralını dolduruyoruz. iPhone kendine göre yapıyor.
    def kilit_ac(self):
        return f"{self.model} -> [FaceID] Yüz tarandı ve kilit açıldı! 🔓"


# Şimdi bir de Samsung sınıfı oluşturalım (O da şablondan miras alıyor)
class Samsung(TelefonSablonu):
    def __init__(self, model):
        self.model = model

    # Polymorphie: Aynı isimli metot, ama Samsung parmak izi kullanıyor!
    def kilit_ac(self):
        return f"{self.model} -> [Fingerprint] Parmak izi okundu ve kilit açıldı! 🔓"


# 1. Nesne oluşturma (Konstruktor tetiklenir)
telefon_1 = IPhone("iPhone 15", 98)
telefon_2 = Samsung("Galaxy S24")

# 2. Kapsülleme testi:
# print(telefon_1.__pil_sagligi) -> HATA VERİR! Doğrudan erişemezsin, kasa kapalı.
print(telefon_1.pil_durumunu_goster())  # Çıktı: Pil Sağlığı: %98 (Güvenli butonla eriştik)

# 3. Polymorphie (Çok Biçimlilik) testi:
print(telefon_1.kilit_ac()) # Çıktı: iPhone 15 -> [FaceID] Yüz tarandı...
print(telefon_2.kilit_ac()) # Çıktı: Galaxy S24 -> [Fingerprint] Parmak izi...
"""










































"""  i: int = 0 # Zuweisung
print(type(i))

einkaufsliste = ["gurke", 7, 8.0]
print(type(einkaufsliste))

def foo():  # Definition
    print(("Hallo"))
    j = 1000 # Definition, j ist nur in der Funktion gültig


def drucken(funktion, zahl):
    funktion("Hello Welt", zahl)

drucken(print, 4)
foo()
j = 5
print(j)
foo()

print("Hallo1")
print("Hallo1")  """
from mimetypes import init

"""class Currywurst:
    def __init__(self, geschmack_p):
    self.geschmack = geschmack_p
    self.laenge = self.laenge_p

sascha_currywurst = Currywurst()
daniel_currywurst = Currywurst()

print(type(sascha_currywurst))
print(type(daniel_currywurs """
"""class Wasserfahrzeug:

    def __init__(self, p_name, ):
        self.name = p_name

wasserfahrzeug1 = Wasserfahrzeug()
wasserfahrzeug1.schwimmen()"""

""" class Konto():
    def __init__(self, p_kontostand):
        self.kontostand = p_kontostand

    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag

    def auszahlen(self, betrag):
        self.kontostand = self.kontostand - betrag


konto1 = Konto(100)
print(konto1.kontostand)

konto1.einzahlen(50)
print(konto1.kontostand)

konto1.auszahlen(30)
print(konto1.kontostand)"""






















