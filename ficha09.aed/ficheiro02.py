#ler o fichero do ex 1 e ver media max min 
import os
import datetime # não necessario 
import time     # """"""""
def cabecalho(data):
    os.system("cls")
    print("\n\n\t\tdata de consulta:", data)
    print()
    print()
    print()
    print("\t\t   data  \t Hora   \t  temperatura ")
    print("\t--------------------------------------")
def consulta_data():
    os.system("cls")

    data=input("data que quer consultar: \t")
    cabecalho(data)
    file = open("temperatura.txt", "r") 
    ficheiro = file.readlines()
    file.close()
    lin = 1
    for linha in ficheiro:
        campos = linha.split(";")
        if campos[0] == data:
            print("\t\t", campos[0], "\t" , campos[1], "\t" , campos[2])
            lin+=1
    input()
    

def consultar_estatistica():
    file  = open("temperatura.txt", "r")
    f = file.readlines()
    temperatura = []
    for linha in f:
        campos = linha.split(";")
        temp =int(campos[2])
        temperatura.append(temp)
    file.close()
    maximo = max(temperatura)
    print("a temperatura max foi :", maximo)
    minima = min(temperatura)
    print("a temperatura min foi :", minima)     
    media = sum(temperatura) / len(temperatura)
    print("a media foi:", media)
    input()

opecao = 1
while opecao != 0:
    os.system("cls")
    print("1 -- consultar por data. ")
    print("2 -- consulta por estatistica.")
    print("0 --sair")
    opecao =int(input("opeção:"))
    if opecao == 1:
        consulta_data()
    else :
        consultar_estatistica()
input()