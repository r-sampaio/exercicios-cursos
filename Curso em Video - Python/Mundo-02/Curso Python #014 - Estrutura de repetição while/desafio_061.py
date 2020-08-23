# Refaá o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
    # progressão usando a estrutura while.

n = 0
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
while n < 10:
    n += 1
    print(f'{termo}', end='')
    print(', ' if n < 10 else '. ', end='')
    termo += razao
