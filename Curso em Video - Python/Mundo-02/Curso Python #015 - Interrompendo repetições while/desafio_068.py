# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador 
    # perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint


n = q = 0
m = 'Pp'
c = randint(1,10)
while True:
    n = int(input('Digite um numero: '))
    m = str(input('Par ou ímpar [P/I]: ')).upper().strip()[0]
    if m in 'Pp':
        if n % 2 == 0:
            print('Você venceu!')
            q += 1
        else:
            print('Você Perdeu')
            break
    elif m in 'Ii':
        if n % 2 != 0:
            print('Você venceu!')
            q += 1
        else:
            print('Você Perdeu')
            break
print(f'Você venceu {q} vezes')
