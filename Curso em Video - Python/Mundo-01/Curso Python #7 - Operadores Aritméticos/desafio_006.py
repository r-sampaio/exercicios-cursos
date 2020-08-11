'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada.
'''
from funcoes import limpa, title, result

limpa()
title()
num = int(input('Digite um numero: '))
limpa()
result()
print(f'Você digitou "{num}", e seu dobro é {num*2}, seu triplo é {num*3} e sua raiz quadrada é aproximadamente {(pow(num,(1/2))):.2f}.\n')
