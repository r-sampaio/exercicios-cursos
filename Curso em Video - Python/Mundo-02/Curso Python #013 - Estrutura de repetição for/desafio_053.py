<<<<<<< HEAD:Curso em Video - Python/Mundo-02/Curso Python #013 - Estrutura de repetição for/desafio_053.py
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, deconsederando os espaços.
    # EX: (SEM ACENTOS)
    # APOS A SOPA                   APOSASOPA
    # A SACADA DA CASA              ASACADADACASA
    # A TORRE DA DERROTA            ATORREDADERROTA
    # O LOBO AMA O BOLO             OLOBOAMAOBOLO
    # ANOTARAM A DATA DA MARATONA   ANOTARAMADATADAMARATONA

nome = str(input('Digite uma frase: ')).upper().strip()
palavra = nome.split()
junto = ''.join(palavra)
inverso = junto[::-1]
# inverso = ''
# for i in range(len(junto) - 1, -1, -1):
#     inverso += junto[i]
print(junto, inverso)
if junto == inverso:
    print('É palindromo')
else:
    print('Não é palindromo')
=======
>>>>>>> parent of 643e711... update:Curso em Video - Python/Mundo-01/Curso Python #013 - Estrutura de repetição for/desafio_053.py
