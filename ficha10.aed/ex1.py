#pograma que guarda um texto em de um fichero em formato txt
#interface de tkinter
from tkinter import *
import os



ficheiro = "texto_ficha10_ex1"

#abre o fichero ; cria se não existir e 
def guardar_ficheiro():
    linha = txt_texto.get("1.0", "end-1c") #janela de texto

    f = open(ficheiro, "w", encoding="utf-8")
    f.write(linha)
    f.close()

#limpar contiado da caixa de texto
def limpar():
    txt_texto.delete("1.0", "end")
    txt_texto.insert("end", "")


def ler_ficheiro():
    f = open(ficheiro, "r", encoding="utf-8") 
    linhas = f.readlines()   # ler todo o ficheiro para uma lista
    f.close()
    txt_texto.delete("1.0", "end")
    for lin in linhas:
        txt_texto.insert("end", lin)

    



#começo do progrma
window = Tk()
window.geometry("500x300") 
window.title("formolario da ficha 10 ex1")

#botoes:

btn_guardar= Button (window , text= "guardar" , width = 10 , height = 3 , command = guardar_ficheiro)
btn_guardar.place(x=20 , y= 50)

btn_limpar= Button (window, text="limpar", width=10, height=3, command =limpar)
btn_limpar.place(x=20 , y=150)

btn_ler = Button (window,  text="Ler ficheiro", width=10, height=3 , command =ler_ficheiro)
btn_ler.place(x=20, y=250)

#caixa de texto
texto=StringVar()  # variavel que vou associar ao componente Text
txt_texto = Text(window, width=55, height=14, relief="sunken", bd=3)
txt_texto.place(x=200, y=50)

#termina a janela o mesmo que input()
window.mainloop()   # event listening loop by calling the mainloop()
