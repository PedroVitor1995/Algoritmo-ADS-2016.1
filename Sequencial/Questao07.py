"""7. Leia 3 numeros, calcule e escreva a soma dos 2 primeiros e a diferenca entre os 2 ultimos."""
def calcula_soma(numero1,numero2):
	soma = numero1 + numero2
	return soma
def calcula_diferenca(numero2,numero3):
	diferenca = numero2 - numero3
	return diferenca
def main():
	numero1 = input ('Digite o primeiro numero: ')
	numero2 = input ('\nDigite o segundo numero: ')
	numero3 = input ('\nDigite o terceiro numero: ')
	soma = calcula_soma(numero1,numero2)
	diferenca = calcula_diferenca(numero2,numero3)
	print soma
	print diferenca
if __name__ == '__main__':
	main()