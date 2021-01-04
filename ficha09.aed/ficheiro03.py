#Crie uma aplicação que permita gerir um ficheiro de países
import os

def  inserir():
    os.system("cls")
    file = open( "paises.txt" , "r+")
    pais  = int(input(""))
    if pais == True:
        print("pais já existe no ficheiro")
    else :
        file.append(pais)

def consulta():
    file = open("paise.txt" , "r")
    ficheiro = file.readlines()
    file.close()
    lin = 1
    for linha in ficheiro:
        campos = linha.split(":")
        if campos[0] == continente :
            print("\t\t", campos[0], "\t" , campos[1], "\t" )
            lin+=1

def consultar(continente):
    print()




def consulta(numero_paises):
    print()


#pasta = "files"
#ficheiro = "files\\paises.txt"

#menu
op = 1
while op != 0:
    os.system("cls")
    os.system("cls")
    print("1 -- iserir paises. ")
    print("2 -- Consultar dados do ficheiro")
    print("3 -- Consultar países de um continente")
    print("4 -- Consultar nº de países por continente")
    print ("0 -- sair ")
    opecao =int(input("opeção:"))
    if op == 1 :
        inserir()
    elif op == 2:
        consulta()
    elif op == 3:
        consultar(continente)
    elif op == 4:
        consulta(numero_paises)
input()