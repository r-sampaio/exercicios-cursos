'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''
from datetime import datetime

dd = int(input('Digite o dia: '))
mm = int(input('Digite o mês: '))
aaaa = int(input('Digite o ano: '))
try:
    data = datetime(aaaa, mm, dd)
    ok = True
except ValueError:
    ok = False
if ok == True:
    print('Data válida')
else:
    print('Data Inválida')
