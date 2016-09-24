gaVerder = True;
getallenLijst = [];

while(gaVerder):
    getal = int(input('Geef een getal: '));
    if(getal == 0):
        gaVerder = False;
    else:
        getallenLijst.append(getal);

print('Er zijn', len(getallenLijst),'getallen ingevoerd, de som is:', sum(getallenLijst));
