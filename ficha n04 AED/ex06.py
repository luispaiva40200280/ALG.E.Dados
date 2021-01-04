# normalização do nome 
nome=input("nome:")
normalizado=""
espaço=nome.find(" ")
if espaço != -1:
    normalizado = nome[:espaço]    

else:
    print("formato invalido ")
    exit

for i in range(espaço,nome.rfind(" ")):
    if nome[i] == " ":
        normalizado+= " " + nome[i+1:] + "."

espaço = nome.rfind(" ") 
if espaço != -1:
    normalizado = normalizado + " " + nome[espaço+1:]

print(normalizado)

input()

