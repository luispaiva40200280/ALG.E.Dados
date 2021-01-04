#gerador de passwords
import random 

username = input("nome:")
password = ""

for i in range(len(username)):
    if i % 2 != 0:
        password+= username[i]
        password+= str(random.randint(1,9))

password+= str(len(username))
print("password é:" , password)


input()
#correto, precissa de se rever uma outra vez


