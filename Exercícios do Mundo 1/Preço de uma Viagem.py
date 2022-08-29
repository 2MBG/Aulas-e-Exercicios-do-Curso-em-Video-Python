distância = float(input('\n\033[33;1mQuantos km serão percorridos durante a sua viagem?: \033[m'))

if distância <= 200:
    valor = distância * 0.50
    print(f'\nA passagem vai custar \033[32;1mR${valor:.2f}\033[m reais!\n')

else:
    valor2 = distância * 0.45
    print(f'\nA passagem vai custar \033[32;1mR${valor2:.2f}\033[m reais!\n')
