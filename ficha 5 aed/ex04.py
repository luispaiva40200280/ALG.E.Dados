#cripta de cesar
def encripta(texto, chave):#encripta o texto de acordo com a chave
    texto = ""
    for i in range (len(texto)):       #para percurrer 
        posicao_ascii = ord(texto[i]) #todos os carcteres do texto 
        posicao_ascii+=chave
        if posicao_ascii > 255 : #se com a soma da chave passar a tabela assci
            posicao_ascii = posicao_ascii-255
            caracter = chr(posicao_ascii)
            texto = texto + caracter
        return texto  #devolve o txto enciptado

texto = input("texto:")
valido = False
while not valido:
    try:
        chave = int(input("chave para o texto:"))
        if chave <0 and chave>20:
            raise ValueError()
    except ValueError:
        print("valor errdado insira outro valor.")
    else:
        valido = True

texto_encriptado = encripta(texto, chave)
print("Texto criptografado:", texto_encriptado)
input()