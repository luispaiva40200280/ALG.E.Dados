#fatorial com funções

def faturial(numero):
    faturial=1
    for i in range (numero ,1 , -1):
        faturial*=i
        print("o fatorial de {0}! é {1}" .format(numero,faturial))

try:
    numero=int(input("numero:"))
except ValueError:
    print("o valor é incorreto")
faturial(numero)
print("o fatorial de {0}! é {1}" .format(numero,faturial))


input()


 