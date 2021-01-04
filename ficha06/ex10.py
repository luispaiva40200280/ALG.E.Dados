#vistantes diarios em uma semana
semana=["sabado","domingo","segunda","terça","quarta","quinta","sexta"]
def media(lista_convidados):
    media = sum(lista_convidados) / len(semana)
    return media
def ordenar_decr(convidados):
    

lista_convidados=[]
for i in range(7):
   comv_diarios = int(input("convidados de {0}:    " .format(semana[i])))
   lista_convidados.append(comv_diarios)

valormedia = media(lista_convidados)
print(valormedia)