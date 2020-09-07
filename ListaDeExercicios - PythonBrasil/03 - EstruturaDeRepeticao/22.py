'''
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, 
por quais número ele é divisível.
'''

c = 0    
while True:
    num = int(input('Digite um numero: '))
    for i in range(1, num + 1):
        if num % i == 0:
            c += 1
        elif c > 2:
            c = 0
            for i in range(1, num + 1):
                if num % i == 0:
                    c += 1
                    print (f'{i}', end='')
                if i < num and num % i == 0:
                    print(f', ', end='')
                elif i == num:
                    print(' : ', end='')
            break
    if c == 2:
        print('Primo')
        c = 0
    else:
        print('Não primo')
        c = 0
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
