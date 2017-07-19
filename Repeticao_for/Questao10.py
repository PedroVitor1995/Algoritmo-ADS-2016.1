"""10. Leia LimiteSuperior e LimiteInferior e escreva todos os numeros impares entre os limites lidos."""
def main():
	limite_inferior = input('Digite o limite inferior: ')
	limite_superior = input('\nDigite o limite superior: ')

	print('\nOs numero impares entre %d e %d ') % (limite_inferior,limite_superior)

	fim = limite_superior

	for i in range(1, fim + 1):

		if i % 2 != 0:
			if i > limite_inferior and i < limite_superior:
				print i
if __name__ == '__main__':
	main()