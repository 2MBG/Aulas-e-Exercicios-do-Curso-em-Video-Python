cidade = str(input('\nDigite o nome de uma cidade: ')).strip()
#city = 'Santo' in cidade
city = cidade[:5].capitalize() == 'Santo'

print(f'\nPossui \033[33mSanto\033[m no nome dessa cidade? \033[37;1m{city}\033[m!\n')
