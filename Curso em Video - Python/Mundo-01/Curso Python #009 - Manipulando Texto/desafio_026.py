# Faça um programa que leia uma frase pelo teclado e mostre:
    # Quantas vezes aparece a letra "A".
    # Em que posiçáo ela aparece a primeira vez.
    # Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print(frase.count('A'))
# print(frase.find('A'))
# print(frase.rfind('A'))

print(frase.find('A')+1)
print(frase.rfind('A')+1)