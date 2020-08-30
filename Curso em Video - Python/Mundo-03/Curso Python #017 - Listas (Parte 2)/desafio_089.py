# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
    # No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as 
    # notas de cada aluno individualmente.

import os
lista = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = str(input('Continuar? '))
    if continuar in 'Nn':
        break
os.system('cls')
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print(f'-'*26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print(f'-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
