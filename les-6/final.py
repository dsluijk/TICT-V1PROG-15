"""
Genereer code vanuit input

@param {String} Input string
@return {String} Output code
"""
def code(invoerstring = ''):
    encoded = '';
    for char in invoerstring:
        encoded = encoded + chr(ord(char)+3)
    return encoded;

print(code('Slechter dan ROT13, gebruik SHA512.'));

print('');
print('           | Georderned | Muteerbaar | Iterable | Dubbele waarde toegestaan');
print('-----------|------------|------------|----------|--------------------------');
print('Tuple      | Ja         | Nee        | Nee      | Ja');
print('Dictionary | Nee        | Ja         | Ja       | Nee');
print('Set        | Nee        | Ja         | Ja       | Ja');
print('List       | Nee        | Ja         | Ja       | Ja');
