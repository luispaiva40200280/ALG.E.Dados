# indice de massa corpural

peso=int(input("peso do em kg:"))
altura=float(input("altura em metros:"))

imc = peso/(altura**2)

print("indice de massa corpural é:",imc)

print("imc = {:.2f}".format(imc))

input()
