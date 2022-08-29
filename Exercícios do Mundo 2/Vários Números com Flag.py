número = 0
soma = 0
contador = 0

print(end='\n')

while True:
    número = int(input('Digite um número (999 para encerrar): '))
    
    if número == 999:
        break  # Tem que ser colocado antes das outras variáveis para que a flag não seja contabilizada.
    
    contador = contador + 1

    soma = soma + número

print(f'\nAo todo foram digitados {contador} números e a soma entre eles é igual a {soma}.\n')
