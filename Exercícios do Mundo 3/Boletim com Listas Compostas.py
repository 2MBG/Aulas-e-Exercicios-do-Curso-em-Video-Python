ficha = list()

print(end='\n')
print('=' * 30)
print(f'{"BOLETIM":^30}')
print('=' * 30)

while True:
    print(end='\n')
    nome = str(input('Nome: ')).title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('\nQuer continuar? [S/N] ')).upper()
    
    while not resposta == 'S' and not resposta == "N":
        resposta = str(input('\n\033[31mOpção inválida.Quer\033[m continuar? [S/N] ')).upper()
    
    if resposta == 'N':
        break

print(end='\n')

print('=' * 30)

print(f'{"Núm.":<4}{"Nome":^10}{"Média":>8}')

print('-' * 30)

for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:^10} {a[2]:>8.1f}')

print('=' * 30)

while True:
    option = int(input('\nMostrar as notas de qual aluno (999 para encerrar)? '))
    if option == 999:
        break
    
    if option <= len(ficha) - 1:
        print(f'\nNotas de {ficha[option][0]} são {ficha[option][1]}')
