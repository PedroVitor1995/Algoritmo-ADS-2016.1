"""9. Leia 1 (um) numero entre 0 e 100, verifique e escreva se o numero e ou nao primo."""
from math import sqrt as raiz
def primo_ou_nao(numero,raiz_quadrada,quadrado_numero):
	if numero != 1 and quadrado_numero != numero :
		if numero == 2 or numero % 2 != 0 :
			if numero == 2 or numero % 3 != 0 or numero == 3 :
				if numero == 2 or numero % 5 != 0 or numero == 5 :
					if numero == 2 or numero % 7 != 0 or numero == 7 :
						if numero == 2 or numero % 9 != 0 :
							print ('\nO numero %d e primo ') % (numero)
						else :
							print ('\nO numero %d nao e primo ') % (numero)
					else :
						print ('\nO numero %d nao e primo ') % (numero)
				else :
					print ('\nO numero %d nao e primo ') % (numero)
			else :
				print ('\nO numero %d nao e primo ') % (numero)
		else :
			print ('\nO numero %d nao e primo ') % (numero)
	else :
		print ('\nO numero %d nao e primo ') % (numero)
def main():
	numero = input ('Digite um numero inteiro: ')
	raiz_quadrada = raiz (numero)
	raiz_quadrada = int (raiz_quadrada)
	quadrado_numero = raiz_quadrada ** 2
	primo_ou_nao(numero,raiz_quadrada,quadrado_numero)

if __name__ == '__main__':
	main()





			


