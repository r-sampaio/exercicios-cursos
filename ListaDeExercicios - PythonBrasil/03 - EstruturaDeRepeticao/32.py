# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
    # Fatorial de: 5
    # 5! =  5 . 4 . 3 . 2 . 1 = 120


numero = int(input('Digite um numero: '))
c = numero
fatorial = 1
print(f'Fatorial de: {numero}')
print(f'{numero}! = ', end='')
while True:
    print(f'{c}', end='')
    fatorial *= c
    c -= 1
    if c == 0:
        break
    else:
        print(' . ', end='')
print(' = ', end='')
print(fatorial)
