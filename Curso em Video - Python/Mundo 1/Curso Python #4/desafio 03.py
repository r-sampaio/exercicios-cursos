from funcoes import limpa

limpa()
n1 = int(input('Digite um numero: '))
limpa()
n2 = int(input('Digite outro numero: '))
limpa()
print(f'A soma de \033[34m{n1}\033[m mais \033[34m{n2}\033[m é: \033[32m{n1 + n2}.\033[m\n')
