#indice de massa corpural
#interface GUI
from tkinter import *
import os
from PIL import ImageTk, Image

window = Tk()
window.geometry("700x500")
window.title("IMC")

#panel for massa and altura
panel = PanedWindow(window, width=300, height=200, bd="3",relief="sunken")
panel.place(x=10, y=10)
#panel for IMC
panel_imc = PanedWindow(window, width=300, height=200, bd="3", relief="sunken")
panel_imc.place(x=10,y=300)

#lables for massa ; altura ; imc
lbl_massa = Label(panel, text = "massa" ,fg= "black" , font = ("serif" , 8))
lbl_massa.place(x=50, y=50)

lbl_altura = Label(panel, text="altura", fg="black", font=("serif", 8))
lbl_altura.place(x=50, y=100)

lbl_imc = Label(panel_imc, text="Indice de massa corporal", fg="red", font=("serif", 9))
lbl_imc.place(x=90, y=40)

#entry
altura = IntVar()
txt_altura = Entry(panel, width=15, textvariable=altura)
txt_altura.place(x=100, y=100)

massa = IntVar()
txt_massa = Entry(panel, width=15, textvariable=massa)
txt_massa.place(x=100, y=50)

val_imc = StringVar()
txt_imc = Entry(panel_imc, width=15, state="disabled", textvariable= val_imc)
txt_imc.place(x=59, y=100)

def indice_MC():
    '''imc = massa.get() / (altura.get() * altura.get())
    imc.set(str(imc))'''
    altura_M = altura.get() / 100        # obter altura da Entry e converter e metros
    imc = massa.get() / (altura_M * altura_M)
    str_imc = "{0:.2f}".format(imc)    # Formata com 2 casas decimais
    val_imc.set(str_imc)


def sair():
  window.destroy()     # fecha o container window


#bottun 
btn_IMC = Button(window, width=12, height=7 , text = "IMC" ,
command = indice_MC)
btn_IMC.place(x=350,y=100)

btn_sair = Button(window, width=12, height=7, text="sair",
command = sair)
btn_sair.place(x=350,y=230)

# ------- Imagem
# container Canvas, usado para aplicações de desenho: imagens e formas geométricas
ctn_canvas = Canvas(window, width=270, height=180, bd=2, relief="sunken")
ctn_canvas.place(x=470, y=40)

img = Image.open("IMC.JPG")
img = ImageTk.PhotoImage(img)
ctn_canvas.create_image(135, 90, image=img)

window.mainloop()
