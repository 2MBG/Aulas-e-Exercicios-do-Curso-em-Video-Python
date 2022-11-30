# valores = []

# print(end='\n')

# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))

# print(f'\nO maior valor da lista é {max(valores)} e o menor {min(valores)}.\n')

lista = []
maior = 0
menor = 0

print(end='\n')

for c in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {c}: ')))

    if c == 0:
        maior = menor = lista[c]

    else:
        if lista[c] > maior:
            maior = lista[c]
        
        if lista[c] < menor:
            menor = lista[c]

print(f'\nVocê digitou os valores {lista}')

print(end='\n')

print(f'O maior valor digitado foi {maior} em ', end='') # Maior valor
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i} - ', end='')
print(';')

print(f'O menor valor digitado foi {menor} em ', end='') # Menor valor
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i} - ', end='')
print(';')

print(end='\n')
