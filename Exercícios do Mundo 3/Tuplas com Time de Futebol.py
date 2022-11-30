print('\n\033[33;1m===== TABELA DO CAMPEONATO BRASILEIRO 2022 =====\033[m')

print(end='\n')

times = ('Palmeiras', 'Athletico-PR', 'Atlético-MG', 'Corinthians', 'Internacional', 
'Fluminense', 'São Paulo', 'Flamengo', 'Santos', 'Botafogo', 'Avaí', 'Coritiba',
'América-MG', 'Bragantino', 'Ceará SC', 'Atlético-GO', 'Goiás', 'Cuiabá', 'Juventude', 'Fortaleza')

print('=' * 15)
for tim in times:
    print(tim)
print('=' * 15)
   
print(f'\nOs primeiros 5 colocados são: {times[0:5]}')

print(f'\nOs últimos 4 colocados são: {times[-4:]}')

print('\n\033[33mLista dos times em ordem alfabética:\033[m\n')

print('=' * 15)
for t in sorted(times):
    print(t)
print('=' * 15)

pal = times.index('Palmeiras') + 1
print(f'\nO \033[32;1mPalmeiras\033[m está na {pal}ª posição.\n')
