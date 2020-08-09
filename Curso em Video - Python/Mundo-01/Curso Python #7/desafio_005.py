from funcoes import limpa, title, result

limpa()
title()
num = int(input('Digite um numero inteiro: '))
limpa()
result()
print(f'Você digitou "\033[33m{num}\033[m", seu antecessor é \033[34m{num-1}\033[m e seu sucessor é \033[32m{num+1}\033[m.\n')
