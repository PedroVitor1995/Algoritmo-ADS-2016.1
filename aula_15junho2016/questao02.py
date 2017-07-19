"""2. Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.
"""

horas = input("horas: ")
minutos = input("minutos: ")
horaz = horas*60
minutos_t = horaz+minutos
print "%d horas e %d minutos equivalem a %d minutos"%(horas,minutos,minutos_t)