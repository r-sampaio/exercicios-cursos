# O mesmo professor do desafio anterios quer sortear a ordem de apresentação de trabalhos dos alunos.
    # * Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from math import shuffle
import os

os.system('cls')
primeiro = str(input('Qual o nome do primeiro aluno: '))
segundo = str(input('Qual o nome do segundo aluno: '))
terceiro = str(input('Qual o nome do terceiro aluno: '))
quarto = str(input('Qual o nome do quarto aluno: '))
# winner = shuffle([primeiro, segundo, terceiro, quarto])

winner = [primeiro, segundo, terceiro, quarto]
shuffle(winner)
print(winner)
