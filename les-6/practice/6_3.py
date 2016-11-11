def namen(klas = {}):
    naam = input('Volgende naam: ');
    if(naam == ''):
        return end(klas);
    if naam not in klas:
        klas[naam] = 1;
    else:
        klas[naam] += 1;
    namen(klas);


def end(klas):
    for leerling in klas:
        print('Er zijn ' + str(klas[leerling]) + ' student(en) met de naam ' + leerling);

namen();
