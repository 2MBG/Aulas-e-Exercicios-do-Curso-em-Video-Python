velocidade = float(input('\nVocê estava a quantos km/hr quando passou pela Avenida Principal? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'\n\033[31;1mVocê excedeu o limite de velocidade e foi multado em R${multa:.2f} reais!\033[m\n')

else:
    print('\n\033[32;1mVocê estava dentro da velocidade permitida!\033[m\n')

print('Dirija sempre com segurança!\n')
