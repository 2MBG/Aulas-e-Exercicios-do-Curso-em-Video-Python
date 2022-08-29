num = int(input('\n\033[33;1mDigite um número inteiro:\033[m '))
total = 0

print(end='\n')

for contador in range(1, num + 1):
    if num % contador == 0:
        total += 1
        print('\033[32;1m', end= '')
    
    else:
        print('\033[31;1m', end='')
    
    print(f'{contador},', end=' ')

print('\033[37;1mFIM.\033[m')

print(f'\n\033[37;1mO número {num} foi divisível {total} vezes!\033[m\n')

if total == 2:
    print('Significa que ele \033[32mé\033[m um número PRIMO!\n')

else:
    print('Significa que ele \033[31mnão\033[m é um número PRIMO!\n')
