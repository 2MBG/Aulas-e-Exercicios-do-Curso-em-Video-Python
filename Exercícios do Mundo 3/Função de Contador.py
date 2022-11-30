from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1 # Transforma o número em positivo
    if passo == 0:
        passo = 1

    print(f"\nContagem de {inicio} até {fim} de {passo} em {passo}.")

    if inicio < fim:
        counter = inicio
        
        while counter <= fim:
            print(f"{counter}, ", end="", flush=True) # Flush serve para que o sleep faça a contagem corretamente
            sleep(0.5)
            counter += passo
        print("Fim!")
    
    else:
        counter = inicio
        
        while counter >= fim:
            print(f"{counter}, ", end="", flush=True) # Usa-se o flush pra forçar que o resultado apareça imediatamente, mesmo sem linha nova
            sleep(0.5)
            counter -= passo
        print("Fim!")


print(end='\n')
print('-' * 31)
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
print('-' * 31)

contador(1, 10, 1) # De 1 até 10 pulando de 1 em 1
contador(10, 0, 2) # De 10 até 0 pulando de 2 em 2
contador(inicio, fim, passo)
