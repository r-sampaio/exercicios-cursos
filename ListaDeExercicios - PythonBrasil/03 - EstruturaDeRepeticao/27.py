# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a 
# quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem 
# ter mais de 40 alunos.


soma = 0
turma = int(input('Digite a quantidade de turmas: '))
for i in range(turma):
    while True:
        q = int(input(f'Digite a quantidade da {i+1}ª turma: '))
        if q >= 0 and q < 40:
            break
    soma += q
total = soma / turma
print(f'Media de alunos é de {total}')
