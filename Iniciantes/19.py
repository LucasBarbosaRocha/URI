segundos = int(raw_input())

horas = (segundos/60)/60 # segundos para horas

minutos = (segundos - (horas*60*60))/60 # minutos 

segundosRestante = (segundos - (horas*60*60)) - (minutos*60) # segundos

print "%d:%d:%d" %(horas,minutos,segundosRestante)