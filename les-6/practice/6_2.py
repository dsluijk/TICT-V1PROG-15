"""
Get tickers from a file

@param {String} Path to ticker file
@return {Dictionary} List of ticker symbols
"""
def ticker(path):
    tickerFile = open(path, 'r');
    rawTickers = tickerFile.readlines();
    tickerFile.close();
    dic = {};
    for tick in rawTickers:
        tick = tick.rstrip().split(':');
        dic[tick[0]] = tick[1];
    return dic;

print(ticker('./6_2.txt'));
