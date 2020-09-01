# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = int(input('Digite um número: '))
if numero < 0:
    result = 'Negativo'
elif numero > 0:
    result = 'Positivo'
else:
    result = 'Neutro'
print(result)
