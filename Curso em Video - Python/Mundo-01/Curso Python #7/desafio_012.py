'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''
from funcoes import limpa, title, result

limpa()
title()
preco = float(input('Digite o proço do produto: '))
desconto = float(input('Qual a porcentagem de desconto? '))
limpa()
result()
print(f'Com o descontro de {desconto:.2f}%, seu produto vai ficar por R$ {(preco-((preco/100)*desconto)):.2f}.\n')
