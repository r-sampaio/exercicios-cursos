# Altere o programa anterior para mostrar no final a soma dos números.

soma = 0
n1 = int(input('Digite um inteiro: '))
n2 = int(input('Digite outro inteiro: '))
if n1 < n2:
    for i in range(n1 +1 , n2):
        print(f'{i} ', end='')
        soma += i
else:
    for i in range(n1 -1, n2, -1):
        print(f'{i} ', end='')
        soma += i
print(f'\nSomados dão o valor de: {soma}')
