# ver se ano é bissexto ou não
import random

resposta = "s" 

while resposta == "s" or resposta == "s":
    ano=random.randint(1900,2020)
    if ano%400 == 0 and (ano%4 == 0 and not ano%400 == 0):
        print("{0} é bissexto" .format(ano))
    else:
        print("{0} não é bissexto." .format(ano))
        
    resposta=input("s/n?")

input()

