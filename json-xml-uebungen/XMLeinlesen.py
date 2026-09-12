import xml.etree.ElementTree as ET

# XML-Datei einlesen
tree = ET.parse("daten.xml")
root = tree.getroot()

for person in root.findall("person"):
    name = person.find("name").text
    alter = person.find("alter").text
    stadt = person.find("stadt").text
    print(f"Name: {name}, Alter: {alter}, Stadt: {stadt}")
