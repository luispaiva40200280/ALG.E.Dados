#ler um texto e mostrar em duas strings diferentes 

texto=input("insira o texto:")
comp=len(texto) #quantidade de caracteres que o texto tem

if texto[comp-1] != " ":
    texto= texto  + ","  #acrescenta "," no final

espaços=texto.count(" ") #conta quantas " " há no tesxto inserido
texto1=""   #1º str
texto2=""   #2º str
pos_ant=0  #posição anterior ???
for i in range(espaços):
    pos = texto.find(" ", pos_ant) #??? find(procura os " " )
    if i % 2 != 0: #espaços impares 
        texto1 = texto1 + " " + texto[pos_ant:pos-1]
    else:
        texto2 = texto2 + "" + texto[pos_ant:pos-1]

print(texto1)
print(texto2)
input()
#não esta a foncionar direito 
#??? perguntar ao prof 