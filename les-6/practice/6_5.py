import random;

def monopolyworp(throws = 0):
    aantal = 0;
    x = random.randrange(1, 7);
    y = random.randrange(1, 7);
    if(x == y):
        if(throws == 2):
            return print(str(x) + ' + ' + str(y) + ' = (direct naar gevangenis)');
        else:
            print(str(x) + ' + ' + str(y) + ' = ' + str(x+y) + ' (dubbel)');
            return monopolyworp(throws+1);
    print(str(x) + ' + ' + str(y) + ' = ' + str(x+y));

monopolyworp();
