#execicio feito pelo prof.
import random                   # módulo que inclui o método randint (números aleatorios)
from datetime import datetime   # módulo que inclui métodos para obter data e hora
import time   
import os                  # módulo que inclui o método sleep


# Função que recebe a linha gerada e guarda no ficheiro
def save_file(linha):
    f = open("temperatura.txt", "a")   # abre o ficheiro em modo de Append
    f.write(linha)
    f.close()

# Função que lê o conteúdo do ficheiro de texto e imprime
def read_file():
    os.system("cls")
    print("\t\t    Data     \t Hora   \tTemperatura")
    print("\t\t------------------------------------------")

    f = open("temperatura.txt", "r")   # abre o ficheiro em modo de Leitura
    for linha in f:
        campos = linha.split(";")       # separa o conteúdo de cada linha do ficheiro pelo caracter ";"
        print("\t\t", campos[0], "\t", campos[1], "\t", campos[2])
    f.close()



# Funciona num do for ever, o ciclo while +e semper veraddeiro. Termina com o fecho da aplicação
# Simula a leitura de um sensor de temperatura, gerando valor aleatório com intervalos de 1 segundo
print("\t\t    Data     \t Hora   \tTemperatura")
print("\t\t------------------------------------------")
fim = False
while not fim:
    temp = random.randint(10,25)                        # valor aleatorio da temperatura
  
    data = datetime.now().date()                        # obtem data de sistema
    hora = datetime.now().time().strftime("%H:%M:%S")   # Obtem hora de sistema H:M:S
    print("\t\t", data, "\t", hora, "\t", temp)         # Imprime
    linha = str(data) + ";" + str(hora) + ";" + str(temp) + "\n"   # Controi string linha para guardar dados no ficheiro 
    save_file(linha)
    time.sleep(1)                                                  # faz pausa de 1 segundo
  
input()