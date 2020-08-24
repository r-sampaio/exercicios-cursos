# Crie um programa que leia o ano de nascimento de sete pessoas, No final, mostre quantas
    # pessoas ainda não atingiram a maioridade e quantas já são maiores. 21 anos.

from datetime import date

ano = date.today().year
ma = 0
me = 0

for i in range(1, 8):
    data = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    resultado = ano - data
    if resultado >= 21:
        ma += 1
    else:
        me += 1
print(f'{ma} pessoas são maiore de idade e {me} são menores.')
