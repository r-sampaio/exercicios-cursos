# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # a. o produto do dobro do primeiro com metade do segundo.
    # b. a soma do triplo do primeiro com o terceiro.
    # c. o terceiro elevado ao cubo.

inteiro1 = int(input('Digite um número inteiro: '))
inteiro2 = int(input('Digite outro número inteiro: '))
real = float(input('Digite um numero real: '))
a = (inteiro1 * 2) * (inteiro2 / 2)
b = (inteiro1 * 3) + (real)
c = pow(real, 3)

print(f'O produto do dobro do primeiro com metade do segundo: {a}')
print(f'A soma do triplo do primeiro com o terceiro: {b}')
print(f'O terceiro elevado ao cubo: {c}')
