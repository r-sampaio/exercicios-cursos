# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
    # A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    # A mensagem "Reprovado", se a média for menor do que sete;
    # A mensagem "Aprovado com Distinção", se a média for igual a dez.

notas = [0, 0]
for i in range(0, 2):
    notas[i] = float(input(f'Digite a {i+1}ª nota: '))
media = (notas[0] + notas[1]) / 2
if media >= 7 and media < 10:
    result = 'Aprovado'
elif media < 7:
    result = 'Reprovado'
elif media == 10:
    result = 'Aprovado com Distinção'
print(f'Media: {media:.2f} = {result}')
