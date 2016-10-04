# Variable declaration
stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam',
            'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel',
            'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert',
            'Roermond', 'Sittard', 'Maastricht'];

"""
Inlezen van het begin station

@return {String} Een valide station
"""
def inlezen_beginpunt():
    while True:
        startStation = str(input('Wat is je beginstation: '));
        if(stations.count(startStation) > 0):
            return startStation;
        else:
            print('Fout: Dit station bestaat niet.');

"""
Inlezen van het eind station

@param {String} Het beginstation
@return {String} Een valide station
"""
def inlezen_eindpunt(startStation):
    while True:
        endStation = str(input('Wat is je endstation: '));
        if((stations.count(endStation) > 0) & (stations.index(startStation) < stations.index(endStation))):
            return endStation;
        else:
            print('Fout: Dit station bestaat niet of heeft een lagere index.');

"""
Print de stationnen.

@param {String} Het beginstation
@param {String} Het eindstation
@return {Void}
"""
def omroepen_reis(startStation='Schagen', eindstation='Maastricht'):
    startStationIndex = stations.index(startStation);
    endStationIndex = stations.index(eindstation);
    print('Het beginstation ' + startStation + ' is het ' + str(startStationIndex + 1) + 'e station in het traject.');
    print('Het endstation ' + eindstation + ' is het ' + str(endStationIndex + 1) + 'e station in het traject.');
    print('De afstand bedraagt ' + str(endStationIndex - startStationIndex) + ' station(s).');
    print('De prijs van het kaartje is ' + str((endStationIndex - startStationIndex) * 5) + ' euro.');
    print('');
    print('Jij stapt in de trein in: '+startStation);
    i = startStationIndex + 1;
    while(i < endStationIndex):
        print(' - ' + stations[i]);
        i = i + 1;
    print('Jij stapt uit de trein in: '+eindstation);

print('De volgende stations zijn beschikbaar: ' + ', '.join(stations));

begin = inlezen_beginpunt();
eind = inlezen_eindpunt(begin);
omroepen_reis(begin, eind);
