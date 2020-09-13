# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como 
# parâmetro e mostre uma mensagem com tamanho adaptável. 
# Ex: escreva(‘Olá, Mundo!’) Saída: 
# ~~~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~~~

def escreva(text):
    print('~' * len(text))
    print(text)
    print('~' * len(text))


texto = str(input('Digite uma frase: '))
escreva(texto)


# def escreva(msg):
#     tam = len(msg) + 4
#     print('~' * tam)
#     print(f'  {msg}')
#     print('~' * tam)


# #Programa Principal
# escreva('Gustavo Guanabara')
# escreva('Curso de Python no YouTube')
# escreva('CeV')
