#jogo adevina o numero
import random
tentativa=0
palpite=0
numero=random.randint(1,50)
while tentativa != numero or palpite < 10:
    tentativa = int(input("tentativa:"))         
    palpite+=1   
    print("não acertou no numero")      
    if numero > tentativa:
        print("o seu palpite é menor que o numero.")
    elif numero < tentativa:
        print("o seu palpite é maior que o numero.")
    else:
        print("parabens acertaste no numero na tentativa {0}" .format(palpite))

input()            