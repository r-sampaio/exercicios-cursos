# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
    # de uma Sequência de Fibonacci.
    # Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8


n = 3
n1 = 0
n2 = 1
termos = int(input('Digite quantos termos exibir: '))
print(f'{n1} - {n2} - ', end='')
while n <= termos:
    s = n1 + n2
    print(f'{s}', end='')
    print(' - ' if n < termos else '', end='')
    n1 = n2
    n2 = s
    termos -= 1
