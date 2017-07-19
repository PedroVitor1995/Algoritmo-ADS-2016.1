"""10. Leia 2 numeros inteiros, calcule e escreva o quociente e o resto da divisao do 1 pelo 2."""
def calcula_quociente(numero1,numero2):
	quociente = numero1 / numero2
	return quociente
def calcula_resto(numero1,numero2):
	resto = numero1 % numero2
	return resto
def main():
	numero1 = input ('Digite o primeiro numero inteiro: ')
	numero2 = input ('\nDigite o segundo numero inteiro: ')
	quociente = calcula_quociente(numero1,numero2)
	resto = calcula_resto(numero1,numero2)
	print quociente
	print resto
if __name__ == '__main__':
	main()