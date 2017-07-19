def main():
	numeros = [3,5,1,2,4]
	for i in range(len(numeros)-1):
		for j in range(len(numeros)-1):
			if numeros[j] > numeros[j + 1]:
				aux = numeros[j]
				numeros[j] = numeros[j+1]
				numeros[j+1] = aux
	print(numeros)

if __name__ == '__main__':
	main()