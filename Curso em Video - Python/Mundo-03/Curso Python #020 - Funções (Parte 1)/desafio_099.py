# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* par):
    cont = maior = 0
    print('Valores: ', end='')
    for p in par:
        print(p, end=' ')
        if cont == 0:
            maior = p
        if p > maior:
            maior = p
        cont += 1
    print()
    print(f'Foram passados {len(par)} valores', end='')
    print(f'e o {maior}')


maior(2, 9, 4, 5, 7, 1)
print()
maior(4, 7, 0)
print()
maior(1, 2)
print()
maior(6)
print()
maior()
