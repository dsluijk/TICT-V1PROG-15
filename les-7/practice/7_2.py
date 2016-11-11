import datetime, csv, sys;

bestand = open('7_2.csv', 'a', newline='');
writer = csv.writer(bestand);

while True:
    naam = input("Wat is je achternaam? ");
    if(naam == 'einde'):
        bestand.close();
        sys.exit();
    voorl = input("Wat zijn je voorletters? ");
    gbdatum = input("Wat is je geboortedatum? ");
    email = input("Wat is je e-mail adres? ");
    datum = datetime.date.today().strftime('%a %d %b %Y at %H:%M');
    writer.writerow(['{};{};{};{};{}'.format(datum, voorl, naam, gbdatum, email)]);
