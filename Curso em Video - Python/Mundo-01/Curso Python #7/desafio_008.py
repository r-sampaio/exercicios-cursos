'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''
from funcoes import limpa, title, result

limpa()
title()
metros = int(input('Dígite a distância em metros: '))
limpa()
print(f'O valor {metros}, corresponde a {metros*100}, e a {metros*1000} milimetros')