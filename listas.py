frutas = ["maçã", "banana", "laranja", "uva"]

print(frutas[0])  # Acessa o primeiro elemento da lista
print(frutas[1])  # Acessa o segundo elemento da lista  
print(frutas[2])  # Acessa o terceiro elemento da lista
print(frutas[3])  # Acessa o quarto elemento da lista
# Acessando elementos usando índices negativos
print()
print(frutas[-1])  # Acessa o último elemento da lista  
print(frutas[-2])  # Acessa o penúltimo elemento da lista
print(frutas[-3])  # Acessa o antepenúltimo elemento da lista
print(frutas[-4])  # Acessa o quarto elemento da lista (mesmo que frutas[0])


print("\nmétodos de listas")
append = frutas.append("abacaxi")   # Adiciona um elemento ao final da lista
print(frutas)

insert = frutas.insert(3, "melancia")  # Insere um elemento em uma posição específica
print(frutas)

remove = frutas.remove("banana")  # Remove a primeira ocorrência de um elemento se estiver sem parênteses, com parênteses, remove o elemento na posição especificada
print(frutas)

pop = frutas.pop()  # Remove e retorna o último elemento da lista
print(frutas)

append = frutas.append("amora")  # Adiciona um elemento ao final da lista
sort = frutas.sort() # Ordena os elementos da lista em ordem alfabética
print(frutas)

reverse = frutas.reverse()  # Inverte a ordem dos elementos da lista
print(frutas)


print("\nLista de compreensão")
numeros = [1,2,3,4,5]
quadrados = []
for x in numeros:
    if x % 2 == 0:
        quadrados.append(x**2)
print(quadrados)

print("\nTuplas são listas imutáveis e ordenadas que armazena uma coleção de elementos, as tuplas não podem ser modificadas, ou seja, não podemos adicionar, remover, criar ou alterar a posição dos elementos.")
print("Tuplas começam e se encerram utilizando parênteses, e os elementos são separados por vírgula.")

ponto = (5,6)  # Criando uma tupla
print(ponto)
print(ponto[0]) #imprime 5
print(ponto[1]) #imprime 6

print()
print("\nMétodos de tuplas: formas de trabalhar com elas")

nova_tupla = (1,1,2,1,5,3,4,3,5,5)

print(nova_tupla.count(1)) #count(elemento) retorna quantas vezes o elemento apareceu na tela
print(nova_tupla.index(3)) #index(elemento) retorna a posição do primeiro elemento 
print(nova_tupla.index(3,5)) #no index também é possível determinar o intervalo, nesse exemplo, a busca vai começar a partir da quinta posição procurando o elemento 3 e imprimir o índice onde o elemento foi encontrado.
print(nova_tupla.index(5,3,9)) #Python vê isso de uma forma: valor, início da busca, fim da busca; Posteriormente, entrega a posição do número 5, nesse caso, a quarta posição.
print("\nPodemos utilizar a função 'len' para contar quantos elementos temos na nossa estrutura:")
len(nova_tupla)
print(len(nova_tupla))


   

