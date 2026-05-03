print("Funções são blocos de código reutilizáveis com tarefas específicas")
print()

print("Para definir uma função em Python, utilizamos def e em seguida o nome da função seguida por parênteses. \nExemplo: def function())")

def function():
    print("Função sendo executada")
function()

def saudacao(nome):
    print(f"Olá, {nome}!")
 
usuario = input("Digite seu nome: ")

saudacao(usuario)
print()

print("Valores de retorno:\n As funções podem retornar um valor usando a palavra-chave return")
def soma(a,b): 
    return a + b 

num1 = float(input("Digite o primeiro valor a ser somado: \n"))
num2 = float(input("Digite o segundo valor a ser somado: \n"))

resultado = num1 + num2

print(resultado) 
print()

print("Funções lambda: são formas concisas de criar pequenas funções anônimas em uma única linha, ideias para operações de uso único")
quadrado = lambda x: x **2
numero = float(input("Digite o número a ser elevado: "))
print(quadrado(numero))
print()


