#to do list 
from tkinter import *
import os

window = Tk()
window.geometry("700x600")
window.title("IMC")

#nome ficheiro
ficheiro = "tarefas.txt"

#panel
panel = PanedWindow(window, width=300, height=350, bd="3", relief="sunken")
panel.place(x=10, y=10)

panel1 = PanedWindow(window, width=300, height=80, bd="3", relief="sunken")
panel1.place(x=350, y=10)

# Adiciona tarefa à Listbox
def adicinar_tarefa():
    lbox_tarefas.insert("end", txt_tarefas.get())  #inserir á list box tarefas 
    tarefas.set("")
    num_tarefas()   ##

#remover tarefa da listvox
def remover_tarefa():
    #Remove o item selecionado da Listbox
    lbox_tarefas.delete(lbox_tarefas.curselection())   # indice do item selecionado
    tarefas.set("")
    num_tarefas()

#seleciona o item para remover da listbox com crusor
def selecao_item(event):
    indice = lbox_tarefas.curselection()   # Índice da linha selecionada
    # Obter conteudo da Listbox, linha selecionada
    texto = lbox_tarefas.get(indice)

def delete_todas():
    lbox_tarefas.delete("0", "end")
    lbox_tarefas.insert("end", "")

#ler o ficheiro 
def upplaod_ficheiro():

    delete_todas()
    f = open(ficheiro , "r", encoding="utf-8")
    lista = f.readlines()  #ler todas as lihas do f
    f.close()
    for linha in lista:
          lbox_tarefas.insert("end", linha)  #insere as linhas lidas á listbox
    num_tarefas()


def downlaod_tarefas():
    f = open(ficheiro , "w", encoding="utf-8")
    cont = lbox_tarefas.size()
    for i in range(cont):
        atividade = lbox_tarefas.get(i) 
        if atividade.find("\n") == -1:
               atividade = atividade + "\n"

        f.write(atividade)
    f.close()  

def ordenar_tarefas():
    cont = lbox_tarefas.size()     # Nº tarefas na ListBox
    lista=[]                       # Lita vazia
    for i in range(cont):          # carrega lista a partir da Listbox
        lista.append(lbox_tarefas.get(i)) 
    lista.sort()                    # Ordena
    lbox_tarefas.delete(0, "end")   # apaga conteudo da Listbox
    for linha in lista:             # coloca lista ordenada na Listbox
        lbox_tarefas.insert("end", linha)

def num_tarefas():
    cont = lbox_tarefas.size()   #contador de linhas no ficheiro
    # contador de tarefas numero que aparece.set(str(cont))   
    numero_tarefas.set(str(cont))  # contador de tarefas numero que aparece
    
#label
lbl_tarefas = Label(panel1, text="TAREFAS", fg="black", font=("serif", 8))
lbl_tarefas.place(x=20,y=20)

#entry
tarefas = IntVar()
txt_tarefas = Entry(panel1, width=30, textvariable=tarefas)
txt_tarefas.place(x=80, y=20)

#Listbox
lbox_tarefas = Listbox(panel, width=35, height=15, bd="3", selectmode="single")
lbox_tarefas.place(x=8, y=25)
# Evento ao selecionar item da Listbox
lbox_tarefas.bind("<<ListboxSelect>>", selecao_item)

#bottuns
btn_adicionar = Button(window, width=7, height=5 , text = "adicionar" ,command=adicinar_tarefa)
btn_adicionar.place(x=350, y=200)

btn_remover = Button(window, width=7, height=5, text="remover", command=remover_tarefa)
btn_remover.place(x=420, y=200)

btn_delete = Button(window, width=7, height=5, text="delete", command=delete_todas)
btn_delete.place(x=480, y=200)

btn_upplaod = Button(window, width=7, height=5,text="upplaod", command=upplaod_ficheiro)
btn_upplaod.place(x=350, y=300)

btn_downlaod = Button(window, width=7, height=5, text="downlaod", command=downlaod_tarefas)
btn_downlaod.place(x=420, y=300)

btn_ordenar = Button(window, width=7, height=5,text="ordenar", command=ordenar_tarefas)
btn_ordenar.place(x=480, y=300)

#Label nº tarefas 
lbl_count_tarefas=Label(window, text="Nº de Tarefas Pendentes:", fg="blue", font=("Helvetica", 9))
lbl_count_tarefas.place(x=300, y=400)

#emtry nº tarefas 
numero_tarefas =StringVar()  #variavek associada à Entry contadora de tarefas
txt_numero = Entry(window, width = 5, textvariable= numero_tarefas)
txt_numero.place(x=500, y=400)

window.mainloop()
