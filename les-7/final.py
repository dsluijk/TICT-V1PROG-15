import time, csv, random;

"""
Vraag de gebruiker om een keuze.

@return {Void}
"""
def ask():
    print('');
    print('Goededag, wat wilt u doen?');
    print('1) Ik wil een nieuwe kluis');
    print('2) Ik wil mijn kluis openen');
    print('3) Ik geef mijn kluis terug');
    print('4) Ik wil weten hoeveel kluizen nog vrij zijn');
    print('5) Ik wil stoppen');
    keuze = input('Wat is uw keuze? ');
    if(keuze.isdigit()):
        keuze = int(keuze);
    if(keuze == 1):
        safe = saveUser();
        if(safe):
            print('Uw kluisnummer is '+str(safe['safe'])+' met de code '+str(safe['code']));
        else:
            print('Sorry, er zijn geen kluizen beschikbaar. Probeer het later opnieuw.');
    elif(keuze == 2):
        code = input('Wat is uw code? ');
        if(code.isdigit()):
            code = int(code);
        else:
            print('Sorry, deze code is niet geldig.');
            time.sleep(3);
            ask();
        if(1000 <= code <= 9999):
            safe = getUser(code);
            if(safe):
                print('Kluisje '+safe+' is nu geopend.');
            else:
                print('Sorry, deze code is niet geldig.');
        else:
            print('Sorry, deze code is niet geldig.');
    elif(keuze == 3):
        print('Nog niet beschikbaar!')
    elif(keuze == 4):
        print('Er zijn nog '+str(getAvaliable())+' kluisjes vrij.')
    elif(keuze == 5):
        print('Tot ziens!');
        exit();
    else:
        print('Deze keuze is niet geldig. Probeer iets anders.');
    time.sleep(3);
    ask();

"""
Get a user

@param {Int} code: Code of the safe.
@return {String|Null} Number of the safe. Null if invalid.
"""
def getUser(code):
    csvfile = open('codes.csv', 'r', newline='');
    codeReader = csv.reader(csvfile);
    for row in codeReader:
        if(int(row[1]) == code):
            return row[0];
    return;


"""
Get the amount of avaliable safes

@return {Int} The amount of free safes.
"""
def getAvaliable():
    csvfile = open('codes.csv', 'r', newline='');
    codeReader = csv.reader(csvfile);
    unavaliable = 0;
    for row in codeReader:
        unavaliable = unavaliable + 1;
    return 12-unavaliable;

"""
Creates a new user a user to the file

@return {Object|Null} Object containing the code and the safe id. Null if no safe available.
"""
def saveUser():
    if(getAvaliable == 0):
        csvfile.close();
        return;
    csvfile = open('codes.csv', 'w', newline='');
    codeWriter = csv.writer(csvfile);
    code = getCode();
    codeWriter.writerow([avaliable[0], code]);
    csvfile.close();
    return {
        'code': code,
        'safe': avaliable[0]
    };

"""
Get random code

@return {Int} 4 number long code.
"""
def getCode():
    return random.randint(1000, 9999);

ask();
