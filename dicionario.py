print("Um dicionário é uma estrutura de dados mutável e não ordenada que armazena pares de chave-valor")
print("\nPara criar um dicionário , utilize chaves e separe as chaves e valores com dois pontos\n")
pessoa = {"nome":"Ellen", "idade":23, "cidade":"Belo Horizonte"}

print(pessoa["nome"]) #imprime "Ellen"
print(pessoa["idade"]) #imprime 24
print(pessoa["cidade"]) #imprime "Belo Horizonte"

print("\nMétodos de dicionários")

print(pessoa.keys()) #retorna uma visualização de todas as chaves do dicionário
print(pessoa.values()) #retorna uma visualização de todos os valores do dicionário 
print(pessoa.items()) #retorna uma visualização de todos os pares chave-valor do dicionário.
pessoa.update({"profissão":"Desenvolvedora"}) #atualiza valores já existentes, caso não exista, cria novos dados ao dicionário 
print(pessoa)