lijst = input("Geef lijst met minimaal 10 strings, gescheiden met een komma en een spatie: ").split(', ');

if(len(lijst) < 10):
    print('Geef minstens een lijst met 10 strings in.');
    exit();

newLijst = [];

for lijstItem in lijst:
    if(len(lijstItem) == 4):
        newLijst.append(lijstItem);

print('De nieuw-gemaakte lijst met alle vier-letter strings is:', ', '.join(newLijst));
