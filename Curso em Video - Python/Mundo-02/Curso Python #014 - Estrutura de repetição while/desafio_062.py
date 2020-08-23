# melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
    # O programa encerra quando ele disser que quer mostrar 0 termos.


n = 0
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razao: '))
total = 0
m = 10
while m != 0:
    total += m
    while n <= total:
        n += 1
        print(f'{termo}', end='')
        print(', ' if n < m else '. ', end='')
        termo += razao
m = int(input('Deseja mostra mais quantos numeros? '))
