# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
    # No final, mostre a matriz na tela, com a formatação correta.

lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for c in range(0, 3):
        lista[i][c] = int(input(f'Digite o valor de [{i}, {c}]: '))
for i in lista:
    print(f'[{i[0]:^5}][{i[1]:^5}][{i[2]:^5}]',)
