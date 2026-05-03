print("Um módulo é um arquivo que contém definições e funções, classes e variáveis que podem ser utilizadas em outros programas.")
print()
print("Para utilizarmos um módulo em nosso programa, devemos importá-lo utilizando a declaração import.")
print()

import math 

resultado = math.sqrt(25) #math.sqrt calcula a raiz quadrada de um número positivo.
print(resultado) #imprime 5.0

print("Poderíamos também importar funções específicas de um módulo utilizando a sintaxe from módulo import sqrt")

from math import sqrt

results = sqrt(25)
print(results) #imprime 5.0

print()

print("Funções e classes de módulos padrão")
print('Os módulos com funções e classes úteis mais comuns da biblioteca Python são:\n Math: Fornece funções matemáticas, como sqrt() (raiz quadrada), sin() (seno), cos() (cosseno), entre outras.; \nRandom: Oferece funções para gerar números aleatórios, como random() (número aleatório entre 0 e 1), randint() (número inteiro aleatório em um intervalo), entre outras.; \nDatetime: Permite trabalhar com datas e horas, como datetime.now() (data e hora atual), datetime.date() (data), datetime.time() (hora), entre outras.')

import random 
import datetime

numero_aleatorio = random.randint(1,45)
print(numero_aleatorio) #imprime um número aleatório entre 1 e 45

data_atual = datetime.datetime.now()
print(data_atual) #imprime a data e a hora atual

hora_atual = data_atual.strftime("%H:%M:%S") #extrai de datetime.date.time.now() apenas hora, minuto e segundo.
print(f'Horário: {hora_atual}') #imprime a hora atual

print("Criando nossos próprios módulos: Além de utilizar módulos, também podemos criá-los.")
print("""Para criar um módulo personalizado, simplesmente criamos um novo arquivo Python com o nome desejado e definimos as funções, classes e variáveis que queremos incluir no módulo. Por exemplo, criamos um arquivo (no mesmo diretório onde estamos executando Python) chamado meu_modulo.py com o seguinte conteúdo:

# meu_modulo.py
def saudar(nome):
    print(f"Olá, {nome}!")


def calcular_soma(a, b):
    return a + b

Depois, podemos importar e utilizar as funções definidas em meu_modulo.py em outro arquivo Python.

import meu_modulo

meu_modulo.saudar("João")  # Imprime "Olá, João!"
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado)  # Imprime 8

Neste exemplo, importa-se o módulo meu_modulo e utilizam-se as funções saudar() e calcular_soma() definidas nele.""")

print("""Criar e utilizar pacotes

Para criar um pacote, criamos um diretório com o nome desejado e adicionamos um arquivo especial chamado __init__.py dentro do diretório. Este arquivo pode estar vazio ou conter código de inicialização do pacote.

Por exemplo, criamos um diretório chamado meu_pacote com a seguinte estrutura:

meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py

Depois, podemos importar e utilizar os módulos do pacote em nosso programa.

from meu_pacote import modulo1, modulo2

modulo1.funcao1()
modulo2.funcao2()

Neste exemplo, são importados os módulos modulo1 e modulo2 do pacote meu_pacote e são utilizadas as funções definidas neles.

A importação e criação de módulos e pacotes em Python nos permite organizar e reutilizar nosso código de maneira eficiente. Ao modularizar nosso código, podemos manter um código mais legível, estruturado e fácil de manter.

Lembre-se de explorar a biblioteca padrão de Python e aproveitar os módulos existentes, que podem facilitar muitas tarefas comuns. Além disso, não hesite em criar seus próprios módulos e pacotes para organizar e reutilizar seu código de maneira eficaz.""")
