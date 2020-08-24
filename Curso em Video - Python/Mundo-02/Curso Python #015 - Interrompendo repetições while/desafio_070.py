# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
    # se o usuário vai continuar ou não. No final, mostre:
'''
maisC = maisB = soma = q = 0
pbarato = continuar = ' '
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço R$ '))
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    soma += preco
    q += 1
    if preco > 1000:
        maisC += 1
    if q == 1 or preco < maisB:
        maisB == preco
        pbarato == produto
    if continuar == 'N':
        break
print(f'Total: {soma}.')
print(f'{maisC} do produtos custa acima de R$ 1.000,00.')
print(f'O mais barato é {pbarato} custando R$ {maisB}.')
'''

total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O toral da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
