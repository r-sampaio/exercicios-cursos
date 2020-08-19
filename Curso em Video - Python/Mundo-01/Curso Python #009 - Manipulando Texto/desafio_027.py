# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
    # o primeiro e o último nome separadamente.
        # Ex: Ana Maria de Souza
        # primreiro : Ana
        # ultimo: Souza

nome = str(input('Qual seu nome completo? '))
dividido = nome.split()
print(dividido[0])
print(dividido[len(dividido)-1])
