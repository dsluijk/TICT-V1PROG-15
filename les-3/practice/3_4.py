"""
Checks if new password is valid.

@param {String} oldPassword - Old password, before changing.
@param {String} newPassword - New password to validate.
@return {Boolean} True if the new password is valid, False if not.
"""
def new_password(oldPassword, newPassword): #The naming :/, also cammelCase plz
    containsDigit = False;

    if(oldPassword == newPassword):
        return False;

    if(len(newPassword) < 6):
        return False;

    for char in newPassword:
        if char.isdigit():
            containsDigit = True;
            break;

    if(containsDigit != True):
        return False;

    return True;

# "Unit tests"
print(newPassword('Password123', 'RtBQjLSj3dwaJAth64yUCi9A')); # Expect True
print(newPassword('Password123', 'WeakPassword123')); # Expect True
print(newPassword('Password123', 'YouNeverGuessThis987')); # Expect True
print(newPassword('Password123', 'Password123')); # Expect False
print(newPassword('Password123', 'short')); # Expect False
print(newPassword('Password123', 'WeakPassword')); # Expect False
