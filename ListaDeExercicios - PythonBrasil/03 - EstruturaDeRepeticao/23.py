'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido 
pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para 
encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes 
(divisões) executados.
'''

c = 0
while True:
    num = int(input('Digite um numero: '))
    for i in range(1, num + 1):
        if num % i == 0:
            c += 1
            print (f'{i}', end='')
            if i < num:
                print(f', ', end='')
            if i >= num:
                print(' : ', end='')
    if c == 2:
        print(f'Primo, divisível {c} vezes.')
        c = 0
    else:
        print(f'Não primo, divisível {c} vezes.')
        c = 0
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
