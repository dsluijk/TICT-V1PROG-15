"""
Checks if a person is long enough for the python.

@param {Integer} length - Length of the person in centimeters
@return {Boolean} Returns true if the person is long enough
"""
def lang_genoeg(length=0):
    # Ternary operator, PLEASE python.
    if(length >= 120):
        return True;
    else:
        return False;

# "Unit tests"
print(lang_genoeg(60)); # Expect False
print(lang_genoeg(-124)); # Expect False
print(lang_genoeg(120)); # Expect True
print(lang_genoeg(182)); # Expect True
print(lang_genoeg(750)); # Expect True
