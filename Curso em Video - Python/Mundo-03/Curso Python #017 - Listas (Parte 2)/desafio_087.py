# Aprimore o desafio anterior, mostrando no final:
    # A) A soma de todos os valores pares digitados.
    # B) A soma dos valores da terceira coluna.
    # C) O maior valor da segunda linha.

s = t3 = cont = 0
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for c in range(0, 3):
        lista[i][c] = int(input(f'Digite o valor de [{i}, {c}]: '))
        if lista[i][c] % 2 == 0:
            s += lista[i][c]
    t3 += lista[i][2]
for i in range(0, 3):
    if i == 0 or lista[1][i] > cont:
        cont = lista[1][i]
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[i][c]:^5}]',end='')
    print()

print(f'A soma de todos os valores pares digitados é: {s}')
print(f'A soma dos valores da terceira coluna é: {t3}')
print(f'O maior valor da segunda linha é: {cont}')


'''
s = 0
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
t3 = 0
for i in range(0, 3):
    for c in range(0, 3):
        lista[i][c] = int(input(f'Digite o valor de [{i}, {c}]: '))
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[i][c]:^5}]',end='')
        if lista[i][c] % 2 == 0:
            s += lista[i][c]
        print()
print(f'A soma de todos os valores pares digitados é: {s}')
for i in range(0, 3):
    t3 += lista[i][2]
print(f'A soma dos valores da terceira coluna é: {t3}')
for c in range(0, 3):
    if c == 0 or lista[1][c] > cont:
        cont = lista[1][c]
print(f'O maior valor da segunda linha é: {cont}')
'''
