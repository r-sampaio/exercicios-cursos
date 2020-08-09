'''
Crie um script Python que leia dois número e tente mostrar a soma entre eles.
'''
from funcoes import limpa, title,result

limpa()
title()
n1 = int(input('Digite um numero: '))
limpa()
title()
n2 = int(input('Digite outro numero: '))
limpa()
result()
print(f'A soma de \033[33m{n1}\033[m mais \033[32m{n2:}\033[m é igual á: \033[34m{n1 + n2}\033[m\n')
