# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
    # será formado:
    # - Equilátero: todos os lados iguais
    # - Isósceles: dois lados iguais
    # - Escaleno: todos os lados diferantes

r1 = float(input('Digite o tamanho de R1: '))
r2 = float(input('Digite o tamanho de R2: '))
r3 = float(input('Digite o tamanho de R3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma triangulo')
else:
    print('Nao forma triangulo')