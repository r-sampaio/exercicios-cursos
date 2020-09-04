'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''
from math import trunc

n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
print('A - Adição')
print('S - Subtração')
print('M - Multiplicação')
print('D - Divisão')
operacao = str(input('Digite a operação desejada: ')).strip()[0]
if operacao in 'Aa':
    num = n1 + n2
elif operacao in 'Ss':
    num = n1 - n2
elif operacao in 'Mm':
    num = n1 * n2
elif operacao in 'Dd':
    num = n1 / n2
print(f'O numero {trunc(num)} é ', end='')
if num % 2 == 0:
    print('par, ', end='')
else:
    print('ímpar, ', end='')
if num > 0:
    print('positivo e ', end='')
else:
    print('negativo e ', end='')
if num == round(num):
    print('inteiro.')
else:
    print(f'decimal.')
