"""
Sums the parameters

@param {Integer|Float} getal1 - First digit of the sum.
@param {Integer|Float} getal2 - Second digit of the sum.
@param {Integer|Float} getal3 - Last digit of the sum.
@return {Integer|Float} Returns the sum
"""
def som(getal1=0, getal2=0, getal3=0):
    if((isinstance(getal1, int) != True) & (isinstance(getal1, float) != True)):
        getal1 = 0;
    if((isinstance(getal2, int) != True) & (isinstance(getal2, float) != True)):
        getal2 = 0;
    if((isinstance(getal3, int) != True) & (isinstance(getal3, float) != True)):
        getal3 = 0;

    return getal1 + getal2 + getal3;

# "Unit tests"
print(som(1, 2, 3)); # Expect 6
print(som(1, 0, 0)); # Expect 1
print(som(2.5, 3, 10)); # Expect 15.5
print(som(2.5, 3, 'derp')); # Expect 5.5
