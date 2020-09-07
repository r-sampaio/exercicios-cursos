'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, 
o maior valor e a soma dos valores.
'''

cont = 0
while True:
    numero = int(input('Digite um número: '))
    if cont == 0:
        maior = numero
        menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    cont += 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
soma = maior + menor
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'A soma entre eles é {soma}')
