# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o 
    # maior e o menor valor digitado e as suas respectivas posições na lista.

cont = menor = maior = posicao = 0
lista = []
ma = []
me = []
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
            me.append(p)
        elif maior <= valor:
            maior = valor
            ma.append(p)
print(ma)
print(me)
print(f'Lista digitada {lista}')
print(f'Menor valor {menor} na posição ')
for i in me:
    print(i, end=' ')
print(f'Maior valor {maior} na posição ')
for i in ma:
    print(i, end=' ')
