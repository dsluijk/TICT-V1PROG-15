import math;

"""
Calculate the power of a list

@param {List of Integers} groundNumbers - List of numbers to get the power of.
@return {List of Integers}
"""
def kwadraten_som(groundNumbers=[]):
    #Found the ternary operator, but it's horrible :(
    return sum(map((lambda x: (x **2 if x > 0 else 0)), groundNumbers));

# "Unit tests"
print(kwadraten_som([4, 5])); # Expect 41
print(kwadraten_som([4, 5, 3])); # Expect 5041
print(kwadraten_som([41414, 145, 3543, 123432])); # Expect 16963151894
print(kwadraten_som([4, 5, 3, -81])); # Expect 50
