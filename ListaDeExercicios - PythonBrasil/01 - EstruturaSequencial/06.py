# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from math import sqrt
a = float(input('Digite o raio do círculo: '))
m = str(input('Unidade de medida: ')).strip()
r = 3.14 * pow(a, 2)
print(f'Aproximadamente {r} {m}²')
