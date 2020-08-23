# melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
    # O programa encerra quando ele disser que quer mostrar 0 termos.


n = 0
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razao: '))
while n < 10:
    n += 1
    print(f'{termo}', end='')
    print(', ' if n < 10 else '. ', end='')
    termo += razao
m = int(input('Deseja mostra mais quantos números? ')
        if m != 0:
            n = 0
            while n <= m:
                n += 1
                print(f'{termo}', end='')
                print(', ' if n < m else '. ', end='')
                termo += razao
        else:
            print('Programa finalizado.')
