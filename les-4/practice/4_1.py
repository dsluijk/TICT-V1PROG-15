"""
Convert celcius input to fahrenheit.

@param {Integer|Float} celsius - Input temperature.
@return {Integer|Float} the input in fahrenheit.
"""
def convert(celcius=0):
    return (celcius * 1.8) + 32;

"""
Print a formated list of celcius to fahrenheit
"""
def table():
    print('   F        C');
    i = -30;
    while i <= 40:
        spacing = '' if ((convert(i) <= -10) | (convert(i) >= 100)) else ' ';
        print(' ' + str(convert(i)) + spacing + '    ' + str(i));
        i = i + 10;

table();
