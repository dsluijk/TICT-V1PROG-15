import csv;

csvfile = open('7_4.csv', 'r', newline='');
reader = csv.reader(csvfile);

row = 0;
totalArticles = 0;
priciest = [0, '', '', 0, 0.00];
lowStock = [0, '', '', 0, 0.00];

for regel in reader:
    row = row + 1;
    if(row == 1):
        continue;
    entity = regel[0].strip().split(';');
    if(float(entity[4]) > float(priciest[4])):
        priciest = entity;
    if((int(entity[3]) < int(lowStock[3])) | (lowStock[0] == 0)):
        lowStock = entity;
    totalArticles = totalArticles + int(entity[3]);

print('Het duurste artikel is {} en die kost {} Euro.'.format(str(priciest[2]), str(priciest[4])));
print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}.'.format(str(lowStock[3]), str(lowStock[0])));
print('In totaal hebben wij {} producten in ons magazijn liggen.'.format(str(totalArticles)));
