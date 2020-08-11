'''
Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento.
'''
from funcoes import limpa, title, result

limpa()
title()
salario = float(input('Qual o valor do seu salario? '))
almento = float(input('Qual a porcentagem de almento? '))
limpa()
result()
print(f'O seu salario vai receber um almento de {almento:.2f}%, e passará para o valor de {((salario+((salario/100)*almento))):.2f} \n')
#print(f'O seu salario vai receber um almento de {almento:.2f}%, e passará para o valor de {((salario+((salario*almento/100)))):.2f} \n')
