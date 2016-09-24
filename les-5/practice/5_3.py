invoer = "5-9-7-1-7-8-3-2-4-8-7-9";

invoer = sorted(list(map((lambda x: int(x)), invoer.split('-'))), key=int);

print('Grootste getal:', invoer[len(invoer)-1], 'en Kleinste getal:', invoer[0]);
print('Aantal getallen:', len(invoer), 'en Som van de getallen: ', sum(invoer));
print('Gemiddelde:', float(sum(invoer)) / max(len(invoer), 1));
