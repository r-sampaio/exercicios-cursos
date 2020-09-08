# Faça um programa que calcule o mostre a média aritmética de N notas.

m = x = x1 = n = n1 = 0
cont = 1
while True:
    x = int(input(f'Digite o {cont}º valor de X: '))
    x1 += x
    print(x1)
    cont += 1
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
cont = 1
while True:
    n = int(input(f'Digite o {cont}º valor de N: '))
    n1 += n
    print(n1)
    cont += 1
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
m = x / n
print(f'A média aritmética é: {m:.2f}')
