# Escreva um programa que leia dois número inteiros e compare-os, mostrando na tela uma mensagem:
    # - O primeiro valor é maior
    # - O segundo valor é maior
    # - Não existe valor maior, os dois são iguais

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
print(f'Você digitou {n1:.2f} e {n2:.2f}.')
if n1 > n2:
    print(f'O primeiro valor e maior.')
elif n1 < n2:
    print(f'O segundo valor e maior.')
else:
    print(f'Não existe valor e maior, os 2 sao iguais.')
