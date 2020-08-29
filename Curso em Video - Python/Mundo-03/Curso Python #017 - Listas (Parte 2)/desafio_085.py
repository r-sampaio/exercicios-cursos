# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
    # lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores 
    # pares e ímpares em ordem crescente.

lista = []
temp = []
for i in range(1, 8):
    temp.append(int(input('Digite um numero: ')))
    if temp[0] % 2 == 0:
        lista.insert(0, temp)
    else:
        lista.insert(1, temp)
    temp.clear()
print(lista[0])
print(lista[1])
