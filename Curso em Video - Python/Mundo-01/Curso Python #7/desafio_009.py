from funcoes import limpa, title, result

limpa()
title()
num = int(input('Digite um numero: '))
limpa()
r = 0 
print(f' Tabuada de {num}')

while r <= 10:
    print(f'| {r} + {num} = {(r+num):<3} |')
    r = r+1
print('-'*15)