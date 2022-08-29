salário = float(input('\nQuanto você ganha por mês? R$'))
aumento = 15
num2 = salário * aumento / 100
novo_salário = salário + num2

print(f'\nVocê ganhará um aumento de 15% e passará a receber R${novo_salário:.2f} reais.\n')
