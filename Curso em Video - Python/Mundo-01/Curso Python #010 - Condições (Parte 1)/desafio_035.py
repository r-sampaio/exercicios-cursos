# Desenvolva um programa que leia o comprimento de três retas e diga
    # ao usuário se ele pode ou não formar um triãngulo.
    # * r1 ----------                 |    r1 --
    # * r2 ---------------     Sim    |    r2 ------             Não      
    # * r3 ------------               |    r3 ----------------

r1 = float(input('Digite o comprimento de r1: '))
r2 = float(input('Digite o comprimento de r2: '))
r3 = float(input('Digite o comprimento de r3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma um triagulo')
else:
    print('Não forma um triagulo')
