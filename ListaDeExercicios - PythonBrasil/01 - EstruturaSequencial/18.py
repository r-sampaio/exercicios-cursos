# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um 
# link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando 
# este link (em minutos).

arquivo = float(input('Digite o tamanho do arquivo em MB: '))
velocidade = float(input('Digite a velocidade da internet em Mbps: '))
tempo = arquivo / (velocidade / 8)
print(f'O arquivo de {arquivo}MB irá levar {tempo} segundos para ser baixado.')
