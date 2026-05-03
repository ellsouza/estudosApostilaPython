print("Podemos ler e escrever dados em arquivos externos com Python.")

arquivo = open("dados.txt", "r") #("r") nos permite ler o arquivo
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

print()

arquivo = open("dados.txt", "w") #("w") nos permite escrever em um arquivo.
arquivo.write('Fui escrito com o modo de escrita ("w") do Python.')
arquivo.close()

print()

print('Para escrevermos no arquivo sem deletar o que já está escrito, utilizamos ("a"), append. O modo append preserva o arquivo e escreve em seu final.\n')
with open("dados.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write('\nFui escrito com o modo append ("a") do Python')
      
print()
print('Recomenda-se o uso de "with open (...)" para garantir o fechamento automtico do arquivo.')

