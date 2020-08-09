import random

pr = str(input('Qual o nome do primeiro aluno? '))
sg = str(input('Qual o nome do segundo aluno? '))
tr = str(input('Qual o nome do terceiro aluno? '))
qu = str(input('Qual o nome do quarto aluno? '))
lista = [pr, sg, tr, qu]
esq = random.choice(lista)
print('E o sortudo foi, {}'.format(esq))