# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

a = b = c = 0
eleitores = int(input('Digite o número de eleitores: '))
for i in range(eleitores):
    print('1 - candidato A\n2 - candidato B\n3 - candidato C')
    opcao = int(input('Em qual candidato você irá votar? '))
    if opcao == 1:
        a += 1
    if opcao == 2:
        b += 1
    if opcao == 3:
        c += 1
print(f'Candidato A teve {a} votos.')
print(f'Candidato B teve {b} votos.')
print(f'Candidato C teve {c} votos.')
