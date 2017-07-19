"""25. Leia um numero inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde."""

valor = input ('Digite um valor inteiro em metros: ')

km = valor / 1000
m = valor % 1000

print ('\nO equivalente em km e metros de %d metros e %d km e %d metros  ') % (valor,km,m)
