# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa 
# que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor 
# e a maior temperaturas informadas, bem como a média das temperaturas.


maior = menor = media = 0
soma = cont = 0
while True:
    temperatura = float(input('Temperatura: '))
    if cont == 0:
        maior = temperatura
        menor = temperatura
    elif temperatura > maior:
        maior = temperatura
    elif temperatura < menor:
        menor = temperatura
    cont += 1
    soma += temperatura
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

r = soma / cont

print(f'''
      Maior temperatura: {maior}
      Menor temperatura? {menor}
      Media: {r:.2f}
      Valores digitados: {cont}
      ''')
