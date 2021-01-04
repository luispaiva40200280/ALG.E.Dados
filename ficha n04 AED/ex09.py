#substituir n decimas pelo seu respetivo nome
#para trabalhar o uso de funçao replace 
texto=input("texto")

texto = texto.replace("0", "zero")
texto = texto.replace("1", "um")           #só rersulta para
texto = texto.replace("2", "dois")        #nº < que 10
texto = texto.replace("3", "três")    
texto = texto.replace("4", "quatro")
texto = texto.replace("5", "cinco")
texto = texto.replace("6", "seis")
texto = texto.replace("7", "sete")
texto = texto.replace("8", "oito")
texto = texto.replace("9", "nove")
print(texto)
input()