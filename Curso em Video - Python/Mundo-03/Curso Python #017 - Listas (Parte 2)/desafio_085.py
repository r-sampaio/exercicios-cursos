# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
    # lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores 
    # pares e ímpares em ordem crescente.

lista = [[], []]
valor = 0
for i in range(1, 8):
    valor = (int(input('Digite um numero: ')))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(lista[0])
print(lista[1])
