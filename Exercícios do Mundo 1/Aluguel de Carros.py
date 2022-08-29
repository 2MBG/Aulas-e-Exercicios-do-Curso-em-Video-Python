# 60 é o valor da diária e 0.15 é o valor cobrado por km rodado.

dias = int(input('\n\033[33;1mPor quantos dias o carro foi alugado? \033[m'))
km = float(input('\n\033[37;1mQuantos kilômetros foram percorridos durante esse tempo? \033[m'))
valor_total = (dias * 60) + (km * 0.15)

print(f'\n\033[37;1mO total a pagar é\033[m \033[32;1mR${valor_total:.2f}\033[m \033[37;1mreais.\033[m\n')
