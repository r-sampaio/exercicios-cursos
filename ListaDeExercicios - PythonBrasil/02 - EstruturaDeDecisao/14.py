'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo
de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
    Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0            A
	Entre 7.5 e 9.0             B
	Entre 6.0 e 7.5             C
	Entre 4.0 e 6.0             D
	Entre 4.0 e zero            E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem 
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''
av1 = float(input('Digite a nota da AV1: '))
av2 = float(input('Digite a nota da AV2: '))
media = (av1 + av2) / 2
print(f'AV1: {av1}, AV2: {av2}, Media: {media} ', end='')
if 9.0 < media <= 10.0:
    conceito = 'A'
elif 7.5 < media <= 9.0:
    conceito = 'B'
elif 6.0 < media <= 7.5:
    conceito = 'C'
elif 4.0 < media <= 6.0:
    conceito = 'D'
elif 4.0 > media >= 0:
    conceito = 'E'
print(f'- Conceito {conceito}, ', end='')
if conceito in 'ABC':
    print('APROVADO.')
elif conceito in 'DE':
    print('REPROVADO.')
