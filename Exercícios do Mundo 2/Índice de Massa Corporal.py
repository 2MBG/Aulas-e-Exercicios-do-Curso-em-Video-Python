massa = float(input('\nQual é o seu peso? (kg): '))
altura = float(input('Qual é a sua altura? (m): '))
imc = massa / (altura ** 2)

print(f'\nO IMC dessa pessoa é de {imc:.1f}\n')

if imc < 18.5:
    print('Abaixo do peso.\n') 

elif imc >= 18.5 and imc < 24.9:
    print('Peso normal.\n')

elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso.\n')

elif imc >= 30 and imc <= 34.9:
    print('Obesidade I.\n')

elif imc >= 35 and imc <= 39.9:
    print('Obesidade II.\n')

elif imc > 40:
    print('Obesidade III.\n')
