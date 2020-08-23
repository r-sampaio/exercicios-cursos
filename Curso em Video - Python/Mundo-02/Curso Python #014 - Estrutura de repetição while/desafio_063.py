# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
    # de uma Sequência de Fibonacci.
    # Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

s = 0
n = 0
n1 = 0
n2 = 1
termos = int(input('Digite quantos termos exibir: '))
while n <= termos:
    print(f'{s} ', end='')
    s = n1 + n2
    n1 = n2
    n2 = s
    termos -= 1
