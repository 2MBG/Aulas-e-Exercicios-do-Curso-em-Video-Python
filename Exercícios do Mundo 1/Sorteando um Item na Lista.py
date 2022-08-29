# Uma lista fica entre colchetes.

from random import choice

print('\n\033[33mDigite o nome de quatro alunos para descobrir' 
' quem irá apresentar o trabalho primeiro:\033[m')

aluno1 = str(input('\n\033[37;1mPrimeiro nome: \033[m'))
aluno2 = str(input('\033[37;1mSegundo nome: \033[m'))
aluno3 = str(input('\033[37;1mTerceiro nome: \033[m'))
aluno4 = str(input('\033[37;1mQuarto nome: \033[m'))

lista = [aluno1, aluno2, aluno3, aluno4]

sorteio = choice (lista)

print(f'\n\033[34;1m{sorteio}\033[m irá apresentar primeiro.\n')
