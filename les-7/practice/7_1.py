try:
    kosten = 4356;
    aantal = int(input('Hoeveel personen gaan mee op reis?: '));
    if aantal < 0:
        raise ValueError('Negative');
    print(kosten / aantal);
except ValueError as e:
    if e.args[0] == 'Negative':
        print('Negatieve getallen zijn niet toegestaan!');
    else:
        print('Gebruik cijfers voor het invoeren van het aantal!');
except ZeroDivisionError:
    print('Delen door nul kan niet');
except:
    print('Onjuiste invoer!');
