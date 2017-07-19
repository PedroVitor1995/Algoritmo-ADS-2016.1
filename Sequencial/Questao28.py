"""28. Leia um numero inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele
corresponde."""

horas = input ('Digite numero inteiro de horas: ')

semanas = (horas / 24 ) / 7
dias = (horas / 24 ) % 7
horas1 = horas % 24

print ('\nA quantidade de semanas,dias e horas corresonde a %d horas e %d semanas %d dias %d horas') % (horas,semanas,dias,horas1)