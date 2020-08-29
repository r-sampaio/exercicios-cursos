# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o 
    # maior e o menor valor digitado e as suas respectivas posições na lista.

cont = menor = maior = posicao = 0
lista = []
for p in range(0, 5):
    valor = int(input(f'Digite um valor da posição {p}: '))
    lista.append(valor)
    for l in lista:
        if cont == 0:
            menor = l
            maior = l
            cont = p
        elif menor >= valor:
            menor = valor
        elif maior <= valor:
            maior = valor
print(f'Lista digitada {lista}')
print(f'Menor valor {menor} na posição ', end='')
for pos, i in enumerate(lista):
    if i == menor:
        print(pos, end=' ')
print(f'\nMaior valor {maior} na posição ', end='')
for pos, i in enumerate(lista):
    if i == maior:
        print(pos, end=' ')
