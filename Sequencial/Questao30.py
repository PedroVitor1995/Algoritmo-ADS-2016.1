"""30. Leia um numero inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele
corresponde."""

minutos = input ('Digite numero inteiro de minutos: ')

dias = (minutos / 60) / 24
horas = (minutos / 60) % 24
minutos1 = (minutos % 60) 

print ('\nA quantidade de dias,horas e minutos corresonde a %d minutos e %d dias %d horas %d minutos') % (minutos,dias,horas,minutos1)