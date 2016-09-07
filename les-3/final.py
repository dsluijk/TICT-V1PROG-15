"""
Calculate the standard price of a trip.

@param {Integer|Float} distance - Distance in kilometers.
@return {Float} Price of the trip.
"""
def standaardprijs(distance=0):
    if(distance < 0):
        return 0;

    if(distance > 50):
        return round((15 + (distance * 0.6)), 2);

    return round((distance * 0.8), 2);

"""
Calculates the actual trip price

@param {Integer} age - Age of the traveler.
@param {Boolean} weekendTrip - If the trip takes place in the weekend
@param {Integer|Float} distance - Distance in kilometers.
@return {Float} Price of the trip.
"""
def ritprijs(age=40, weekendTrip=False, distance=0):
    age = abs(age);
    price = standaardprijs(distance);

    if(age >= 12 & age < 65):
        if(weekendTrip):
            price = price * 0.6;
    else:
        if(weekendTrip):
            price = price * 0.65;
        else:
            price = price * 0.7;

    return round(price, 2);

testAges = [11, 12, 64, 65];
testDistance = [-10, 0, 5, 25, 49, 50, 150];

for a in testAges:
    for d in testDistance:
        print('For a person with a age of ' + str(a) + ' traveling in the weekend a distance of ' + str(d) + ' costs ' + str(ritprijs(a, True, d)) + ' euro.');
        print('For a person with a age of ' + str(a) + ' not traveling in the weekend a distance of ' + str(d) + ' costs ' + str(ritprijs(a, False, d)) + ' euro.');
