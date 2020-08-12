'''
Faça um programa que leia o comprimento de cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.

O quadrado da hipotenusa é igual a soma dos quadrados dos catetos.
'''
import os
from math import hypot
os.system('cls')
catetoOposto = float(input('Digite o comprimeito do cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
print(f'{hypot(catetoOposto, catetoAdjacente)}')