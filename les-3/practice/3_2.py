"""
Sums the given list.

@param {List of Integers} getallenlijst - List of integers to sum
@return {Integer} Returns the sum
"""
def som(list=[]):
    return sum(list);

# "Unit tests"
print(som([1, 2, 3])); # Expect 6
print(som([1, 0, 0])); # Expect 1
print(som([])); # Expect 0
print(som([345345345, 512451254, 6543646, 2345345, 234234523, 2342345, 23423452345])); # Expect 24526714803
print(som([-345345345, -512451254, -6543646, -2345345, -234234523, -2342345, -23423452345])); # Expect -24526714803
