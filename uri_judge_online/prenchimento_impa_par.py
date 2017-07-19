def main():

	impares = []
	pares = []

	for i in range(15):
		numero = input()
		if numero % 2 == 0:
			pares.append(numero)
			if (len(pares) == 5):
				escrever(pares, 'par')
				pares = []
		else:
			impares.append(numero)
			if (len(impares) == 5):
				escrever(impares, 'impar')
				impares = []

	
	escrever(impares, 'impar')
	escrever(pares, 'par')

def escrever(lista, texto):
	for i in range(len(lista)):
		print '%s[%d] = %d' % (texto, i, lista[i])

if __name__ == '__main__':
	main()