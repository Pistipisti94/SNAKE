lista = []
file = open("Python 13.11\\fajl", "r")
for line in file:
   lista.append(line[0:len(line) - 1])
file.close()

index = len(lista) - 1
forditott_lista = []
for l in lista:
   forditott_lista.append(lista[index])
   index = index - 1

file = open("Python 13.11\\ujfajl", "w")
for x in forditott_lista:
   file.writelines(f"{x}\n")
file.close()