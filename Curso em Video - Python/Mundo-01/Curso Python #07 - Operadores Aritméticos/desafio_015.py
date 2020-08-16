# Escreva um programa que pergute a quantidade de Km percorrido por um carro alugado
    # e a quantidade de dias pelos quais ele foi alugado, calcule o preço a pagar,
    # sabendo que o carro custa R$60 pro dia e R$0,15 por Km rodado.

from funcoes import limpa, title, result

limpa()
title()
km = float(input('Quantos quilometros o carro percorreu? '))
dias = int(input('Por quantos dias o carro ficou alugado? '))
limpa()
result()
print(f'Você irá pagar R${((km*0.15)+(dias*60)):.2f}.\n')
