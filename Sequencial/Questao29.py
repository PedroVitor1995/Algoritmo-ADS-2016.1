"""29. Leia um numero inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde."""

meses = input ('Digite um valor inteiro em de mese: ')

anos = meses / 12
meses1 = meses % 12

print ('\nO equivalente em anos e meses de %d meses e %d anos e %d meses ') % (meses,anos,meses1)