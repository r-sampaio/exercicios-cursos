'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade 
(em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

morango  = float(input('Quanto quilos de morandos deseja comprar? '))
maca = float(input('Quanto quilos de maçãs deseja comprar? '))
if morango <= 5.0:
    m1 = morango * 2.50
elif morango > 5.0:
    m1 = morango * 2.20
if maca <= 5.0:
    m2 = maca * 1.80
elif maca > 5.0:
    m2 = maca * 1.50
if (morango + maca) > 8.0:
    total = m1 + m2 - (((m1 + m2) / 100) * 10)
else:
    total = m1 + m2
print(f'O total da compra foi de {total}')
