# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
    # de uma Sequência de Fibonacci.
    # Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8


n = 0
termos = int(input('Digite quantos termos exibir: '))
while n < termos:
    print(f'{n}', end='')
