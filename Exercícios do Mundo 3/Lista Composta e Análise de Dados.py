dados = []
dados2 = []

# Atribuição dos dados nas listas:
while True:
    print(end='\n')

    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso (em kg): ')))
    dados2.append(dados[:])
    dados.clear()

    pergunta = str(input('\nContinuar [S/N]? ')).upper()
    
    while not pergunta == 'S' and not pergunta == 'N':
        pergunta = str(input('\n\033[31mOpção inválida.\033[m Quer continuar [S/N]? ')).upper()
        
    if pergunta == 'N':
        break

print(f'\nTotal de pessoas cadastradas: {len(dados2)}') # Mais prático do que o usar o contador nesse caso.

pesos = list()  # Lista onde estarão apenas os pesos

for i in dados2:
    pesos.append(i[1])

pesos = sorted(pesos)  # Lista do maior e menor valor.

# 0 são os dados dos pesos
# 1 são os dados dos nomes

menor = pesos[0] # Pega o primeiro da ordem
maior = pesos[-1] # Pega o último da ordem

# Nomes das pessoas
mais_pesados = list()
menos_pesados = list()

for peso in dados2:  # Para cada lista dentro de dados2:
    
    if peso[1] == maior:  # Se o peso for igual a maior
        mais_pesados.append(peso[0])  # Adicione seu nome à lista
    
    if peso[1] == menor:  # Se o peso for igual a menor
        menos_pesados.append(peso[0])  # Adicione seu nome à lista

print(f'\nO maior peso foi de {maior}kg. Peso de {mais_pesados}.')
print(f'O menor peso foi de {menor}kg. Peso de {menos_pesados}.\n')
