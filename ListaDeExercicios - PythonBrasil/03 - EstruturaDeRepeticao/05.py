'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de 
crescimento iniciais. Valide a entrada e permita repetir a operação
'''
a = int(input('Quantos habitantes tem na cidade A? '))
t1 = float(input('Digite a taxa de crescimento da cidade A: '))
b = int(input('Quantos habitantes tem na cidade B? '))
t2 = float(input('Digite a taxa de crescimento da cidade B: '))
c = 0
while True:
    a += (a / 100) * t1
    b += (b / 100) * t2
    c += 1
    if a >= b:
        break
#print(f'a = {a}\nb = {b}')
print(f'Levará {c} anos')
