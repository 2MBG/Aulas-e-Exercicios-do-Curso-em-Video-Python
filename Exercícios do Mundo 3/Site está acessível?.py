import requests

try:
    site = input('\nInsira o link do site: ')
    check = requests.get(site)
    print('\n\033[1;32mSite está acessível.\033[m\n')
    # print(site.read()) # mostra o código html do site
except:
    print(f'\n\033[1;31mSite está indisponível.\033[m\n')
