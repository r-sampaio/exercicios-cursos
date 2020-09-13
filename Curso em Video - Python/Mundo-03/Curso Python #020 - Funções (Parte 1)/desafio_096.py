# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular 
# (largura e comprimento) e mostre a área do terreno.

def area(b, h):
    a = b * h
    print(f'{a:.2f} cm²')


b = float(input('Digite o comprimento da base em centímetros: '))
h = float(input('Digite o comprimento da altura em centímetros: '))
area(b, h)
