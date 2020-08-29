# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
    # extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
    # Ao final, mostre o conteúdo das três listas geradas.

lista = []
impar = []
par = []
while True:
    lista.append(int(input('Digite um numero: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
for i in lista: # for i, v in enumerate(lista):
    if i % 2 == 0:
        par.append(i)
    elif i % 2 == 1:
        impar.append(i)
print(f'Lista de numero digitados: ',end='')
for i in lista:
    print(i, end=' ')
print()
print(f'Valores pares: ',end='')
for i in lista:
    print(i, end=' ')
print()
print(f'Valores impares: ',end='')
for i in lista:
    print(i, end=' ')
print()
