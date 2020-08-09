d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos KM foram rodados? '))
t = (d*60)+(km*0.15)
print('Total a pagar sera de R${:.2f}'.format(t))