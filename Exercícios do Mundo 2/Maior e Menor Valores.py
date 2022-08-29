resposta = 'SIM'
média = 0
soma = 0
quantidade = 0
maior = 0
menor = 0

while resposta == 'SIM':
    print(end='\n')

    número = int(input('\033[33mDigite um número:\033[m '))
    soma =  soma + número
    quantidade = quantidade + 1
    
    # Se for digitado apenas um número ele será o maior e o menor
    if quantidade == 1:
        maior = menor = número
    
    else:
        if número > maior:
            maior = número
        
        if número < menor:
            menor = número

    resposta = str(input('\n\033[32mQuer continuar?\033[m [SIM/NÃO] ')).upper().strip()

    while not resposta == 'SIM' and not resposta == 'NÃO':
        resposta = str(input('\n\033[31;1mDados inválidos.\033[m Quer continuar? [SIM/NÃO] ')).upper().strip()


média = soma / quantidade

print(f'\nVocê digitou {quantidade} número(s) e a média foi de {média:.1f}.\n')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}.\n')
