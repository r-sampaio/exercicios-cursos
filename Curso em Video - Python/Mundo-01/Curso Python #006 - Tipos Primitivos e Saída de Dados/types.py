from funcoes import limpa
limpa()
v1 = input(' Digite o valor de um: ')
limpa()
v2 = int(input(' Digite o valor de dois: '))
limpa()
v3 = str(input(' Digite o valor de três: '))
limpa()
v4 = float(input(' Digite o valor de quatro: '))
limpa()
v5 = bool(input(' Digite o valor de cinco: '))
limpa()
print(f' O tipo de \033[33mum\033[m é: \033[34m{type(v1)}\033[m, e seu valor é \033[32m{v1}\033[m.')
print(f' O tipo de \033[33mdois\033[m é: \033[34m{type(v2)}\033[m, e seu valor é \033[32m{v2}\033[m.')
print(f' O tipo de \033[33mtrês\033[m é: \033[34m{type(v3)}\033[m, e seu valor é \033[32m{v3}\033[m.')
print(f' O tipo de \033[33mquatro\033[m é: \033[34m{type(v4)}\033[m, e seu valor é \033[32m{v4}\033[m.')
print(f' O tipo de \033[33mcinco\033[m é: \033[34m{type(v5)}\033[m, e seu valor é \033[32m{v5}\033[m.\n')
