salário = float(input('\n\033[33;1mQuanto você ganha por mês? R$\033[m'))
valor1 = salário

if valor1 > 1250:
    valor2 = valor1 + (valor1 * 10 / 100)
    
    print(f'\n\033[37;1mVocê ganhará um aumento de\033[m \033[34;1m10%\033[m '
    f'\033[37;1me passará a receber\033[m \033[32;1mR${valor2:.2f}\033[m \033[37;1mreais!\033[m\n')

if valor1 < 1250:
    valor3 = valor1 + (valor1 * 15 / 100)
    
    print(f'\n\033[37;1mVocê ganhará um aumento de\033[m \033[34;1m15%\033[m '
    f'\033[37;1me passará a receber\033[m \033[32;1mR${valor3:.2f}\033[m \033[37;1mreais!\033[m\n')
