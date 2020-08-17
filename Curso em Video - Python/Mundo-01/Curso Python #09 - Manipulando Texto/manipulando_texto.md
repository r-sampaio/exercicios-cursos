# Manipulando Texto

* Python é uma linguagem case-sensitive.

```python
frase = 'Curso em Vídeo Python'
```
```
frase
| C | u | r | s | o |   | e | m |   | V | í | d | e | o |   | P | y | t | h | o | n |
  0...............................................................................20

Possuí 21 caracteres começando a contagem do 0
```

# Fatiamento

``` python
>> print(frase(9))
>> V
```
* Mostra o conteúdo do decimo espaço da memória começando a contagem no 0.

#############################################################################################

``` python
>> print(frase(9:13))
>> Víde
```
* O python para na casa de número informado, mas não mostra seu conteúdo.

#############################################################################################

``` python
>> print(frase(9:21))
>> Vídeo Python
```
* Colocar um número acima do limite, funciona, mas não é a melhor maneira de fatiar a lista.

#############################################################################################

``` python
>> print(frase(9:21:2))
>> VdoPto
```
* Mostra o conteúdo de pulando de dois em dois.

#############################################################################################

``` python
>> print(frase(::2))
>> Croe íe yhn
```
* Mostra o conteúdo do início ao fim pulando de dois em dois.

#############################################################################################

``` python
>> print(frase(:5))
>> Curso
```
* Quando omite o início ele começa no 0.

#############################################################################################

``` python
>> print (frase(15:))
>> Python
```
* Quando omite o final ele mostra o conteúdo ate o final.

#############################################################################################

``` python
>> print (frase(9::3))
>> VeoPh
```
* Vai começar no 9 indo ate o final pulando de três em três.

#############################################################################################

# Análise

``` python
>> print (len(frase))
>> 21
```
* Mostra o comprimento da frase (espaços).

#############################################################################################

``` python
>> print (frase.count('o'))
>> 3
```
* Mostra a quantidade vê vezes que aparece a letra “o” minúscula.

#############################################################################################

``` python
>> print (frase.uper().count('O'))
>> 
```
* Pega a frase joga para minúscula e conta quanto “O” maiúsculo tem.

#############################################################################################

``` python
>> print (frase.count('o', 0, 13))
>> 1
```
* Contagem com fatiamento, do 0 ao 13 a apenas 1 letra “o”.

#############################################################################################

``` python
>> print (frase.find('deo'))
>> 11
```
* Procura e mostra onde começa o que foi buscado.

#############################################################################################

``` python
>> print (frase.find('Android'))
>> -1
```
* Se não achar ele retorna -1.

#############################################################################################

``` python
>> print (frase.lower().find('vídeo'))
>> 9
```
* Joga tudo para minúsculo e mostra onde começa.

#############################################################################################

``` python
>> print ('Curso' in frase)
>> True
```
* Busca se existe a string na frase e mostra True ou False.

#############################################################################################

# Transformação

``` python
>> #frase.replace('Python', 'Android')
>> frase = 'Curso em Vídeo Python'
>> frase = frase.replace('Python', 'Android') # Sobrescreve a variável mudando a string .
>> print (frase)
>> Curso em Vídeo Android
```
* Procura e substituí (de uma forma secundaria, não diretamente na string) uma string por outra e adapta o tamanho se necessário.

#############################################################################################

``` python
>> print (frase.upper())
>> CURSO EM VÍDEO PYTHON
```
* Pega o que estava em minuscula e joga para maiúscula mantendo os que já estavam maiúsculas.

#############################################################################################

``` python
>> print (frase.lower())
>> curso em vídeo python
```
* Pega o que estava em maiúscula e joga para minuscula mantendo os que já estavam minuscula.

#############################################################################################

``` python
>> print (frase.capitalize())
>> Curso em vídeo python
```
* Pega toda a string e joga para minuscula e apenas a primeira para maiúscula.

#############################################################################################

``` python
>> print (frase.title())
>> Curso em vídeo python
```
* Pega toda a string separa pelos espaços e joga para minúscula e apenas a primeira letra de cada palavra para maiúscula.

```
frase
|   |   | A | p | r | e | n | d | a |   | P | y | t | h | o | n |   |   | 
  0...................................................................18
```

#############################################################################################

``` python
>> print (frase.strip()) # Retira os espaços das bordas.
>> Aprenda Python
```
```
frase
| A | p | r | e | n | d | a |   | P | y | t | h | o | n |
  0...................................................14
```

#############################################################################################

``` python
>> print (len(frase.strip()))
>> 14
```
* Retira os espaços e conta.

#############################################################################################

``` python
>> print (frase.rstrip()) # Retira os espaços da direita.
>>   Aprenda Python
```
```
frase
|   |   | A | p | r | e | n | d | a |   | P | y | t | h | o | n |
  0...........................................................16
```

#############################################################################################

``` python
>> print (frase.lstrip()) # Retira os espaços da esquerda.
>> Aprenda Python  
```
```
frase
| A | p | r | e | n | d | a |   | P | y | t | h | o | n |   |   |
  0...........................................................16
```

#############################################################################################

``` python
>> print (frase.split()) # Separa pelo espaço uma lista gerando outras para cada palavras.
>> ['Curso', 'em', 'Vídeo', 'Python']
```
``` python
>> frase = 'Curso em Vídeo Python'
>> dividido = frase.split()
>> print (dividido[0]) # Mostra apenas a lista desejada.
>> Curso
```
``` python
>> frase = 'Curso em Vídeo Python'
>> dividido = frase.split()
>> print (dividido[2][3]) # Busca na lista 2 o que esta no espaço 3.
>> e
```

```
frase
| C | u | r | s | o |   | e | m |   | V | í | d | e | o |  | P | y | t | h | o | n |
  0...............4       0...1       0...............4      0...................5
```

#############################################################################################


``` python
>> print ('-'.join(frase)) # Preenche com o carácter desejado no caso um traço.
>> Curso-em-Vídeo-Python 
```
```
frase
| C | u | r | s | o |   | e | m |   | V | í | d | e | o |  | P | y | t | h | o | n |
  0...............4       0...1       0...............4      0...................5
         0                  1                2                         3 
```

```
frase
| C | u | r | s | o | - | e | m | - | V | í | d | e | o | - | P | y | t | h | o | n |
  0..............................................................................20
