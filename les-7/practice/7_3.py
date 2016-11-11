import csv;

csvfile = open('7_3.csv', 'r', newline='');
reader = csv.reader(csvfile);

top = ['', '00-00-0000', 0];
for regel in reader:
    gamer = regel[0].strip().split(';');
    if(int(gamer[2]) > int(top[2])):
        top = gamer;

print('De hoogste score is: ' + str(top[2]) + ' op ' + str(top[1]) + ' behaald door ' + str(top[0]));
