def leiaDinheiro(mensagem):
    válido = False
    
    while not válido:
        entrada = str(input(mensagem)).replace(',','.').strip()
        
        if entrada.isalpha() or entrada == '':
            print(f'\n\033[1;31mERRO. \"{entrada}\" é um preço inválido.\033[m')
        else:
            válido = True
            return float(entrada)
