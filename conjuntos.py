print("Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos. Os conjuntos são delimitados por chaves: {}, também podemos criá-los a partir da função set()")

moveis = {"cama", "guarda-roupa", "tv"}
numeros = set([1,2,3,4,5,6,7,8,9,10])

print("\nOs conjuntos suportam operações matemáticas de conjuntos, como a união (|), intersecção (&), diferença (-) e diferença simétrica (^)")

print()
conjunto1 = {1,2,3}
conjunto2= {3,4,5}

uniao = conjunto1 | conjunto2
print(uniao) #imprime {1,2,3,4,5}, os conjuntos não permitem repetições

interseccao = conjunto1 & conjunto2
print(interseccao) #imprime {3}

diferenca = conjunto1 - conjunto2
print(diferenca) #imprime a diferença entre o conjunto 1 e 2, resultando em: {1,2}

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica) #imprime todos os elementos que pertencem a um conjunto ou ao outro, mas que não pertencem a ambos. Neste caso. nosso resultado é: {1,2,4,5}

print()

print("Métodos de conjuntos\n")
cores = {"vermelho","amarelo","azul","roxo"}
print(cores)
cores.add("preto") #adiciona um elemento
print(cores)
cores.remove("azul") #remove um elemento existente, se não existir, gera um erro.
print(cores)
cores.discard("verde") #remove um elemento se o elemento existir, caso não exista, não faz nada.
print(cores)
cores.clear() #remove todos os elementos do conjunto
print(cores)