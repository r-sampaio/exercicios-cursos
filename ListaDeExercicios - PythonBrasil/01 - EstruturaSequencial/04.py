# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

s = 0
for i in range(0, 4):
    n = float(input(f'Digite a {i+1}ª nota: '))
    s += n
r = s / 4
print(f'A media do aluno foi {r}')
