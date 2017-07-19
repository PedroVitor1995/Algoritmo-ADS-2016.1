"""26. Leia um numero inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde."""

dias = input ('Digite um valor inteiro de dias: ')

semanas = dias / 7
dias1 = dias % 7

print ('\nO equivalente em semanas e dias de %d dias e %d semanas e %d dias  ') % (dias,semanas,dias1)
