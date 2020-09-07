'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

c = 0
while True:
    num = int(input('Digite um numero: '))
    for i in range(1, num + 1):
        if num % i == 0:
            c += 1
    if c == 2:
        print('Primo')
        c = 0
    else:
        print('Não primo')
        c = 0
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
