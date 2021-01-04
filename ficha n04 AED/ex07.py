#procurar num texto o numero de vezes que uma palvra aparece

texto=input("texto:")
texto = " " + texto + " "
palavra=input("palavra?")
pesquisa = " " + palavra + " "

numero=texto.count(palavra)   #n de vezes que a palavra aparece
posição=0              #posição das palavras 
ant=0
for i in range(texto):
    posição=texto.find(palavra)
    if posição != -1:
        posição+= " " + str(posição+1)
        ant= posição  +1
    else:
        break

print("a palavra ocorre :", numero )
print("a posição no texto:", posição)

input()


