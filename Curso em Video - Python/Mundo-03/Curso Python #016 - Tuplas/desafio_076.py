# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
    # No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Guitarra', 2000, 'Celular', 3000, 'Mochila', 200, 'Cadeira', 4546, 'Casa', 100, 'Carro', 1000)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'R${lista[i]:>7.2f}.')
