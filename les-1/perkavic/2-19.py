# Imports
import math;

# Helper functions
def calcLengthFromCenter(x, y):
    return math.sqrt(math.pow(x, 2)+ math.pow(y, 2));

# A
print(calcLengthFromCenter(0, 0) < 10);

# B
print(calcLengthFromCenter(10, 10) < 10);

# C
print(calcLengthFromCenter(6, 6) < 10);

# D
print(calcLengthFromCenter(7, 8) < 10);
