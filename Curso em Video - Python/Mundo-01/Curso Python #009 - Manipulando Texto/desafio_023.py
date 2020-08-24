# Faça um programa que leia de 0 a 9999 e mostra na tela cada um dos digitos separados.
    # * Ex: Digite um número: 1834
        # * unidade: 4
        # * dezena: 3
        # * centena: 8
        # * milhar: 1

numero = int(input('Digite um número '))
#num = str(numero)

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')