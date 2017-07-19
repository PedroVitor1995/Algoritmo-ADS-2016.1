"""18. Leia dois valores e uma das seguintes operacoes a serem executadas codificadas da seguinte forma: 1 
Adicao, 2  Subtracao, 3  Multiplicacao e 4 Divisao. Calcule e escreva o resultado dessa operacao
sobre os dois valores lidos."""
def main():
	numero1 = input ('Digite o primeiro numero: ')
	numero2 = input ('\nDigite o segundo numero: ')

	print ('Tipo da operacao 1 Adicao, 2 Subtracao, 3 Multiplicacao e 4 Divisao')

	tipo_operacao = input ('\nDigite o tipo de operaco a ser feita: ')

	if tipo_operacao == 1 :
		adicao = numero1 + numero2
		print ('\nA soma de %d + %d = %d ') % (numero1,numero2,adicao)
	elif tipo_operacao == 2 :
		subtracao = numero1 - numero2
		print ('\nA subtracao de %d - %d = %d ') % (numero1,numero2,subtracao)
	elif tipo_operacao == 3 :
		multiplicacao = numero1 * numero2
		print ('\nA multiplicacao de %d * %d = %d ') % (numero1,numero2,multiplicacao)
	elif tipo_operacao == 4 :
		numero1 = float(numero1)
		numero2 = float(numero2)
		divisao = float(numero1 / numero2)
		print ('\nA divisao de %.2f / %.2f = %.2f ') % (numero1,numero2,divisao)
	else :
		print ('\nO tipo de operacao nao existe')
if __name__ == '__main__':
	main()
