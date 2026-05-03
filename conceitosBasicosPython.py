print('Olá, mundo! Esta frase foi escrito com Python.')

#pyhton distingue maiúsculas de minúsculas
#não requer uso de ponto e vírgula

print("Phyton utiliza do tipo de dados básicos, sendo eles: " "\n"
"Int (Inteiros, sem parte decimal. Ex: Idade = 25, sem aspas); " "\n"
"Float (flutuantes, contém parte decimal. Exemplo: preço = 9.99, utiliza-se de ponto final para separar); " "\n"
"Strings (cadeias de texto entre aspas simples ou duplas para representar textos. Exemplo: nome = ""Lucas"") " "\n"
"e Booleanos (True or False, valores de verdade utilizados em expressões de condição ou operações Lógicas. Exemplo: é_de_maior = True tem_desconto = False)")

#os valores booleanos em phyton começam com letra maiúscula
#as váriaveis são espaços reservados na memória
#o operador de atribuição de variável é o = , a esquerda do operador vai o nome da variável e a direita o valor atribuido, exemplo: altura = 1.75

print('operadores aritmeticos')
a = 6
b = 3
c = 2
d = 2.5

soma = a + b 
print(soma)
 
subtracao = b - c
print(subtracao)

multiplicacao = b * a
print(multiplicacao)

divisao = a/c 
print(divisao)

divisao_inteira = a//d 
print(f"{divisao_inteira} Descarta a parte decimal")

modulo = a%d
print(f"{modulo} devolve o resto da divisão entre o primeiro valor e o segundo.")

exponenciacao = b**c
print(f"{exponenciacao} eleva o primeiro valor à potência do segundo.")

print('operadores de comparação')

e = 34
f = 15

igual  = e == f 
print(f"{igual} devolve True se ambos os valores forem iguais")

diferente_de = e != f 
print(f"{diferente_de} devolve True se os valores forem diferentes")

maior_que = e > f 
print(f'{maior_que} devolve True se o primeiro valor for maior que o segundo')

menor_que = e < f 
print(f"{menor_que} devolve True se o primeiro número fro menor que o segundo")

maior_ou_igual = e >= f 
print(f"{maior_ou_igual} imprime True quando o primeiro valor é maior ou igual ao segundo")

menor_ou_igual = e <= f
print(f"{menor_ou_igual} devolve True se o primeiro valor for menor ou igual ao segundo")

print("operadores lógicos")

#os operadores lógicos servem para combinar, avaliar ou inverter multiplas expressões booleanas

g = 30
h = 8

resultado_and = (g > 5) and (h < 5) 
print(f'{resultado_and} devolve True se ambas forem verdadeiras')

resultado_or = (g > 15) or (h < 5)
print(f'{resultado_or} devolve True se ao menos uma condição for verdadeira')

resultado_not = not (g > 5)
print(f"{resultado_not} devolve True se for False e devolve False se for True, inverte o valor de uma condição")
