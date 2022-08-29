print('\n\033[33;1mForneça algumas informações para saber se seu empréstimo será aprovado ou não:\033[m')

casa = float(input('\nQual é o valor da casa que você pretende comprar? R$'))
salário = float(input('Quanto você ganha por mês? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))

prestação = casa / (anos * 12)
num2 = salário * 30 / 100

print(f'\nO valor da prestação será de \033[37;1mR${prestação:.2f}\033[m reais!')

if prestação <= num2:
   print('\n\033[32;1mEmpréstimo aprovado!\033[m\n')

else:
   print('\n\033[31;1mEmpréstimo negado!\033[m\n')
