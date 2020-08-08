import random

pr = str(input('Primeiro aluno: '))
sg = str(input('Segundo aluno: '))
tr = str(input('Terceiro aluno: '))
qu = str(input('Quarto aluno: '))
sorteio = random.sample([pr, sg, tr, qu], k=4)
print('a ordem sera {}'.format(sorteio))
