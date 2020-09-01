# Faça um Programa que leia três números e mostre o maior e o menor deles.

maior = menor = 0
lista = [0, 0, 0]
for i in range(0, 3):
    lista[i] = int(input(f'Digite o {i+1}º numero: '))
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    elif maior < lista[i]:
        maior = lista[i]
    elif maior > lista[i]:
        menor = lista[i]
print(f'Maior: {maior}, menor: {menor}')
