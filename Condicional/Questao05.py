"""5. Leia 3 (tres) numeros e escreva-os em ordem crescente."""
def ordem_crescente(numero1,numero2,numero3):
	if numero1 != numero2 and numero1 != numero2 and numero2 != numero3:
		if numero1 < numero2 and numero1 < numero3 and numero2 < numero3:
			print('A ordem crescente dos numeros eh %d %d %d ') % (numero1,numero2,numero3)
		elif numero2 < numero1 and numero2 < numero3 and numero1 < numero3:
			print('A ordem crescente dos numeros eh %d %d %d ') % (numero2,numero1,numero3)
		elif numero3 < numero1 and numero3 < numero2 and numero2 < numero1:
			print('A ordem crescente dos numeros eh %d %d %d ') % (numero3,numero2,numero1)
		elif numero1 < numero2 and numero1 < numero3 and numero2 > numero3:
			print('A ordem crescente dos numeros eh %d %d %d ') % (numero1,numero3,numero2)
		elif numero2 < numero1 and numero2 < numero3 and numero1 > numero3:
			print('A ordem crescente dos numeros eh %d %d %d ') % (numero2,numero3,numero1)
		elif numero3 < numero1 and numero3 < numero2 and numero2 > numero1:
			print('A ordem crescente dos numeros eh %d %d %d ') % (numero3,numero1,numero2)
	else:
		print('Existe numeros iguais')
def main():
	numero1 = input('Digite o primeiro numero: ')
	numero2 = input('Digite o segundo numero: ')
	numero3 = input('Digite o terceiro numero: ')
	ordem_crescente(numero1,numero2,numero3)
if __name__ == '__main__':
	main()