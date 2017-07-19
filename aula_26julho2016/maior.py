def main():
	numeros = [int(i) for i in raw_input().split()]
	print 'maior: ', maior(numeros)

def maior(lista):
	maior = lista[0]
	for i in range(1, len(lista)):
		if lista[i] > maior:
			maior = lista[i]
	return maior


if __name__ == '__main__':
	main()