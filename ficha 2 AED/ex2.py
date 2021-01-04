#cassificar triangulos

lado1=int(input("valor de 1 lado:"))
lado2=int(input("valor do 2 lado:"))
lado3=int(input("valor do 3 lado:"))

if lado1 == lado2 == lado3:
    print("o triangulo é equilatro")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
     print("o triangulo é isósceles")
else:
    print("o triangulo é escaleno")
  