# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input('Digite o ano: '))
# ano = ano % 2
# if ano == 0:
#     print('Ano BISSEXTO')
# else:
#     print('Não é BISSEXTO')

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Ano {ano} BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')
