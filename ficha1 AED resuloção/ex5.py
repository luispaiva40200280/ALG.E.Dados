# tempo em segundos convertidos

segundos=int(input("tempo em segundos:"))

horas=int(segundos/3600)
segundos-=horas*3600

minutos=int(segundos/60)
segundos-=minutos*60 
 
print(horas, "horas" , minutos, "minutos", segundos, "segundos")
 
input()