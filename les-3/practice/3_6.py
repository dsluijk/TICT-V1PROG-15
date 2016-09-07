"""
Change the content of a list

@param {List of Strings} letterList - List of letters
"""
def wijzigList(letterList=[]):
    letterList[0] = 'd';
    letterList[1] = 'e';
    letterList[2] = 'f';

"""
Change the content of a string

@param {String} letterString - A single char.
"""
def wijzigString(letterString=''):
    letterString = 'b';

lijst = ['a', 'b', 'c'];
print(lijst);
wijzigList(lijst);
print(lijst);

letter = 'a';
print(letter);
wijzigString(letter);
print(letter);
