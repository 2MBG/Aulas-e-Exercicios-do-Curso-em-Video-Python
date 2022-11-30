contador = 1
tupla = []

print(end='\n')

# Ler 4 valores pelo teclado:
while contador < 5:
    n = int(input(f'Digite um número ({contador}/4): '))
    tupla.append(n)
    contador += 1

# Guardá-los em uma tupla:
tupla = tuple(tupla)
print(f'\nTupla: {tupla}')

# a) Quantas vezes apareceu o valor 9:
nove = tupla.count(9)
if nove > 0:
    print(f'\nVezes em que o número 9 aparece: {nove}')
else:
    print('\nO número 9 não está presente.')

# b) Em que posição foi digitado o primeiro valor 3:
print(end='\n')

if 3 in tupla:
    print(f'O primeiro 3 está na posição: {tupla.index(3) + 1}.') # Index diz em qual posição algum caractere está.
else:
    print('O número 3 não está presente.')

# c) Quais foram os números pares:
pares = []

for num in tupla:
    if num % 2 == 0:
        pares.append(num)

print(f'\nNúmeros pares: {pares}\n')
