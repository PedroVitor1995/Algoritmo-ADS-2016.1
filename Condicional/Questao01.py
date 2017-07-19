"""1. Leia 3 (tres) numeros, verifique e escreva quantos numeros iguais existem entre os numeros."""
def iguais_ou_diferentes(numero1,numero2,numero3):
	if numero1 == numero2 and numero1 == numero3 and numero2 == numero3:
	 	print ('\nTem tres numeros sao iguais ')
	elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
		print ('\nTem dois numero iguais')
	else :
		print('\nTodos os numeros sao diferentes')
def main():
	numero1 = input ('Digite o primeiro numero: ')
	numero2 = input ('\nDigite o segundo numero: ')
	numero3 = input ('\nDigite o terceiro numero: ')
	iguais_ou_diferentes(numero1,numero2,numero3)
if __name__ == '__main__':
	main()