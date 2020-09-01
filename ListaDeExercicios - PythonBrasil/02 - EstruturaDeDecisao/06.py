# Faça um Programa que leia três números e mostre o maior deles.

maior = 0
lista = [0, 0, 0]
for i in range(0, 3):
    lista[i] = int(input(f'Digite o {i+1}º numero: '))
    if i == 0 or maior < lista[i]:
        maior = lista[i]
print(maior)
