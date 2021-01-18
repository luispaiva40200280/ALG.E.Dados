#peso ideal com interface grafica 
#biblioteca tkinter
from tkinter import *
import os 

def peso_ideal():
    k = 4
    peso = (altura.get() - 100) - (altura.get() - 150)/k
    peso_ideal.set(str(peso))
    
    if selected.get() == "femenino":
        k == 2
        
    else:
        k == 4
       
window = Tk()
window.geometry("700x300")
window.title("peso ideal")

#labels
lbl_alura = Label(window, text="Altura em cm::", fg="blue", font=("Helvetica", 9))
lbl_alura.place(x=25, y=10)

#entry
altura = IntVar()
txt_altura = Entry(window, width=15, textvariable=altura)
txt_altura.place(x=100, y=10)

#lable  frame
lframe = LabelFrame(window, width=300, height=130, bd=3,
text="Género", fg="blue", relief="sunken")
lframe.place(x=25, y=100)

#radiobutton
selected=StringVar()             
selected.set("Masculino")

masculino = Radiobutton(lframe, variable= selected, value="masculino" , text ="masculino")
masculino.place(x=15,y=20)
femenino =Radiobutton(lframe,  variable= selected , value="femenino", text = "femenino")
femenino.place(x=15,y=50)

#button
peso_ideal = Button(window, text="calcular  \n peso ideal", 
width=10 , height=6, command= peso_ideal )
peso_ideal.place(x=350,y=150)

# Panel
panel1 = PanedWindow(window, width=230, height=120, bd="3", relief="sunken")
panel1.place(x=450, y=110)
#lable
lbl_PesoIdeal = Label(panel1, text="Peso Ideal em Kg", 
fg="blue", font=("Helvetica", 9))
lbl_PesoIdeal.place(x=42, y=25)

#entry
peso_ideal = StringVar()
txt_PesoIdeal = Entry(panel1, width=15, state="disabled", 
textvariable=peso_ideal)
txt_PesoIdeal.place(x=59, y=60)

window.mainloop()