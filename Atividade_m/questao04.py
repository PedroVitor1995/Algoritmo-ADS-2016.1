def main():
	qtd_numeros = int(input())
	impares = []
	pares = []

	#Receber Valores ja separados
	for i in range(qtd_numeros):
		numero = int(input())
		if numero % 2 == 0:
			pares.append(numero)
		else:
			impares.append(numero)

	#Impares
	pares.sort()
	impares.sort(reverse=True)

	#imprimir valores
	for par in pares:
		print(par)

	for impar in impares:
		print(impar)

if __name__ == '__main__':
	main()