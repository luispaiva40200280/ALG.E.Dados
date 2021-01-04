#fundir duas lista sem numero repetidodos
def remover(lista):
    lista1=[]
    for i in lista:
        if i not in lista1: #se ainda não estiverem na lista 
            lista1.append(i) #adiciona os numeros na lista
    return lista1

def remover_2lista(listan):
    lista2=[]
    for i in listan:
        if i not in lista2:
            lista2.append(i)
    return lista2
def junt_listas(lista1,num_lista2):
    lista_final=[]
    for i in range(2*numero):
        lista_final.append(naorepetida,lista_nrepentida)
    return lista_final

listan=[]
lista= []
numero=int(input("N: "))
for i in range(numero):
    num=int(input("numeros: "))
    lista.append(num)
    num_lista2=int(input("elementos: "))
    listan.append(num_lista2)

naorepetida= remover(lista)  #lista1
lista_nrepentida= remover(listan)  #lista2
listaf=junt_listas(lista1,num_lista2) #listafinal

print(naorepetida)
print(lista_nrepentida)
print(listaf)
input()