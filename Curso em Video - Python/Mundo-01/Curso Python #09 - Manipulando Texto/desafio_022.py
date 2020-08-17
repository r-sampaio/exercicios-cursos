# Crie um programa que leia o nome completo de uma pessoa e mostre:
    # * O nome com todas as letras maíusculas.
    # * O nome com todas minúsculas.
    # * Quantas letras ao todo (sem conseferar escaços).
    # * Quantas letras tem o primeiro nome.

nome = str(input('Qual o seu nome? '))
print(nome.upper())
print(nome.lower())
nomeDividido = nome.split()
print(len(nomeDividido)
print((len((nomeDividido)[0]))