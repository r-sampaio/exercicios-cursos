# Faça um programa que leia nome e média de um aluno, guardando também a situação 
# em um dicionário. No final, mostre o conteúdo da estrutura na tela.

escola = dict()
lista = list()
escola['nome'] = str(input('Digite o nome: '))
escola['media'] = float(input('Digite a media: '))
if escola['media'] >= 7.0:
    escola['situacao'] = 'Aprovado'
else:
    escola['situacao'] = 'Reprovado'
lista.append(escola.copy())
for k, v in escola.items():
    print(f'{k} é {v}')



# aluno = dict()
# aluno['nome'] = str(input('Nome: '))
# aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
# if aluno['media'] >= 7:
#     aluno['sitacao'] = 'Aprovado'
# elif 5 <= aluno['media'] and aluno['media'] < 7:
#     aluno['sitacao'] = 'Recuperacao'
# else:
#     aluno['sitacao'] = 'Reprovado'
# print()
# for k, v in aluno.items():
#     print(f' - {k} é igual a {v}')
