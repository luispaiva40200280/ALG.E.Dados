#encontrar um n numa lista sem o uso de funçao
lista=[10,20,30,40,50,60.70,80,90,100]
numero=int(input("numero:"))
for i in range (len(lista)):
    posição =lista.index(numero)
    posição+=1



print(posição)
input()