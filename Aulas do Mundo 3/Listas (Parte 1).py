# Alguns Comandos:
valores = list(range(11, 3, 5))
valores1 = [8, 2 , 5, 4, 9, 3, 0]

# Remove sempre o primeiro valor encontrado. Para remover mais utiliza-se os laços.
valores1.remove(5)

# Iria adicionar o 0 no lugar do 5.
valores1.insert(3, 0)

# Iria remover o terceiro valor (ou o último caso esteja vazio).
valores1.pop(3)

# Organiza os valores em ordem crescente.
valores1.sort()

# Organiza os valores em ordem decrescente.
valores1.sort(reverse = True)

# Quantidade de elementos da Lista.
len(valores1)

# Adiciona valores na lista.
valores1.append(2)

# Iria excluir o terceiro índice.
del valores1 [3]

# Exclui um item da lista pelo nome.
valores1.remove (8)

print(valores1)

#########################################################################################################

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(end='\n')

for contador, valor in enumerate(valores):
    print(f'Na posição {contador} encontrei o valor {valor}!')

print('\nFim da lista\n')

#########################################################################################################

a = [1, 2, 3]
b = a[:] # Cria uma cópia de a em b ao invés de juntar as duas.

#########################################################################################################
