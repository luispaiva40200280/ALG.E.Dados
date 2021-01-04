#verificar se o numero é primo ou não
import random
vezes=0
numero=random.randint(1,1000)
for i in range(1,numero,1):
    if numero%i == 0:
        print("{0} é primo" .format(numero))
    else:
        print("{0} não é primo." .format(numero))
        

input()