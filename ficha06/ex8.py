#criar uma lista sem valores duplicados
def remover(lista):
    lista1=[]
    for i in lista:
        if i not in lista1:
            lista1.append(i) #adiciona os numeros na lista
    return lista1          #se ainda não estiverem na lista 


lista= []
numero=int(input("N:"))
for i in range(numero):
    num=int(input("numeros:"))
    lista.append(num)
naorepetida= remover(lista)
print(lista)
print(naorepetida)
input()









