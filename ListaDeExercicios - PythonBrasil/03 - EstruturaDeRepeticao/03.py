# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = str(input('Digite seu nome: '))
    if len(nome) > 3:
        break
    else:
        print('Nome invalido... Tente novamente.')
while True:
    idade = int(input('Digite sua idade: '))
    if 0 <= idade <= 150:
        break
    else:
        print('Idade invalida... Tente novamente.')
while True:
    salario = float(input('Digite seu salario: '))
    if salario > 0:
        break
    else:
        print('Salário invalido... Tente novamente.')
while True:
    sexo = str(input('Digite seu sexo [F/M]: '))
    if sexo in 'FfMm':
        break
    else:
        print('Sexo invalido... Tente novamente.')
while True:
    print('''S - Solteiro(a)\nC - Casado(a)
V - Viuvo(a)\nD - Divorciado(a)''')
    estadoCivil = str(input('Digite seu Estado Civil: ')).upper().strip()[0]
    if estadoCivil in 'SCVD':
        break
    else:
        print('Estado Civil invalido... Tente novamente.')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: {salario:.2f}')
if sexo in 'Ff':
    sexo = 'Feminino'
    if estadoCivil in 'S':
        estadoCivil = 'Solteira'
    elif estadoCivil in 'C':
        estadoCivil = 'Casada'
    elif estadoCivil in 'V':
        estadoCivil = 'Viuva'
    elif estadoCivil in 'D':
        estadoCivil = 'Divorciada'
else:
    sexo = 'Masculino'
    if estadoCivil in 'S':
        estadoCivil = 'Solteiro'
    elif estadoCivil in 'C':
        estadoCivil = 'Casado'
    elif estadoCivil in 'V':
        estadoCivil = 'Viuvo'
    elif estadoCivil in 'D':
        estadoCivil = 'Divorciado'
print(f'Sexo: {sexo}')
print(f'Estado Civil: {estadoCivil}')
