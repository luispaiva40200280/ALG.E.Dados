#gerar uma chave aleatoria de euromelhoes
import random

def gera_valor(lim_inf,lim_sup, qt):
    chave = []
    cont = 0
    chave_completa = False
    while not chave_completa:
        numero = random.randint(lim_inf,lim_sup) #gera um num aleatorio
        if numero not in chave:                #para as duas listas
            chave.append(numero)   #acrescenta os num gerados as listas              
            cont+=1 #cont = cont+1  #conta os num postas nas listas
        if cont == qt: # quando a lista estiver cheia
            chave_completa = True
    return chave



op = ""
while op.upper() != "N":
    chave = []
    estrelas = []

    chave = gera_valor(1,50,5)
    estrelas = gera_valor(1,12,2)
    print("chhave:", chave , "estreras:", estrelas )
    op = input("deseja outra chave S/N?  ")
 
input()










