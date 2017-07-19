"""11. Leia LimiteSuperior e LimiteInferior e escreva todos os numeros primos entre os limites lidos."""

from math import sqrt as raiz
def main():
	limite_inferior = input('Digite o limite inferior: ')
	limite_superior = input('\nDigite o limite superior: ')

	print('Os numeros primos entre %d e %d ') % (limite_inferior,limite_superior)

	fim = limite_superior

	for i in range(1, fim + 1):

		raiz_quadrada = raiz (i)
		raiz_quadrada = int (raiz_quadrada)
		quadrado_numero = raiz_quadrada ** 2

		if i > limite_inferior and i < limite_superior:
			if i != 1 and quadrado_numero != i :
				if i == 2 or i % 2 != 0 :
					if i == 2 or i % 3 != 0 or i == 3 :
						if i == 2 or i % 5 != 0 or i == 5 :
							if i == 2 or i % 7 != 0 or i == 7 :
								if i == 2 or i % 9 != 0 :
									print i
if __name__ == '__main__':
	main()
					

