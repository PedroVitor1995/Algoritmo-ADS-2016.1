def main():
	numeros = [3,5,1,2,4]
	for i in range(1,len(numeros)):
		aux = numeros[i]
		j = i -1
		while j >= 0 and aux < numeros[j]:
			numeros[j+1] = numeros[j]
			j = j - 1
		numeros[j+1] = aux
	print(numeros)
if __name__ == '__main__':

	main()