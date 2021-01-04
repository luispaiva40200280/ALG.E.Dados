#mostra só o utimo e primero nome 

nome=input("nome:")
espaço=nome.find(" ")
if espaço != -1:
    primeiro= nome[:espaço]
    espaço = nome.rfind(" ")
    if espaço != -1:
        ultimo = nome[espaço+1:]
        print(primeiro, ultimo)

input()
#esta corretto


