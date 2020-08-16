# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
    # quantos dólares ela pode comprar.
    # * Considere: US$ 1,00 = R$ 3,27

from funcoes import limpa, title, result

limpa()
title()
dinheiro = float(input('Quanto em dinheiro, você tem na carteira? '))
dolar = float(input('Qual o valor atual do dolar? '))
limpa()
result()
print(f'Dinheiro na carteira: {dinheiro}')
print(f'Valor do dólar atual: {dolar}')
print(f'Com o dólar a US$ {dolar}, você poderia comprar US$ {(dinheiro/dolar):.2f} com esse valor em dinheiro tem na carteira.\n')
