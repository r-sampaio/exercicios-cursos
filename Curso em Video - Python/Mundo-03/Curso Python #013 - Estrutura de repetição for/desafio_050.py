# Desenvolva um programa que leia seis números inteiros e mostre a soma
    # apenas daqueles que forem pares. Se o valor digitado for ímpar, deconsedere-o.

s = 0
c = 0
for i in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        s += numero
        c += 1
print(f'Foram digitados {c} numeros pares dando a soma de {s}.')
