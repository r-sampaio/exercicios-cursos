# Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = b = c = 0
temp1 = int(input(f'Digite o 1º numero: '))
temp2 = int(input(f'Digite o 2º numero: '))
temp3 = int(input(f'Digite o 3º numero: '))
if temp1 > temp2 > temp3:
    a = temp1
    b = temp2
    c = temp3
elif temp2 > temp3 > temp1:
    a = temp2
    b = temp3
    c = temp1
elif temp3 > temp1 > temp2:
    a = temp3
    b = temp1
    c = temp3
elif temp3 > temp2 > temp1:
    a = temp3
    b = temp2
    c = temp1
elif temp2 > temp1 > temp3:
    a = temp2
    b = temp1
    c = temp3
print(a, b, c)