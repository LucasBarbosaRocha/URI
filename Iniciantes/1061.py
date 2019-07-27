# Entrada de dados
scan = raw_input().split(" ")
scan2 = raw_input().split(" ")
scan3 = raw_input().split(" ")
scan4 = raw_input().split(" ")

# Separando a entrada 
diaI = int(scan[1])
horaI = int(scan2[0])
minI = int(scan2[2])
segI = int(scan2[4])
diaF = int(scan3[1])
horaF = int(scan4[0])
minF = int(scan4[2])
segF = int(scan4[4])

# 24*3600 = 86400 um dia todo
# 60*60 = 3600 = uma hora toda
# 60 = um minuto

durI = ((diaI*86400) + (horaI*3600) + (minI*60) + segI)
durF = ((diaF*86400) + (horaF*3600) + (minF*60) + segF)
dur = durF-durI

print "%d dia(s)" %((dur/86400))
print "%d hora(s)" %(((dur%86400)/3600))
print "%d minuto(s)" %((((dur%86400)%3600)/60))
print "%d segundo(s)" %(((((dur%86400)%3600)%60)))