#matrix com menu: (valor max); (list trans)
import os
import random
#1 
def criar_lista(): 
    lista = []
    dimen = int(input("dimenção da matriz: "))
    for i in range(dimen):
        lista.append([])
        for j in range(dimen):
            numero = random.randint(10,100)
            lista[i].append(numero)
    print()
    print("lista:")
    for linha in lista:
        print(linha)
    input()
    return lista
#2
def transposta(lista):
    if lista == []:
        print("não ha lista")
        input()
        return

    print("\t\n  lista transposta:")
    for j in range(len(lista)):
        for i in range(len(lista)):
            print(lista[j][i], end =" ")
    return
#3
def maximo(lista):
    if lista == []:
        print("não ha lista")
        input()
        return
    
    maximo = []
    for i in range(len(lista)):
        maximo.append(max(lista[i]))
        print("o max da matrix é ", max(maximo))
        input()
    return
lista= criar_lista()
opcao = " "
while opcao != "0":
    print(" \t\nMENU")
    print("1 -- inicaliçar lista.")
    print("2 -- lista transposta.")
    print("3 -- ver max da lista.")
    print("0 -- sair.")
    opcao= input("qual é a sua escolha: ")
    if opcao =="1":
        lista = criar_lista() #invoca a função 1
    elif opcao == "2":
        transposta(lista)  #invoca a função 2
    elif opcao == "3":
        for i in range(len(lista)):
            maximo(lista)  #invoca a função 3
    break
input()