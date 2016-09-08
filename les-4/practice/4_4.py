import datetime;

def inputName():
    name = str(raw_input('Naam hardloper: '));
    if(name == ''):
        return;
    textFile = open('./4_4-file.txt', 'a');
    textFile.write(datetime.datetime.today().strftime("%a %d %b %Y, %H:%M:%S") + ', ' + name + '\n');
    textFile.close();
    return;

while True:
    inputName();
    if(str(raw_input('Wilt u nog een hardloper invoeren? (Y/n) ')) == 'n'):
        exit();
