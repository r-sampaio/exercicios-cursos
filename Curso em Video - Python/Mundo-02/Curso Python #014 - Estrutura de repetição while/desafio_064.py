# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
    # digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digirados e qual
    # foi a soma entre eles (desconsiderando o flag).


n = s = q = 0
while n != 999:
    n = int(input('Digite um numero ou 999 para sair: '))
    if n != 999:
        s += n
        q += 1
print(f'Você digitou {q} números que da uma soma de {s} entre eles.')

'''
n = s = q = 0
n = int(input('Digite um numero ou 999 para sair: '))
while n != 999:
    s += n
    q += 1
    n = int(input('Digite um numero ou 999 para sair: '))
print(f'Você digitou {q} números que da uma soma de {s} entre eles.')
'''
