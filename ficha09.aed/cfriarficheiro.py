# criação de ficheiro
arquivo = open(input('Nome do arquivo a ser editado:'), 'r')  
texto = arquivo.readlines()  
texto.append(input('Insira o texto:'))
arquivo = open(input('Nome do arquivo a ser editado:'), 'w')
arquivo.writelines(texto)
arquivo.close()

try:
    nome_arquivo = input('Nome do arquivo a ser editado:')
    arquivo = open(nome_arquivo, 'r+')
except FileNotFoundError:
    arquivo = open(nome_arquivo, 'w+')
    arquivo.writelines('Arquivo criado pois nao existia')
#faca o que quiser
arquivo.close()

if os.path.isfile(diretorio):
      ...
      ficheiro = open(diretorio, "w") # criamos/abrimos o ficheiro
      #.... .... ... operacoes no ficheiro
      ficheiro.close()
 
input()