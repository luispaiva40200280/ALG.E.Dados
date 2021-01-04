#ler x numeros e calular a sua media e qua é o maior
soma=0
maior=0
media=0
x=int(input("quantas vezes queres?"))
for i in range(x):  
    numero=int(input("indica um numero:"))              #pede para inserir x numeros 
    soma+=numero
    if numero > maior:
        maior=numero

print("a media é: {0}" .format(soma/x))
print("o maior é", maior)


input()