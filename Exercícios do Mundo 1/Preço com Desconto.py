produto = float(input('\nQuanto custa um Playstation 5? R$'))
desconto = 5
num1 = produto * desconto / 100
valor_final = produto - num1

print(f'\nO valor do Playstation 5 com 5% de desconto é R${valor_final:.2f} reais.\n')
