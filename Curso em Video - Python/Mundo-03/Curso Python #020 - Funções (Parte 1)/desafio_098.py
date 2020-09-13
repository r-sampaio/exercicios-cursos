# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

def contador(a, b, c):
    
    print(f'Contagem de {a} ate {b} de {c} em {c}')
    sleep(2.5)
    
    if c == 0:
        c = 1
    
    if a < b:
        for i in range(a, b + 1, c):
            print(i, end=' ', flush=True)
            sleep(0.5)
        print()
    else:
        for i in range(a, b - 1, -c):
            print(i, end=' ', flush=True)
            sleep(0.5)
        print()


contador(1, 10, 1)
contador(10, 1, 2)
print('Digite:')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Pas: '))
contador(ini, fim, pas)

# def contador(i, f, p):
#     if p< 0:
#         p *= -1
#     if p == 0:
#         p = 1
#     print(f'Contagem de {a} ate {b} de {c} em {c}')
    
#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f'{cont} ', end='', flush=True)
#             cont += p
#     else:
#         cont = i
#         while cont >= f:
#             print(f'{cont} ', end='', flush=True)
#             cont -= p
