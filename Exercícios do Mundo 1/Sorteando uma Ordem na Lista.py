# Uma lista fica entre colchetes.

from random import shuffle

print('\n\033[33mDigite o nome de quatro alunos para descobrir' 
' em que ordem eles irão apresentar o trabalho:\033[m')

aluno1 = str(input('\n\033[37;1mPrimeiro nome: \033[m'))
aluno2 = str(input('\033[37;1mSegundo nome: \033[m'))
aluno3 = str(input('\033[37;1mTerceiro nome: \033[m'))
aluno4 = str(input('\033[37;1mQuarto nome: \033[m'))

lista = [aluno1, aluno2, aluno3, aluno4]

shuffle (lista)

print(f'\nA ordem de apresentação é a seguinte: {lista}.\n')
