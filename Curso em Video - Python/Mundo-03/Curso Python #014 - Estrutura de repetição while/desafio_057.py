# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
    # peça a digitação novamente até ter um valor correto.

sexo = '1'
while sexo not in 'MFmf':
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    while sexo in 'MFmf':
        print(f'Você digitou o sexo {sexo}')
        break
    while sexo not in 'MFmf':
        print(f'Você digitou um sexo invalido.')
        break

'''
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MFmf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
'''