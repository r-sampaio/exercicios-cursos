import os
from funcoes import limpa

limpa()
dia = input('Em que dia você nasceu? ')
limpa()
mes = input('Em que mês você nasceu? ')
limpa()
ano = input('Em que ano você nasceu? ')
limpa()
print('Você nasceu em {}/{}/{}.\n'.format(dia, mes, ano))
