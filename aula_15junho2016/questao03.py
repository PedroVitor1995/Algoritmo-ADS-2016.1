"""3. Leia um valor em minutos, calcule e escreva
o equivalente em horas e minutos."""

print 'Teste'
minutos = input("Minutos: ")
hora = minutos/60
mins = minutos % 60
print "%d horas e %d minutos." % (hora, mins)