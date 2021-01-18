# Biblioteca Tkinter: UI
from tkinter import *


window=Tk()   # invoca classe tk , cria a "main window"
window.geometry("700x300")
window.title('Peso Ideal')



#Label
lbl_altura=Label(window, text="Altura em cm::", fg="blue", font=("Helvetica", 9))
lbl_altura.place(x=25, y=30)
#Entry
altura = IntVar()
txt_altura=Entry(window, width = 15, textvariable = altura)
txt_altura.place(x=120, y=30)
#Radiobutton
lframe = LabelFrame(window, width = 300, height=130, bd=3, text= "Género", fg = "blue", relief = "sunken")
lframe.place(x=25, y=100)

selected = StringVar()
selected.set("Masculino")   # Opção selecionada por defeito
rd1 = Radiobutton(lframe, text = "Masculino", value = "Masculino", variable = selected)
rd1.place(x=15, y=20)
rd2 = Radiobutton(lframe, text = "Feminino", value = "Feminino", variable = selected)
rd2.place(x=15, y=50)

def PesoIdeal():
    txt_PesoIdeal.config( fg = "red", width = 10, font = ("Helvetica", 11))
    k=4
    if selected.get() == "Masculino":
        k=4
    else:
        k=2
    # Obter valor da Entry altura: altura.get()
    peso = (altura.get() - 100) - (altura.get() - 150)/k
    peso_ideal.set(str(peso))
    


#Button
btn_PesoIdeal=Button(window,  text = "Calcular \nPeso Ideal" , width = 10, height = 7, relief = "raised", fg = "black", command = PesoIdeal)
btn_PesoIdeal.place(x=350, y=110)


# Panel
panel1 = PanedWindow(window, width = 230, height = 120, bd = "3", relief = "sunken")
panel1.place(x=450, y=110)

lbl_PesoIdeal=Label(panel1, text="Peso Ideal em Kg",  fg="blue", font=("Helvetica", 9))
lbl_PesoIdeal.place(x=42, y=25)
#Entry
peso_ideal=StringVar()
txt_PesoIdeal=Entry(panel1, width = 15, state = "disabled" , textvariable = peso_ideal)
txt_PesoIdeal.place(x=59, y=60)

window.mainloop()