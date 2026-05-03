print("Erros comuns em Python:\n")
print("SyntaxError: Ocorre quando o código não segue as regras de sintaxe do Python, como inserir ponto e vírgula no fim da função ou esquecer dois pontos.\n")
print("NameError: Ocorre quando realizamos menção a uma variável não definida,\n")
print("TypeError: Ocoore quando tentamos realizar uma operação com tipos de dados incompatíveis, como tentar somar um número e uma string.\n")
print("IndexError: Ocorre quando tentamos acessar um índice fora do intercalo válido de uma lista ou sequência.\n")

print()
print("Manejos de erros: como capturar e lidar") 
print("Try: É onde colocamos o código que pode causar um erro (exceção). Python tentará executar esse bloco. Se nada der errado, o programa ignora o except e segue em frente")
print("Except: É executado apenas se um erro (exceção) ocorrer dentro do bloco try. Podemos especificar que tipo de erro queremos capturar (como por exemplo, ValueError) para fornecer mensagems de erro mais precisas e até mesmo amigáveis.")
print(f"Finally: É um bloco que sempre é executado, não importa se houve erro ou não no try. É ideal para \"limpeza\", como fechar um arquivo aberto, encerrar uma conexão com o BD, ou liberar recursos.")
print()
try: 
    resultado =10/2 
except ZeroDivisionError:
    print("Erro!")
else: 
    print(f"Sucesso! o resultado é: {resultado}")
finally: 
    print("Finalizando processamento.")

print("Exceções personalizadas: Além das exceções (subentende-se erro) fornecidas pelo Python, podemos criar as nossas próprias. Para realizar esta ação, precisamos criar uma classe que herde da classe base Exepction ou de uma de nossas subclasses")

condicao = True
def funcao():
    if condicao:
        raise Exception("A condição falhou, erro interno.")

try: 
    funcao()
except Exception as e:
        print(f"Erro: {str(e)}")
