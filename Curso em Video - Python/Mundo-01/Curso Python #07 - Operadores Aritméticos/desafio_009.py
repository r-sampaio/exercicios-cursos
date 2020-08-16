# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

from funcoes import limpa, title, result

def traco():
    n = 0
    while n <= 3:
        print('-'*17, end='')
        print('  ', end='')
        n = n+1

limpa()
title()
num = int(input('Digite um numero: '))
limpa()
r = 0
traco()
print('')
while r <= 10:
    print(f'| {r:<2} + {num:<2} = {(r+num):<3} |  | {r:<2} - {num:<2} = {(r-num):<3} |  | {r:<2} x {num:<2} = {(r*num):<3} |  | {r:<2} / {num:<2} = {(r/num):<3.0f} |')
    r = r+1
traco()
print('\n')
