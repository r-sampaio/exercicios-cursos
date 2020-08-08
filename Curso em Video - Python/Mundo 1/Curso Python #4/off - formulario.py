import os

def title():
    print('\033[34mPreencha logo abaixo:\033[m\n')

def result():
    print('\033[32mResultado:\033[m')

os.system('cls')
title()
nome = str(input('Qual seu nome? '))
os.system('cls')
title()
idade = int(input('Quantos anos você tem? '))
os.system('cls')
title()
peso = float(input('Qual seu peso? '))
os.system('cls')
result()
print(f'\nMeu nome é \033[31m{nome}\033[m, tenho \033[36m{idade}\033[m e peso \033[33m{peso}\033[m.\n')
