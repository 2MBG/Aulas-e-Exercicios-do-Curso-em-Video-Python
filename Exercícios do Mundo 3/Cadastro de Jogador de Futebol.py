jogador = {}
total_de_gols = 0

while True:
    print(end='\n')
    jogador['nome'] = str(input('Nome: ')).title()
    jogador['partidas'] = int(input('Total de partidas jogadas: '))
    
    print(end='\n')

    for contador in range(0, jogador['partidas']):
        gols_partida = int(input(f'Total de gols na {contador + 1}ª partida: '))
        total_de_gols += gols_partida
    jogador['total_de_gols'] = total_de_gols

    print(end='\n')
    print('=' * 30)
    print(f'{"APROVEITAMENTO DO JOGADOR":^30}')
    print('=' * 30)
    print(end='\n')
    
    print(f'Nome: {jogador["nome"]}\n'
    f'Total de partidas: {jogador["partidas"]}\n'
    f'Total de gols no campeonato: {total_de_gols} gols\n')

    break
