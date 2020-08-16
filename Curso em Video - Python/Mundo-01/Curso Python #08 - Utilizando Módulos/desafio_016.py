# Crie um programa que leia um número Real qualquer pelo teclado
    # e mostre na tela a sua porção inteira.
    # * Ex: Digite um número: 6.127
    # * O número 6.127 tem a parte inteira 6.

from math import trunc
import os
os.system('cls')
numero = float(input('Digite um número Real qualquer: '))
#print(f'A parte inteira do numero {numero} é, {numero:.0f}.') // usa aproximação
print(f'A parte inteira do numero {numero} é, {trunc(numero)}.')
