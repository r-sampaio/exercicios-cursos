# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
c = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end='')
        c += 1
    else:
        print('\033[31m', end='')
    print(i, end=' ')
print(f'\n\033[mO número {numero} e divisivel {c} vezes.')
if c == 2:
    print('Primo')
else:
    print('Não é primo')
