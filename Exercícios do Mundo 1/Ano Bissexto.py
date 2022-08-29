from datetime import date

ano = int(input('\n\033[37;1mQual ano você gostaria de saber se é\033[m '
f'\033[32;1mBissexto\033[m \033[37;1mou não? '
f'Digite\033[m \033[33;1m0\033[m \033[37;1mcaso queira analisar o ano atual: \033[m'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\n\033[37;1m{ano}\033[m \033[32;1mé\033[m \033[37;1mum ano Bissexto!\033[m\n')

else:
    print(f'\n\033[37;1m{ano}\033[m \033[31;1mnão\033[m \033[37;1mé um ano Bissexto!\033[m\n')
