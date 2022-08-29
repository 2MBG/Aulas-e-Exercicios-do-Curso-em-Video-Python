from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''\n\033[33;1mSua jogada:\033[m

[ \033[34;1m0\033[m ] Pedra
[ \033[34;1m1\033[m ] Papel
[ \033[34;1m2\033[m ] Tesoura\n''')

jogador = int(input('\033[33mDigite o número da opção desejada:\033[m '))
print(end='\n')
while not jogador == 0 and not jogador == 1 and not jogador == 2:
    jogador = int(input('\033[31;1mOpção inválida.\033[33mDigite o número da opção desejada:\033[m '))

print('\n\033[36;1mJO\033[m\n')
sleep(0.7)
print('\033[36;1mKEN\033[m\n')
sleep(0.7)
print('\033[36;1mPO!\033[m\n')

print('-' * 20)
print(f'\033[35;1mJogador:\033[m {itens[jogador]}\n')
print(f'\033[35;1mComputador:\033[m {itens[computador]}')
print('-' * 20)

if computador == 0: # Pedra
    if jogador == 0:
        print('\n\033[33mDeu empate!\033[m\n')
    elif jogador == 1:
        print('\n\033[32mO jogador venceu!\033[m\n')
    elif jogador == 2:
        print('\n\033[37;1mO computador venceu!\033[m\n')

elif computador == 1: # Papel
    if jogador == 0:
        print('\n\033[37;1mO computador venceu!\033[m\n')
    elif jogador == 1:
        print('\n\033[33mDeu empate!\033[m\n')
    elif jogador == 2:
        print('\n\033[32mO jogador venceu!\033[m\n')

elif computador == 2: # Tesoura
    if jogador == 0:
        print('\n\033[32mO jogador venceu!\033[m\n')
    elif jogador == 1:
        print('\n\033[37;1mO computador venceu!\033[m\n')
    elif jogador == 2:
        print('\n\033[33mDeu empate!\033[m\n')
