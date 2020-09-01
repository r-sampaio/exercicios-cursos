# Faça um Programa que peça dois números e imprima o maior deles.

numero = [0, 0]
for i in range(0, 2):
    numero[i] = int(input(f'Digite o {i+1}º número: '))
if numero[0] > numero[1]:
    num = numero[0]
else:
    num = numero[1]
print(num)
