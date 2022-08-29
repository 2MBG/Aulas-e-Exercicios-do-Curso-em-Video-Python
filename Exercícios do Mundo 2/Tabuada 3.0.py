número = 0

print('\nDigite um número negativo para encerrar.')

print(end='\n')

while True:
    número = int(input('Quer ver a tabuada de qual número? '))

    if número < 0:
        break
    
    print(end='\n')
    
    print('-' * 25)

    for cont in range(1, 11):
        print(f"{número} x {cont} = {número * cont}")
    
    print('-' * 25)

    print(end='\n')

print('\nFim\n')
