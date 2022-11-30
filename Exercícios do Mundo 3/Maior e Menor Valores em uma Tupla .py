from random import randint

# Gerar 5 números e colocar numa tupla:
tupla = []
contador = 0

while contador < 5:
    tupla.append(randint(0, 100))
    contador += 1

tupla = tuple(tupla)

# Listagem de números gerados:
print('\nValores sorteados: ', end='')

for num in tupla:
    print(f'{num}, ', end='')

print('FIM.')

# Menor e maior valores:
menor = tupla[0]
maior = tupla[0]

for num in tupla:
    if num < menor:
        menor = num
    
    if num > maior:
        maior = num

print(f'\nMenor: {menor}')
print(f'Maior: {maior}\n')


'''from random import randint

números = (randint(1, 100),randint(1, 100),randint(1, 100),randint(1, 100),randint(1, 100))

print('OS valores sorteados foram: ', end='')

for n in números:
    print(f'{n} ', end='')

print(f'\nO maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')'''
