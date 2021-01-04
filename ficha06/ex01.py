#inserir 10 numeros e ver quantos deles estão a cima da media
def acima_media(lista_numeros):
    media = sum(lista_numeros) / len(lista_numeros)
    print(media)
    cont = 0
    for i in range (10):
        if lista_numeros[i] > media:
            cont+=1
    return cont


lista_numeros = [] 
for i in range(10):
    numero=int(input("numero:"))
    lista_numeros.append(numero)
cont = acima_media(lista_numeros)
print("há {0} numº acima da media." .format(cont))

input()