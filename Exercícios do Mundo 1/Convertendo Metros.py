num1 = float(input('\nA porta do seu quarto possui quantos metros? '))
num2 = num1 / 1000 # Quilômetro
num3 = num1 / 100 # Hectômetro
num4 = num1 / 10 # Decâmetro
num5 = num1 * 10 # Decímetro
num6 = num1 * 100 # Centímetro
num7 = num1 * 1000 # Milímetro

print(f'''\nCovertendo estes metros sua porta teria:
\n{num2} Quilômetros
{num3} Hectômetros
{num4} Decâmetros
{num5:.0f} Decímetros
{num6:.0f} Centímetros
{num7:.0f} Milímetros\n''')
