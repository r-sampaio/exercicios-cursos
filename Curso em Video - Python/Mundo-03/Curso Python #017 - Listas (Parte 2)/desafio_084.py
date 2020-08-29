# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
    # A) Quantas pessoas foram cadastradas. 
    # B) Uma listagem com as pessoas mais pesadas.
    # C) Uma listagem com as pessoas mais leves.

maior = menor = 0
lista = []
temp = []
while True:
    temp.append((str(input('Nome: '))))
    temp.append((float(input('Peso: '))))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    continuar = input('Continuar? [S/N] ')
    if continuar in 'Nn':
        break
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'Maior peso {maior}Kg de ', end='')
for i in lista:
    if i[1] == maior:
        print(f'[{i[0]}]', end='')
print()
print(f'Menor peso {menor}Kg de ', end='')
for i in lista:
    if i[1] == menor:
        print(f'[{i[0]}]', end='')
print()
