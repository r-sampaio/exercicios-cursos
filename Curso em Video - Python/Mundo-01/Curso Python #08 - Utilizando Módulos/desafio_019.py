# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
    # * Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
import os

os.system('cls')
primeiro = str(input('Qual o nome do primeiro aluno: '))
segundo = str(input('Qual o nome do segundo aluno: '))
terceiro = str(input('Qual o nome do terceiro aluno: '))
quarto = str(input('Qual o nome do quarto aluno: '))

# lista = [primeiro, segundo, terceiro, quarto]
# winner = choice(lista)

winner = choice([primeiro, segundo, terceiro, quarto])
print(f'{winner}')
