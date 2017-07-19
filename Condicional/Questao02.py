"""2. Leia 2 (dois) numeros, verifique e escreva o menor e o maior entre os numeros lidos."""
def maior_e_menor(numero1,numero2):
	maior = 10000000000
	menor = 0
	if numero1 < maior:
		menor = numero1
	if numero2 < menor:
		maior = menor
		menor = numero2
	else:
		maior = numero2
		menor = menor
	print('\nO maior numero eh %d ') % maior
	print('\nO menor numero eh %d ') % menor
def main():
	numero1 = input('Digite o primeiro numero: ')
	numero2 = input('\nDigite o segundo numero: ')
	maior_e_menor(numero1,numero2)
if __name__ == '__main__':
	main()
