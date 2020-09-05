'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento 
de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa 
que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a 
população do país B, mantidas as taxas de crescimento.
'''
a = 80000
b = 200000
c = 0
while True:
    a += (a / 100) * 3
    b += (b / 100) * 1.5
    c += 1
    if a >= b:
        break
#print(f'a = {a}\nb = {b}')
print(f'{c} anos')
