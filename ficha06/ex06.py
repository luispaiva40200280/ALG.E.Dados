#procutar numero em lista

def procurar(lista_numero):
    posicao=0
    for i in range (len(lista_numero)):
        posicao=lista_numero.index(numero)
        posicao+=1
    return posicao

lista_numero=[2,4,8,10,14,16,18,20]
numero=int(input("de a sua tentativa: "))
valor = procurar(lista_numero)
print(valor)
input()
