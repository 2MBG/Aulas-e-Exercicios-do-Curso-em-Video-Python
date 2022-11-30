# Listas Compostas
dados = list()
pessoas = list()
dados.append('Marcelo')
dados.append(20)
pessoas.append(dados[:])
pessoas = [['Marcelo', 20], ['Maria', 19], ['João', 32]]
print(pessoas[0][0]) # Marcelo
print(pessoas[1][1]) # 19
print(pessoas[2][0]) # João
print(pessoas[1]) # ['Maria', 19]

print(end='\n')

########################################################
galera = [['Marcelo', 20], ['Maria', 19], ['João', 32]]

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print(end='\n')

########################################################
galera = list()
dados = list()
total_maior = 0
total_menor = 0

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear() # Apaga os dados cada vez que refaz o laço e impede que os dados sejam duplicados.

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1
    
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1

print(end='\n')
