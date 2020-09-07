'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias 
vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''

m = 1
while True:
    while True:
        num = int(input('Digite um numero: '))
        num2 = num
        if 0 < num < 16:
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
        elif num <= 0:
            print('Digite um numero maior que 0.')
        elif num >= 16:
            print('Digite um numero menor que 16.')
        if 0 < num2 < 16:
            continuar = str(input('Deseja continuar? [S/N] '))
            if continuar in 'Nn':
                break
