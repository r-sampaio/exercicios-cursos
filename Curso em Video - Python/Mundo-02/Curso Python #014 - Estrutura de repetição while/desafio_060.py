# Faça um programa que leia um número qualquer e mostre o seu fatorial.
    # Ex: 5! = 5x4x3x2x1 = 120

# while
numero = int(input('Digite um número: '))
f = 1
c = numero
print(f'Fatorial de {numero}! é ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f'{f}')

# for
numero = int(input('Digite um número: '))
f = 1
c = numero
print(f'Fatorial de {numero}! é ', end='')
for i in range(c, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f'{f}')