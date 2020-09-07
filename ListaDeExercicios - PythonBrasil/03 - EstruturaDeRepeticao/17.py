'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''

m = 1
num = int(input('Digite um numero: '))
print(f'O fatorial de {num}! é ', end='')
while True:
    print(f'{num}', end='')
    m *= num
    num -= 1
    if num == 0:
        print(' = ', end='')
        break
    print('.', end='')
print(m)
