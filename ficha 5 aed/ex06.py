#numeração romana
def numeracao_romana(num):
    numeros =[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    romano =["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    i=13
    num_romano=""
    while num != 0:
        if numeros[i] <= num:
          num_romano += romano[12] 
          num -= numeros[i]
        else:
              i -= 1
    return num_romano

valido = False
while not valido:
    try:
        num=int(input("numero:"))
        if num < 0 and num > 999:
             raise ValueError()
    except ValueError:
        print("insira outro valor.")
    else:
        valido = True
romano = numeracao_romana(num)
print(romano)
 
input()
