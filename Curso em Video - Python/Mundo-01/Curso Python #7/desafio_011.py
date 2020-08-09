'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta. pinta uma área de 2m².
'''
from funcoes import limpa, title, result

limpa()
title()
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
limpa()
print(f'Será nescesario comprar {(largura*altura)/2} litros de tinta, para pintar os {largura*altura}m² da parede.\n')
