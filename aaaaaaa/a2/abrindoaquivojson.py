import json

with open("pessoas.json", 'r') as pessoas:
    meu_objeto2 = json.load(pessoas)
    print(meu_objeto2)

    
print('Helow, word')