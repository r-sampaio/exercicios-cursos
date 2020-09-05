'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de 
números pares e a quantidade de números impares.
'''
par = []
impar = []
cPar = 0
cImpar = 0
for i in range(0, 10):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        cPar += 1
        par.append(num)
    else:
        cImpar += 1
        impar.append(num)
print(f'Quntidade de numero pares: {cPar} - {par}')
print(f'Quntidade de numero impares: {cImpar} - {impar}')
