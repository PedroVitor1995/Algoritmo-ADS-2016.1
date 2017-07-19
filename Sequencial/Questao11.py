"""11. Leia um numero inteiro (3 digitos) e escreva o inverso do numero. (Ex.: numero = 532 ; inverso = 235)"""
def calcula_inverso(numero):
	numero1 = str(numero / 100)
	numero2 = str((numero % 100) /10)
	numero3 = str(numero % 10)
	inverso_numero = str (numero3 + numero2 + numero1)
	inverso_numero = int(inverso_numero)
	return inverso_numero
def  main():
	numero = input ('Digite um numero inteiro (3 digitos): ')
	inverso_numero = calcula_inverso(numero)
	print inverso_numero
if __name__ == '__main__':
	main()