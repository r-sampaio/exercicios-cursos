'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''
from funcoes import limpa, title, result

limpa()
title()
metros = float(input('Dígite a distância em metros: '))
limpa()
result()
# print(f'A distância de {metros} metros, corresponde a {metros*100} centímetros e a {metros*1000} milímetros\n')

# Continuação: Metros em: quilômetros, hectômetro, decâmetros, decímetros, centímetros e milímetros.

print(f'A medida de {metros} metros equivale a: ')
print(f'{metros/1000} km\n{metros/100} hm\n{metros/10} dam\n{metros} m\n{metros*10} dm\n{metros*100} cm\n{metros*1000} mm\n')
