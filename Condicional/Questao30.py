"""30. Existem numeros de 4 digitos (entre 1000 e 9999) que obedecem a seguinte caracteristica: se dividirmos
o numero em dois numeros de dois digitos, um composto pela dezena e pela unidade, e outro pelo
milhar e pela centena, se somarmos estes dois novos numeros gerando um terceiro, o quadrado deste
terceiro numero e exatamente o numero original de quatro digitos. Por exemplo:
2025 -> dividindo: 20 e 25 -> somando temos 45 -> 45 ** 2 = 2025."""

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
numero_original = terceiro_numero ** 2

if raiz(numero) == terceiro_numero :
	print ('\nDividindo o numero em dois numeros de dois digitos, um composto pela dezena e pela unidade, e outro pelo milhar e pela centena ')
	print ('\nNumero formado pelo milhar e pela centena e %d ') % (numero1)
	print ('\nNumero formado pela dezena e pela unidade %d') % (numero2)
	print ('\nO terceiro numero formado pela soma da divisao do numero em dois outro numeros de dois digitos e %d') % (terceiro_numero)
	print ('\nO terceiro numero %d vai ser o quadrado do numero original que e %d ') % (terceiro_numero,numero_original)
else :
	print ('O numero dividido em  dois numeros de dois digitos que a soma formam o terceiro numero nao e o quadrado do numero original')




