# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    # A média de idade do grupo.
    # Qual é o nome do homem mais velho.
    # Quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totalmulher = 0

for i in range(1, 5):
    print(f'{i} pessoa')
    nome = str(input('Nome: ')).upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'Ff' and idade > 20:
        totalmulher += 1
mediaidade = somaidade / 4
print(f'Media de idade {mediaidade}')
print(f'Homem mais velho tem {maioridadehomem} e seu nome é {nomevelho}')
print(f'Tem {totalmulher} de mulheres com menos de 20 anos.')
