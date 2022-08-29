num = int(input('\n\033[33mDigite um número inteiro para ver sua tabuada:\033[m '))

print(end='\n')

for contador in range(1, 11):
    print(f'{num} x {contador} = {num * contador}')                          

print(end='\n')
