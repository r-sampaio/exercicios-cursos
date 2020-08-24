# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número: '))
numero = numero % 2
if numero == 0:
    print('PAR')
else:
    print('IMPAR')
