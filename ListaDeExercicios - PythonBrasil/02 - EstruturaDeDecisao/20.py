'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média 
alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
nota = [0, 0, 0]
for i in range(0, 3):
    nota[i] = float(input(f'Digite o {i+1}º nota: '))
media = (nota[0] + nota[1] + nota[2]) / 3
if 7 <= media < 10:
    print(f'Aprovado com media {media:.2f}')
elif media < 7:
    print(f'Reprovado com media {media:.2f}')
elif media == 10:
    print(f'Aprovado com Distinção, media {media:.2f}')
