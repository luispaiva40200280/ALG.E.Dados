#advinha o numero 2.0
import random
numero=random.randint(1,50)
resposta = "s" 
tentativa=0
palpite=0
while resposta == "s" or resposta == "s":
    while tentativa != numero or palpite < 10:
        tentativa = int(input("tentativa:"))         
        palpite+=1  
        if numero > tentativa:
            print("o seu palpite é menor que o numero.")
        elif numero < tentativa: 
            print("o seu palpite é maior que o numero.")
        else:
            print("parabens acertaste no numero na tentativa {0}" .format(palpite))
    
resposta=input("s/n?")

input()
