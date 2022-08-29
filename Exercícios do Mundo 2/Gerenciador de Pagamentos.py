print('\n\033[33;1mPAGAMENTO DE COMPRAS\033[m')

valor = float(input('\nQual o valor total da sua compra? R$'))
print('''\nComo pretende pagar?

[ \033[35;1m1\033[m ] À vista no dinheiro/cheque (10% de desconto)
[ \033[35;1m2\033[m ] À vista no cartão (5% de desconto)
[ \033[35;1m3\033[m ] Em 2x no cartão (sem juros)
[ \033[35;1m4\033[m ] Em 3x ou mais no cartão (20% de juros)\n''')

escolha = int(input('Digite o número da opção desejada: '))

if escolha == 1:
    total = valor - (valor * 10 / 100)
    print(f'\n\033[37;1mO valor final da sua compra é de \033[32mR${total:.2f}\033[m reais.\033[m\n')

elif escolha == 2:
    total = valor - (valor * 5 / 100)
    print(f'\n\033[37;1mO valor final da sua compra é de \033[32mR${total:.2f}\033[m reais.\033[m\n')

elif escolha == 3:
    total = valor
    parcela = total / 2
    print(f'\nSua compra será parcelada em 2x de R${parcela:.2f} reais.')
    print(f'\n\033[37;1mO valor final da sua compra é de \033[32mR${total:.2f}\033[m reais.\033[m\n')

elif escolha == 4:
    total = valor + (valor * 20 / 100)
    qtdparcelas= int(input('Em quantas parcelas? '))
    parcela = total / qtdparcelas
    print(f'\nSua compra será parcelada em {qtdparcelas}x de R${parcela:.2f} reais.')
    print(f'\n\033[37;1mO valor final da sua compra é de \033[32mR${total:.2f}\033[m reais.\033[m\n')

else:
    print('\n\033[31;1mOpção inválida. Tente novamente.\033[m\n')
