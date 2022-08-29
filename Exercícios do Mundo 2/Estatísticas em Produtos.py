soma = 0
mais_de_mil = 0
caro = 0
mais_caro = ''
barato = 0
mais_barato = ''

print(end='\n')

print('=' * 30)
print(f'\033[33;1m{"COMPRAS":^30}\033[m')
print('=' * 30)

print(end='\n')

while True:
    nome = str(input('Digite o nome do produto: ')).title()
    preço = float(input('Preço: R$'))

    if preço > 1000: # Valem mais de mil reais
        mais_de_mil += 1

    if barato == 0: # Produto mais barato
        barato = preço
        mais_barato = nome

    elif preço < barato:
        barato = preço
        mais_barato = nome

    if caro == 0: # Produto mais caro
        caro = preço
        mais_caro = nome

    elif preço > caro:
        caro = preço
        mais_caro = nome

    soma = soma + preço

    print(end='\n')

    continuar = str(input('Quer continuar adicionando itens ao carrinho? [S/N] ')).upper().strip()

    print(end='\n')

    while not continuar == 'S' and not continuar == 'N':
        continuar = str(input(
            '\033[31mOpção inválida.\033[m Quer continuar adicionando itens ao carrinho? [S/N] ')).upper().strip()

    if continuar == 'N':
        print('-=' * 30)
        print(f'\nTotal gasto: R${soma:.2f} reais.')
        print(f'Total de produtos que custam mais de R$1000.00 reais: {mais_de_mil}')
        print(f'Produto mais barato da lista: {mais_barato}')
        print(f'Produto mais caro da lista: {mais_caro}\n')
        print('-=' * 30)
        break
