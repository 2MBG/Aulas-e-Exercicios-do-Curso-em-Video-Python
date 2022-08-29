num1 = int(input('\n\033[33;1mDigite um número: \033[m'))
m1 = num1 * 2
m2 = num1 * 3
m3 = num1 ** (1/2)

print(f'''\n\033[37;1mO dobro de\033[m \033[35;1m{num1}\033[m \033[37;1mé:\033[m \033[34;1m{m1}\033[m
\n\033[37;1mO triplo de\033[m \033[35;1m{num1}\033[m\033[37;1m é:\033[m \033[34;1m{m2}\033[m
\n\033[37;1mE a raiz quadrada de\033[m \033[35;1m{num1}\033[m \033[37;1mé:\033[m \033[34;1m{m3:.2f}\033[m\n''')
