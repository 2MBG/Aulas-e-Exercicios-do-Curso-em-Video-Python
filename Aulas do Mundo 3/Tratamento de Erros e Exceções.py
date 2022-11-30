# As cláusulas else e finally são opcionais.

try:
    a = int(input('\nNumerador: '))
    b = int(input('Denominador: '))
    r = a / b

# except Exception as erro:
#     print(f'\nInfelizmente tivemos um problema de \033[1;31m{erro.__class__}\033[m.\n')

except (ValueError, TypeError):
    print('\nTivemos um problema com os dados que você digitou.\n')

except ZeroDivisionError:
    print('\nNão é possível dividir um número por zero!\n')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')

# except Exception as erro:
#     print(f'O erro encontrado foi {erro.__cause__}')

else:
    print(f'\nO resultado é {r:.2f}\n')

finally:
    print('Volte sempre!\n')
