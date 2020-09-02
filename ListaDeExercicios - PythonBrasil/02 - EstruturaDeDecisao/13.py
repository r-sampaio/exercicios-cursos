'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''
print('1 - Domingo')
print('2 - segunda-feira')
print('3 - terça-feira')
print('4 - quarta-feira')
print('5 - quinta-feira')
print('6 - sexta-feira')
print('7 - sábado')
dia = str(input('Dia: '))
if dia in '1':
    print('Domingo')
elif dia in '2':
    print('Segunda-feira')
elif dia in '3':
    print('Terça-feira')
elif dia in '4':
    print('Quarta-feira')
elif dia in '5':
    print('Quinta-feira')
elif dia in '6':
    print('Sexta-feira')
elif dia in '7':
    print('Sábado')
else:
    print('Valor inválido')