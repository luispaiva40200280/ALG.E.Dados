#em uma frase lê nº de caracters espaços e vogais
frase=input("escreve uma frase: ")
vogais=0
caracteres=len(frase)
for i in frase:
    if i.lower() == "a" or i.lower() == "e" or i.lower() == "i"or i.lower() == "o" or i.lower() =="u":
         vogais+=1

espaços=frase.count(" ")

print("há {0} vogais na texto".format(vogais))
print("numero de caracteres é: {0}" .format(caracteres))
print("numero de espaços é:{0}" .format(espaços))

input()

#esta correto