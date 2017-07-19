"""27. Leia um numero inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos
segundos ele corresponde."""

segundos = input ('Digite numero inteiro de segundos: ')

horas = (segundos / 60 ) / 60
minutos = (segundos / 60) % 60
segundos1 = segundos % 60

print ('\nA quantidade de horas, quantos minutos e quantos segundos corresonde a %d segundos e %d horas %d minutos %d segundos ') % (segundos,horas,minutos,segundos1)