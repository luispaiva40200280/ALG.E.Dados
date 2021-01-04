#media com funções
def media(valores):    #função media
     soma=0 
     for i in range(valores):
         soma+=numeros[i]
         media=soma/valores
     return media

valores = int(input("quantos argumentos:"))
for i in range(valores):
    numeros=int(input("valores inteiros:"))
media = media(valores)

print("a media é: {0}".format(media))

input()


