def ficha(jogador='<desconhecido>', gol=0):
    print(f'\nO jogador {jogador} fez {gol} gol(s) no campeonato.\n')


nome = str(input('\nNome do jogador: ')).title()
gols = str(input('Número de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(gol = gols)
else:
    ficha(nome, gols)
