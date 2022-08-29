print('''\nDigite vários valores para descobrir quantos deles são pares e quantos são ímpares.
Digite 0 para encerrar.''')

número = 1
par = 0
ímpar = 0

print(end='\n')

while número != 0:
    número = int(input('Digite um valor: '))
    
    if número != 0:
        
        if número % 2 == 0:
            par = par + 1 # += 1
        
        else:
            ímpar = ímpar + 1 # += 1

print(f'\nVocê digitou {par} números pares e {ímpar} números ímpares!\n')
