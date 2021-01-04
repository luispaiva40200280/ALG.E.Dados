#ler 10 pontuções e ver quas são positivas
def lista_positivas(lista_pontuacao):
    positivas = []
    for i in range (10):
        if lista_pontuacao[i] >= 10:
            positivas.append(lista_pontuacao[i])
    return positivas

lista_pontuacao = []
for i in range(10) :
    valor = False
    while not valor:
        try:
            pontuação = int(input("pontuação : "))
            if pontuação < 0 and pontuação > 20:
              raise ValueError()
            lista_pontuacao.append(pontuação)
        except ValueError:
            print("insere outro valor:")
        else:
            valor = True
            
positivas = lista_postiva(lista_pontuacao)

print("pontuação positiva {0}" .format(positivas))


