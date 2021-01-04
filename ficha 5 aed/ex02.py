#palavras repetidas
def palavras(texto):
    texto = texto + " "
    cont_repetidas = 0
    pos =texto.find(" ")
    while pos != 0:   #enq houver espaços
        palavra = texto[0:pos+1] #obter a palavra + o espaço
        ocorrencias = texto.count(palavra) #verifica se ocorre no texto a palavra
        if ocorrencias > 1:
            cont_repetidas+=1
        texto = texto.replace(palavra, "")  #substitui a palavra por um vazio
        pos = texto.find("")
    return cont_repetidas


texto=input("escreve um texto:")
cont = palavras(texto) #variavel de todas as palavras do texto
print("nº de palavras repetidas :", cont)

input()