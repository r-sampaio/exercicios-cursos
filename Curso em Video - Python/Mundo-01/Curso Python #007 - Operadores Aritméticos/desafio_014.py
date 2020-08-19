# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

from funcoes import limpa, title, result

limpa()
title()
temperatura = float(input('Digite uma temperatura em graus Celsius: '))
limpa()
result()
print(f'{temperatura}ºC equivalem a {(temperatura*9/5)+32}ºF ou a {temperatura+273.15}ºK\n')