#lista com pontuação positavas e com os nomes dos participantes
def lista_postitivas(lista_nomes,lista_notas):
    nomes_positavas=[]
    notas_positavas=[]   
    for i in range(len(lista_notas)):
        if lista_notas[i] >= 10:
            notas_positivas.append(lista_notas[i])
            nomes_positavas.append(lista_nomes[i])
    return nomes_positavas , notas_positavas 

lista_nomes=[]
lista_notas=[]
for i in range (10):
    nomes=input("nome do aluno: " )
    valor = False
    while not valor:
        try:
            nota=int(input("nota do aluno: " ))
            if nota > 20 and nota < 0 :
                raise ValueError()
            lista_notas.append(nota)
            lista_nomes.append(nomes)
        except ValueError:
                print("insira outro valor: ")
        else :
            valor = True

nomes, positivas = lista_postitivas(lista_nomes,lista_notas)               
print("os alunos com nota possitiva: {0}")
print("nome do aluno : {0}" .format(nomes_positivas))
print("notas dos alunos: {0}" .format(notas_postitivas))

