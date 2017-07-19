"""29. Um numero e um quadrado perfeito quando a raiz quadrada do numero e igual a soma das dezenas
formadas pelos seus dois primeiros e dois ultimos digitos.
Exemplo: raiz 9801 = 99 = 98 + 01. O numero 9801 e um quadrado perfeito.
Escreva um algoritmo que leia um numero de 4 digitos e verifique se ele e um quadrado perfeito."""

from math import sqrt as raiz
numero = input ('Digite um numero de 4 digitos: ')

milhar = str(numero / 1000)
centena = str((numero % 1000) / 100)
dezena = str((numero % 1000) % 100 / 10)
unidade = str(numero % 10)

numero1 = str(milhar + centena)
numero2 = str(dezena + unidade)

numero1 = int (numero1)
numero2 = int (numero2)

terceiro_numero = numero1 + numero2

if raiz(numero) == terceiro_numero :
	print ('\nO numero e um quadrado perfeito')
else :
	print ('\nO numero nao e  um quadrado perfeito')




