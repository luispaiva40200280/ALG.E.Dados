#fatoração dentro de uma impresa

meses =["janeiro" , "fevereiro" , "março " ,"abril", "maio" ,"junho", "julho", "agosto", "setembro ","outobro ","novenbro" , "decembro"]
def media(lista_faturacao):
    media = sum(lista_faturacao) / len(meses)
    return media

def maior(lista_faturacao):
    maior= max(lista_faturacao[i])
    return maior
def minimo(lista_faturacao):
    minimo= min(lista_faturacao)
    return minimo

lista_faturacao=[]
for i in range(12):
    faturção_mensal = int(input("faturção de {0}:    " .format(meses[i])))
    lista_faturacao.append(faturção_mensal)


valormedia = media(lista_faturacao)

print("media mensal foi {0}:" .format(valormedia))
print("{0} teve a menor faturação com {1}" .format(meses,maior))
print("{0} teve a maior faturação com {1}" .format(meses,minimo))

input()