frase = str(input('\n\033[37;1mDigite uma frase: \033[m')).upper().strip()
frase2 = frase.count('A')
frase3 = frase.find('A') + 1 # O '1' por causa da contagem iniciar em 0. 
frase4 = frase.rfind('A') + 1

print(f"\nA letra '\033[33;1mA\033[m' aparece {frase2} vezes nessa frase. ")
print(f"A letra '\033[33;1mA\033[m' aparece pela primeira vez na posição {frase3}.")
print(f"A letra '\033[33;1mA\033[m' aparece pela última vez na posição {frase4}.\n")
