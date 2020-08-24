# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
    # o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
    # A) quantas pessoas tem mais de 18 anos.
    # B) quantos homens foram cadastrados.
    # C) quantas mulheres tem menos de 20 anos.

h = m = i = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    if idade > 18:
        i += 1
    elif sexo == 'M':
        h += 1
    elif sexo == 'F' and idade < 20:
        m +=1
    stop = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if stop == 'N':
        break
print(f'Tem {i} pessoas com mais de 18 anos, {h} homems e {m} mulheres com menos de 20 anos.')
