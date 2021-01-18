#contador de presensas
from tkinter import *
from tkinter import messagebox
import datetime
from PIL import ImageTk, Image
import os 

window = Tk()
window.geometry("800x600")
window.title("presensas")

#criar uma barra de menus
barra_Menu = Menu(window)

def movimentos():
    x=0
barra_Menu.add_command(Label = "movimentos" , command = movimentos )

#criarr ficheiro 
def criar_ficheir(open):
    if os.path.exists("miniprojeto1.txt") == False :
        file = open("miniprojeto1.txt" , "a")
        file.write("PRESENSAS")
    else:
        file = open("miniprojet1" , "w+")
    file.close()


#imagen
canvas = Canvas(window, width=400, height=400,
highlightthickness=0, relief='ridge')
canvas.place(x=50, y=50)
img = ImageTk.PhotoImage(Image.open("presencas.jpg"))
canvas.create_image(200, 200, image=img)
    
lbl_tit = Label(window, text="Gestão de presencas" , fg= "black", font= ("helvicta",11))
lbl_tit.place(x=500,y=300)



#barra do menu 

window.mainloop()
