#ler 10 numeros e calcular a media e o maior numero 

soma=0
maior=0
for i in range(10):  
    numero=int(input("indica um numero:"))              #pede para inserir 10 numeros 
    soma+=numero
    if numero > maior:
        maior=numero

print("a media é: {0}".format(soma/10))
print("o maior é", maior)


input()