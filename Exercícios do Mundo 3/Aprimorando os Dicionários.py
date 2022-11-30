time = []
jogador = {}
partidas = []

while True:
    print(end='\n')
    
    jogador.clear
    jogador['nome'] = str(input('Nome: ')).title()
    total_de_partidas = int(input('\nTotal de partidas jogadas: '))
    partidas.clear

    print(end='\n')

    for contador in range(0, total_de_partidas):
        partidas.append(int(input(f'Total de gols na {contador + 1}ª partida: ')))
    
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    time.append(jogador.copy())

    resposta = str(input('\nQuer continuar? [S/N] ')).upper()

    while not resposta == 'S' and not resposta == 'N':
        print(end='\n')
        resposta = str(input('\033[31mOpção inválida.\033[m Quer continuar? [S/N] ')).upper()

    if resposta == 'N':
        break

print(end='\n')
print('=' * 30)
print(f'{"APROVEITAMENTO DO JOGADOR":^30}')
print('=' * 30)
print(end='\n')

print('cód ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

for k, v in enumerate(time):
    print(f' {k:>2} ', end='')

    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    busca = int(input('\nMostar dados de qual jogador? (999 para encerrar) '))

    if busca == 999:
        break

    if busca >= len(time):
        print(f'\nNão possui nenhum jogador com o código {busca}')
    
    else:
        print(f'\nLEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:\n')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No {i+1}° jogo fez {g} gols.')
