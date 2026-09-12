import xml.etree.ElementTree as ET

baum = ET.parse('daten.xml')
wurzel = baum.getroot()

for person in wurzel.findall('person'):
    name = person.find('name').text
    alter = person.find('alter').text
    stadt = person.find('stadt').text
    print(f"Name: {name}, Alter: {alter}, Stadt: {stadt}")
