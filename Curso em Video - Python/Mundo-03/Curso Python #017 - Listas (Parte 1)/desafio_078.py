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

'''
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i,v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ',end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i,v in enumerate(listanum):
    if v == men:
        print(f'{i}... ',end='')
print()
'''
