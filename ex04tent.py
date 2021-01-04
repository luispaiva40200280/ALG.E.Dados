# ocupação de um pequeno parque de estacionamento
def estacinamento(lin,col):
    lista=[]
    for i in range(lin):
        lista.append([])
        for j in range(col):
            lista[i].append("livre")

    for linha in lista:
        print(linha)
    
    valor = False
    while not valor:
        try:
            fila=int(input("qual a fila em quer o carro?  "))
            if fila < 0 or fila > 3:
              raise ValueError()
        except ValueError:
            print("insira outro valor.")
        else:
            valor = True

    while not valor:
        try:
            posição=int(input("em que lugar quer por o carro? "))
        if posição < 0 or posição > 5:
             raise ValueError()
        except ValueError:
          print("insira outro valor")
        else:
         valor= True
        
    
    lista[fila][posição] =  "ocupado"

    return lista


parque = estacinamento(3,5)
opcao = " "
while opcao != 0:
    print("1 -- entrada do viculo")
    print("2 -- saida do vaiculo")
    print("3 -- eatado do parque")
    print("0 -- sair")
    if opcao == "1":
        estacinamento(lin,col)
    elif opcao == "2":
       entrada(parque)
    elif opcao == "3":
        estado(parque)
input()

