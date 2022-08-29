# > aliha para a direita
# < alinha para a esquerda
# ^ centraliza
# Também é possível adicionar caracteres ao lado do nome como por exemplo {:+^20} que seria ++++++Marcelo+++++++

nome = str(input('\nQual é o seu nome? '))
print(f'\nPrazer em te conhecer!\n{nome:-^40}')
