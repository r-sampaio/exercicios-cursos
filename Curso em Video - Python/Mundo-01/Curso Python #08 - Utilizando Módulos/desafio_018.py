'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
'''
from math import radians
from math import sin
from math import cos
from math import tan
import os

os.system('cls')

anguloGrau = float(input('Digite o ângulo: '))
seno = sin(radians(anguloGrau))
cosseno = cos(radians(anguloGrau))
tangente = tan(radians(anguloGrau))
print(f'O seno do ângulo \033[32m{anguloGrau:.2f}\033[m é \033[34m{seno:.2f}\033[m.')
print(f'O cosseno do ângulo \033[32m{anguloGrau:.2f}\033[m é \033[34m{cosseno:.2f}\033[m.')
print(f'A tangente do ângulo \033[32m{anguloGrau:.2f}\033[m é \033[34m{tangente:.2f}\033[m.')
