# Variable declaration
validStartStation = False;
validEndStation = False;
startStation = '';
endStation = '';
startStationIndex = 0;
endStationIndex = 0;
stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam',
            'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel',
            'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert',
            'Roermond', 'Sittard', 'Maastricht'];

print('De volgende stations zijn beschikbaar: ' + ', '.join(stations));

startStation = str(input('Wat is je beginstation: '));
if(stations.count(startStation) > 0):
    validStartStation = True;
else:
    print('Fout: Dit station bestaat niet, Schagen toegekend.');
    startStation = 'Schagen';

endStation = str(input('Wat is je endstation: '));
if(stations.count(endStation) > 0 & stations.index(startStation) < stations.index(endStation)):
    validEndStation = True;
else:
    print('Fout: Dit station bestaat niet of heeft een lagere index, Maastricht toegekend.');
    endStation = 'Maastricht';

startStationIndex = stations.index(startStation);
endStationIndex = stations.index(endStation);

print('Het beginstation ' + startStation + ' is het ' + str(startStationIndex + 1) + 'e station in het traject.');
print('Het endstation ' + endStation + ' is het ' + str(endStationIndex + 1) + 'e station in het traject.');
print('De afstand bedraagt ' + str(endStationIndex - startStationIndex) + ' station(s).');
print('De prijs van het kaartje is ' + str((endStationIndex - startStationIndex) * 5) + ' euro.');
print('');
print('Jij stapt in de trein in: '+startStation);

i = startStationIndex + 1;
while(i < endStationIndex):
    print(' - ' + stations[i]);
    i = i + 1;

print('Jij stapt uit de trein in: '+endStation);
