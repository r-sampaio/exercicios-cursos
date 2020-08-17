# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Em qual cidade você nasceu? ')).upper().strip()
cidade = cidade.split()
print('SANTO' in cidade[0])
#print(cidade[:5] == 'SANTO')