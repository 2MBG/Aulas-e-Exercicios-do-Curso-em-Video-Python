num1 = int(input('\n\033[33mDigite um número: \033[m'))
num2 = int(input('\033[33mDigite outro número: \033[m'))

soma = num1 + num2
divisão = num1 / num2
multiplicação = num1 * num2
expoente = num1 ** num2
divisão_inteira = num1 // num2

print(f'''\n\033[32mConsiderando esses dois números:\n\033[m
\033[35;1mO expoente: \033[m{expoente}
\033[35;1mA multiplicação: \033[m{multiplicação}
\033[35;1mA divisão: \033[m{divisão:.2f}
\033[35;1mA divisão inteira: \033[m{divisão_inteira}
\033[35;1mA soma: \033[m{soma}\n''')
