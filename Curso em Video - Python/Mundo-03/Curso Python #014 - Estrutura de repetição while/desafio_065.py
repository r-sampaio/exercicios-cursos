# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
    # todos os valores e qual foi o maior e o menor valor lido. o programa deve perguntar ao usuário se ele 
    # quer ou não continuar a digitar valores.

o = 'S'
n = q = s = maior = menor = 0
while o in 'Ss':
    n = float(input('Digite um número: '))
    o = str(input('Quer continuar? ')).upper().strip()[0]
    s += n
    q += 1
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
m = s / q
print(f'Quantidade de números digitados {q} com média de {m}.')
print(f'O número {maior} foi o maior, e o {menor} foi o menor número digitado.')
