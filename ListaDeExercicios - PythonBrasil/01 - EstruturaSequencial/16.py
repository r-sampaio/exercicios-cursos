# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área 
# a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta 
# é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta 
# a serem compradas e o preço total.

from math import ceil

tamanho = float(input('Digite o tamanho da parede em metros quadrados: '))
s = tamanho / 3
b = 80 / 18
c = s * b
v = c / 80
f = ceil(v)
print(f'Você irá pagar R${(f*80):.2f} por {f} latas de tinta.')
