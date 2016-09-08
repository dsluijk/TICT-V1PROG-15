textFile = open('./4_2-file.txt', 'r');
users = textFile.readlines();
textFile.close();

for user in users:
    user = user.split(', ');
    print(user[1].rstrip() + ' heeft kaartnummer: ' + user[0]);
