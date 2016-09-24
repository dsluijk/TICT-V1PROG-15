# Variable declaration
age = int(input('Geef je leeftijd: '));
passport = str(input('Nederlands paspoort (Y/n): '));

if((age >= 18) & ((passport == 'y') | (passport == ''))):
    print('Gefeliciteerd, je mag stemmen!');
else:
    print('Helaas, je mag nog niet stemmen.');
