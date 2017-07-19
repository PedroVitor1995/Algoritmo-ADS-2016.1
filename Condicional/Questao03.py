"""Leia 3 (tres) numeros, verifique e escreva o maior entre os numeros lidos."""
def maior(numero1,numero2,numero3):
	if numero1 > numero2 and numero1 > numero3 :
		print ('\nO maior numero e %d ') % (numero1)
	elif numero2 > numero1 and numero2 > numero3 :
		print ('\nO maior numero e %d ') % (numero2)
	else :
		print ('\nO maior numero e %d ') % (numero3)
def main():
	numero1 = input ('Digite o primeiro numero: ')
	numero2 = input ('\nDigite o segundo numero: ')
	numero3 = input ('\nDigite o terceiro numero: ')
	maior(numero1,numero2,numero3)
if __name__ == '__main__':
	main()