destinationsFile = open('./final_destination.txt', 'r');
rawDestinations = destinationsFile.readlines();
destinationsFile.close();

canceledFile = open('./final_canceled.txt', 'r');
rawCanceled = canceledFile.readlines();
canceledFile.close();

canceledList = [];
final = [];

for canceled in rawCanceled:
    canceledList.append(canceled.rstrip().split(': ')[1]);

for destination in rawDestinations:
    cleanDestination = destination.rstrip().split(' - ')[1];
    if(canceledList.count(cleanDestination) == 0):
        final.append(destination);

finalFile = open('./final_final.txt', 'w');
finalFile.writelines(final);
finalFile.close();
