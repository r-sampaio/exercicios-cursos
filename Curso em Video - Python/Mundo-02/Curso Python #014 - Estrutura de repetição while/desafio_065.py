# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
    # todos os valores e qual foi o maior e o menor valor lido. o programa deve perguntar ao usuário se ele 
    # quer ou não continuar a digitar valores.


n = 0
q = 1
o = 'S'

while o in 'S':
    n = float(input('Digite um número: '))
    o = str(input('Quer continuar? ')).upper().strip()[0]
    n += n
    q += 1
    if n <= n:
        maior = n
    elif n >= n:
        menor = n
s = n / q
print(f'{s} Media e o maior foi {maior} e o menor foi {menor}.')
