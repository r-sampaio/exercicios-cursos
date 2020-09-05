'''
Faça um programa que receba dois números inteiros e gere os números inteiros 
que estão no intervalo compreendido por eles.
'''

n1 = int(input('Digite um inteiro: '))
n2 = int(input('Digite outro inteiro: '))
if n1 < n2:
    for i in range(n1 +1 , n2):
        print(f'{i} ', end='')
else:
    for i in range(n1 -1, n2, -1):
        print(f'{i} ', end='')
