# Imports
import random;

cijferICOR = random.randint(10, 100) / 10;
cijferPROG = random.randint(10, 100) / 10;
cijferCSN = random.randint(10, 100) / 10;

gemiddelde = round(((cijferICOR + cijferPROG + cijferCSN) / 3), 2);
beloning = round((gemiddelde * 30), 2);

overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van ' + str(beloning) + ' op!';
print(overzicht);
