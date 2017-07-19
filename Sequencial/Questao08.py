"""8. Leia 2 numeros, calcule e escreva a divisao da soma pela subtracao dos numeros lidos."""
def calcula_soma(numero1,numero2):
	soma = numero1 + numero2
	return soma
def calcula_subtracao(numero1,numero2):
	subtracao = numero1 - numero2
	return subtracao
def calcula_divisao(numero1,numero2):
	divisao = calcula_soma(numero1,numero2) / calcula_subtracao(numero1,numero2)
	return divisao
def main():
	numero1 = input ('Digite o primeiro numero: ')
	numero2 = input ('\nDigite o segundo numero: ')
	divisao = calcula_divisao(numero1,numero2)
	print divisao
if __name__ == '__main__':
	main()