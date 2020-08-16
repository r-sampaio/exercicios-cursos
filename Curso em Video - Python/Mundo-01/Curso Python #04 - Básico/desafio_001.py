# Crie um script em Python que leia o nome de uma pessoa e mostre 
    # uma mensagem de boas-vindas de acordo com o valor digitado.

from funcoes import limpa, title, result

limpa()
title()
nome = input('Qual o sue nome? ')
limpa()
result()
print('Seja bem-vindo, {}.\n'.format(nome))
