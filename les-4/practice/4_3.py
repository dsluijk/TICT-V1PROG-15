textFile = open('./4_2-file.txt', 'r');
users = textFile.readlines();
textFile.close();

biggestCardNumber = [0, 0];
currentLine = 0;
for user in users:
    currentLine = currentLine + 1;
    user = user.split(', ');
    if(user[0] > biggestCardNumber[1]):
        biggestCardNumber[0] = currentLine;
        biggestCardNumber[1] = user[0];

print('Deze file telt ' + str(currentLine) + ' regels');
print('Het grootste kaartnummer is: ' + str(biggestCardNumber[1]) + ' en dat staat op regel ' + str(biggestCardNumber[0]));
