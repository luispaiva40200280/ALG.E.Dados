#ler um texto e ver se é capicua ou não
texto=input("escreve aqui:")
comp=len(texto)
contrario=""
for i in range(comp-1,-1,-1):
    contrario+= texto[i]

if texto == contrario:
    print("é capicua")
else:
      print("não é capicua .")

input()
#esta correto