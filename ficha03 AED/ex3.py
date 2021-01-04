# calcular o fatorial de um numero

numero=int(input("escreve um numero:"))
faturial=1
for i in range (numero ,1 , -1):
    faturial*=i
    
print("o fatorial de {0} é {1}" .format(numero,faturial))

input()



