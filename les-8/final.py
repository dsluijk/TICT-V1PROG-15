from xml.etree import ElementTree;

e = ElementTree.parse('./json.xml').getroot();

stations = [];

for child in e:
    station = {};
    station['code'] = child.find('Code').text;
    station['type'] = child.find('Type').text;
    station['land'] = child.find('Land').text;
    station['namen'] = [];
    for naam in child.find('Namen'):
        station['namen'].append(naam.text);
    station['synoniemen'] = [];
    for synoniem in child.find('Synoniemen'):
        station['synoniemen'].append(synoniem.text);
    stations.append(station);

print('Dit zijn de codes en types van de 4 stations:');
for station in stations:
    print(station['code'], '-', station['type']);

print('');
print('Dit zijn alle stations met één of meer synoniemen:');
for station in stations:
    if(len(station['synoniemen']) > 0):
        print(station['code'], '-', station['synoniemen']);

print('');
print('Dit is de lange naam van elk station:');
for station in stations:
    print(station['code'], '-', station['namen'][2]);
