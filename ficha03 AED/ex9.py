# numero perfeito 

numero=int(input("numero?"))
soma=0
for i in range(numero-1,0,-1):
    resto= numero%i
    if resto == 0:
        soma = i
if soma == numero:
    print("o n é {0} é perfeito" .format(numero))
else:
    print("o n {0}  não é perfeito" .format(numero))

input()