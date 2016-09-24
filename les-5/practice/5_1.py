"""
Get the season which a month belongs to.

@param {Integer} month - Input month
@return {String} Season
"""
def seizoen(month=1):
    if((month < 1) | (month > 12)):
        return '';
    if((month >= 3) & (month <= 5)):
        return 'Lente';
    if((month > 5) & (month < 9)):
        return 'Zomer';
    if((month >= 9) & (month <= 11)):
        return 'Herfst';
    return 'Winter';

i = -1
while(i < 13):
    print(seizoen(i));
    i += 1;
