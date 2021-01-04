# ocupação de um pequeno parque de estacionamento
def lista(fila,lugar):
    lista = []
    for i in range(fila):
        lista.append(lugar)
        for j in range(lugar):
            lista.append("ocupado")
    




parque = lista(3,5)
opcao = " "
while opcao != 0:
    print("1 -- entrada do viculo")
    print("2 -- saida do vaiculo")
    print("3 -- eatado do parque")
    print("0 -- sair")
    if opcao == "1":
        lista(fila,lugar)
    elif opcao == "2":
        entrada(parque)
    elif opcao == "3":
        estado(parque)

input()
