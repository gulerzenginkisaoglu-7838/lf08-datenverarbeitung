# DE: Importiert das eingebaute JSON-Modul, um JSON-Dateien verarbeiten zu können.
# TR: JSON dosyalarını işleyebilmek için yerleşik JSON modülünü içe aktarır.
import json

# DE: Definiert den relativen Pfad zur JSON-Datei im Unterordner.
# TR: Alt klasörde bulunan JSON dosyasının göreceli (relative) yolunu tanımlar.
dateipfad = 'Übung 07.07.2026/daten.json'

# DE: Try-Except-Block fängt potenzielle Fehler ab, falls die Datei fehlt.
# TR: Try-Except bloğu, dosya bulunamazsa oluşabilecek olası hataları yakalar.
try:
    # DE: Öffnet die Datei im Lesemodus ('r') mit UTF-8 Kodierung für Umlaute.
    # TR: Dosyayı okuma modunda ('r') ve özel karakterler için UTF-8 kodlamasıyla açar.
    with open(dateipfad, 'r', encoding='utf-8') as datei:
        # DE: Konvertiert den JSON-Inhalt in eine Python-Liste aus Dictionaries.
        # TR: JSON içeriğini bir Python Sözlük (Dictionary) listesine dönüştürür.
        daten = json.load(datei)

    # DE: Gibt eine einfache Trennlinie auf der Konsole aus.
    # TR: Konsola basit bir başlık ayırıcı çizgi yazdırır.
    print("--- JSON Dosyasından Okunan Veriler ---")

    # DE: Iteriert durch jede Person (Dictionary) in der geladenen Liste.
    # TR: Yüklenen listedeki her bir kişiyi (Sözlüğü) döngü ile tek tek döner.
    for person in daten:
        # DE: Gibt den Wert des Schlüssels 'name' aus.
        # TR: 'name' anahtarına karşılık gelen değeri ekrana yazdırır.
        print(f"Name: {person['name']}")

        # DE: Gibt den Wert des Schlüssels 'alter' aus.
        # TR: 'alter' anahtarına karşılık gelen değeri ekrana yazdırır.
        print(f"Alter: {person['alter']}")

        # DE: Gibt den Wert des Schlüssels 'beruf' aus.
        # TR: 'beruf' anahtarına karşılık gelen değeri ekrana yazdırır.
        print(f"Beruf: {person['beruf']}")

        # DE: Verbindet die Listenelemente der Interessen mit Komma und Leerzeichen.
        # TR: İlgi alanları listesindeki elemanları virgül ve boşluk ile birleştirir.
        interessen_str = ", ".join(person['interessen'])

        # DE: Gibt die formatierten Interessen als einen Textstring aus.
        # TR: Biçimlendirilmiş ilgi alanlarını tek bir metin olarak ekrana yazdırır.
        print(f"Interessen: {interessen_str}")

        # DE: Erzeugt eine visuelle Trennlinie (40 Bindestriche) nach jeder Person.
        # TR: Her kişiden sonra görsel bir ayırıcı çizgi (40 adet tire) oluşturur.
        print("-" * 40)

# DE: Wird ausgeführt, wenn der angegebene Pfad oder die Datei nicht existiert.
# TR: Belirtilen yol veya dosya mevcut olmadığında bu hata bloğu çalışır.
except FileNotFoundError:
    # DE: Gibt eine Fehlermeldung mit dem falschen Pfad aus.
    # TR: Hatalı dosya yolunu belirten bir hata mesajı yazdırır.
    print(f"Hata: '{dateipfad}' dosya yolu bulunamadı!")
