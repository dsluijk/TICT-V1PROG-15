ding = '';

while(len(ding) != 4):
    ding = str(input('Geef een string van vier letters: '));
    if(len(ding) != 4):
        print(ding, 'heeft', len(ding), 'letters.');

print('Inlezen van correcte string:', ding, 'is geslaagd');
