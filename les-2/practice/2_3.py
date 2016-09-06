# Variable declaration
age = int(input('Geef je leeftijd: '));
passport = bool(input('Nederlands paspoort: '));

if(age > 18 & passport == True):
    print('Gefeliciteerd, je mag stemmen!');
else:
    print('Helaas, je mag nog niet stemmen.');
