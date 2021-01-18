# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import ttk  # treeview
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime


ficheiro = "presencas.txt"


#------------------------------------------------------
class App:                                  # Definição da classe App
    def __init__(self, window, img):         # Construtor da classe App
        self.window = window
        # Implementar menu
        barra_Menu = Menu(self.window)
        # Constroi menu Simuladores, com 2 opções dropd-down
        barra_Menu.add_command(label="Movimentos", command=self.movimentos)
        barra_Menu.add_command(label="Consulta", command=self.consulta)
        # Constroi menu Sair, com comando quit
        barra_Menu.add_command(label="Sair", command=window.quit)
        window.configure(menu=barra_Menu)

        lbl = Label(window, text="Gestão de Presenças", font=("Helvetica", 12))
        lbl.place(x=450, y=120)

        # ------- Imagem
        # container Canvas, usado para aplicações de desenho: imagens e formas geométricas
        ctn_canvas = Canvas(window, width=350, height=200,
                            bd=4, relief="sunken")
        ctn_canvas.place(x=70, y=40)
        ctn_canvas.create_image(175, 100, image=img)

    def consulta(self):

        ConWindow = Toplevel()
        ConWindow.geometry("700x300")
        ConWindow.title("Consultas")
        ConWindow.focus_force()  # força o focus na window atual
        ConWindow.grab_set()    # direciona todos os eventos para a window ativa

        # Panel
        panel1 = PanedWindow(ConWindow, width=200,
                             height=270, bd="3", relief="sunken")
        panel1.place(x=15, y=20)

        #Frame Tipo de Movimento
        lframe = LabelFrame(panel1, width=160, height=100, bd=3,
                            text="Tipo de Movimento", fg="blue", relief="sunken")
        lframe.place(x=5, y=5)
        self.cb1 = IntVar()
        self.cb2 = IntVar()
        ck1 = Checkbutton(lframe, text="Entrada", variable=self.cb1)
        ck1.place(x=15, y=15)
        ck2 = Checkbutton(lframe, text="Saída", variable=self.cb2)
        ck2.place(x=15, y=40)

        #Frame Utilizador
        lframe2 = LabelFrame(panel1, width=160, height=100, bd=3,
                             text="Por Utilizador", fg="blue", relief="sunken")
        lframe2.place(x=5, y=120)
        lbl_utilizador = Label(lframe2, text="Número: ")
        lbl_utilizador.place(x=15, y=5)

        self.utilizador = StringVar()
        txt_utilizador = Entry(lframe2, width=15, textvariable=self.utilizador)
        txt_utilizador.place(x=15, y=25)

        btn_consultar = Button(panel1, width=21, height=2, text="Consultar",
                               relief="raised", command=self.dados_treeview)
        btn_consultar.place(x=8, y=222)

        # Painel 2
        panel2 = PanedWindow(ConWindow, width=450,
                             height=270, bd="3", relief="sunken")
        panel2.place(x=220, y=20)

        self.tree = ttk.Treeview(panel2, columns=(
            "Número", "Data", "Hora", "Movimento"), show="headings")
        self.tree.column("Número", width=100,   anchor="c")
        # c- center, e - direita, w- esquerda
        self.tree.column("Data", width=100,  anchor="c")
        self.tree.column("Hora", width=100,   anchor="c")
        self.tree.column("Movimento", width=140,   anchor="c")
        self.tree.heading("Número", text="Número")
        self.tree.heading("Data", text="Data")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Movimento", text="Movimento")
        self.tree.place(x=5, y=5)

    def dados_treeview(self):  # Remove TODAS as linhas da Treeview
        self.tree.delete(*self.tree.get_children())
        mov = ""
        if self.cb1.get() == True and self.cb2.get() == True:   # Se está checado entrada e saída (cb1 e cb2)
            mov = "T"
        else:
            if self.cb1.get() == True:                      # se está apenas checado cb1 (entrada)
                mov = "Entrada\n"
            if self.cb2.get() == True:                      # se está apenas checado cb2 (saida)
                mov = "Saída\n"

        f = open(ficheiro, "r", encoding="utf-8")
        lista = f.readlines()
        f.close()
        for linha in lista:
            campos = linha.split(";")
            if mov == "T" or campos[3] == mov:
                if self.utilizador.get() == "" or self.utilizador.get() == campos[0]:
                    self.tree.insert("", "end", values=(
                        campos[0], campos[1], campos[2], campos[3]))

    def registar_mov(self):
       f = open("presencas.txt", "a")
       data = str(datetime.date.today())
       hora = str(datetime.datetime.now().time())
       mov = self.selected.get()
       num = str(self.numero.get())
       linha = num + ";" + data + ";" + hora + ";" + mov
       f.write(linha)
       f.close()
       self.lbox_mov.insert("end", linha)

    def movimentos(self):
        top = Toplevel()   # Objeto da classe Toplevel, janela principal
        top.geometry("700x300")
        top.title("Entradas e Saídas")
        top.focus_force()     # Força toda a interação com a janela atual (top window)
        top.grab_set()        # Força que todos os eventos (p.e. clicar num button)  estejam enquadrados no componente atual (janela top)

        lbl_numero = Label(top, text="Número de Estudante:")
        lbl_numero.place(x=20, y=15)

        self.numero = IntVar()
        self.txt_numero = Entry(top, width=20, textvariable=self.numero)
        self.txt_numero.place(x=150, y=15)

        #Radiobutton
        lframe = LabelFrame(top, width=200, height=130, bd=3,
                            text="Género", fg="blue", relief="sunken")
        lframe.place(x=25, y=60)

        self.selected = StringVar()
        self.selected.set("Entrada")   # Opção selecionada por defeito
        self.rd1 = Radiobutton(lframe, text="Entrada",
                               value="Entrada", variable=self.selected)
        self.rd1.place(x=15, y=20)
        self.rd2 = Radiobutton(lframe, text="Saída",
                               value="Saída", variable=self.selected)
        self.rd2.place(x=15, y=50)

        #Button
        self.btn_registar = Button(
            top, width=12, height=4, text="Registar", command=self.registar_mov)
        self.btn_registar.place(x=250, y=80)

        self.lbl_numero = Label(top, text="Histórico de movimentos")
        self.lbl_numero.place(x=500, y=15)
        # Panel
        self.panel1 = PanedWindow(
            top, width=280, height=200, bd="3", relief="sunken")
        self.panel1.place(x=400, y=50)
        #ListBox
        self.lbox_mov = Listbox(self.panel1, width=38,
                                height=10, bd="3", selectmode="single")
        self.lbox_mov.place(x=6, y=22)


window = Tk()   # invoca classe tk , cria a "main window"
window.geometry("700x300")
window.title('Gestão de Presenças')
img = ImageTk.PhotoImage(Image.open("presencas.jpg"))
#s_w = window.winfo_screenmmwidth()
#s_h = window.winfo_screenmmheight()


# Invoca classe App, passando como argumentos a window atual e a imagem
App(window, img)


window.mainloop()   # event listening loop by calling the mainloop()
