cijfers = {
        "Dany": "10.0",
        "Caprice": "1.0",
        "Reiko": "5.2",
        "Willa": "7.6",
        "Royce": "9.5",
        "Yoshiko": "0.0",
        "Leroy": "-10.0",
        "Jeffery": "9.0",
        "Mina": "4.7",
        "Jacquelin": "2.7",
        "Rosaria": "8.9"
    };

for cijfer in cijfers:
    if(float(cijfers[cijfer]) > 9.0):
        print(cijfer+' had een score van '+cijfers[cijfer]);
