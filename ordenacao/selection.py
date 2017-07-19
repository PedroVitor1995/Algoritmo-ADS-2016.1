def main():
	numeros = [3,5,1,2,4]
	for i in range(len(numeros)):
		menor = i
		for j in range(len(numeros)-1):
			if numeros[j] > numeros[menor]:
				menor = j
		numeros[menor], numeros[i] = numeros[i], numeros[menor]
	print(numeros)	
if __name__ == '__main__':
	main()