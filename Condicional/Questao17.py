"""17. Leia valores inteiros em duas variaveis distintas e se o resto da divisao da primeira pela segunda for 1
escreva a soma dessas variaveis mais o resto da divisao; se for 2 escreva se o primeiro e o segundo valor
sao pares ou impares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
divida a soma dos numeros lidos pelo segundo, se este for diferente de zero. Em qualquer outra situacao
escreva o quadrado dos numeros lidos."""
def main():
valor1 = input ('Digite o primeiro valor: ')
valor2 = input ('\nDigite o segundo valor: ')

	if valor1 % valor2 == 1 :
		soma = valor1 + valor2
		resto = valor1 % valor2
		print ('\nA soma dos dois valores e %d e o resto da divisao e %d ') % (soma,resto)
	elif valor1 % valor2 == 2 : 
		if valor1 % 2 == 0 and valor2 % 2 == 0 :
			print ('\nO primeiro e o segundo numero sao pares ')
		elif valor1 % 2 == 1 and valor2 % 2 == 1 :
			print ('\nO primeiro e o segundo numero sao impares ')
		else :
		    if valor1 % 2 == 1 :
		    	print ('\nO primeiro numero e impar e o segundo numero e par ')
		    else :
		    	print ('\nO primeiro numero e par e o segundo numero e impar ')
	elif valor1 % valor2 == 3 :
		soma = valor1 + valor2
		multiplicacao = soma * valor1
		print ('\nA multiplicacao da soma dos numeros pelo primeiro numero e %d ') % (multiplicacao)
	elif valor1 % valor2 == 4 :
		soma = valor1 + valor2
		if valo2 != 0 :
			divisao = soma / valor2
			print ('\nA divisao da soma dos numeros pelo segundo numero e %d ') % (divisao)
	else :
		quadrado1 = valor1 ** 2 
		quadrado2 = valor2 ** 2
		print ('\nO quadrado do primeiro numero e %d e o quadrado do segundo numero e %d') % (quadrado1,quadrado2)
if __name__ == '__main__':
	main()
