# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a 
# temperatura em graus Celsius. C = 5 * ((F-32) / 9).

fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
#celsius = (fahrenheit - 32) * 5 / 9
celsius = 5 * ((fahrenheit - 32) / 9)
print(f'A temperatura de {fahrenheit}°F equivale a aproximadamente {celsius:.2f}°C.')
