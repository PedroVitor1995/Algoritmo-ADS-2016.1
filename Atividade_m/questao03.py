def main():
	qtd_numeros = int(input())
	vetor_numeros = [0] * qtd_numeros

	qtd_impares = 0
	qtd_pares = 0

	#Receber valores e contar impares e pares
	for i in range(qtd_numeros):
		vetor_numeros[i] = int(input())
		if vetor_numeros[i] % 2 == 0:
			qtd_pares += 1
		else:
			qtd_impares += 1

	#Vetores para guardar impares e pares separadamente
	impares = [0] * qtd_impares
	index_impar = 0
	pares = [0] * qtd_pares
	index_par = 0

	#Separar impares e pares em vetores distintos
	for i in range(qtd_numeros):
		if vetor_numeros[i] % 2 != 0:
			impares[index_impar] = vetor_numeros[i]
			index_impar += 1
		else:
			pares[index_par] = vetor_numeros[i]
			index_par += 1

	#Ordernar Pares crescentemente e impares decrescentemente.
	select_crescente(pares)
	select_decrescente(impares)

	#imprimir valores
	for par in pares:
		print(par)

	for impar in impares:
		print(impar)

def select_crescente(conjunto):
	""" Troca o primeiro elemento nao ordenado pelo menor valor entre o nao-ordenados """

	for i in range(len(conjunto) - 1):
		pos_menor = i # primeiro valor nao ordenado

		for j in range(i + 1, len(conjunto)):
			if conjunto[j] < conjunto[pos_menor]:
				pos_menor = j

		#tuple swap
		conjunto[i], conjunto[pos_menor] = conjunto[pos_menor], conjunto[i]


def select_decrescente(conjunto):
	""" Troca o primeiro elemento nao ordenado pelo menor valor entre o nao-ordenados """

	for i in range(len(conjunto) - 1):
		pos_menor = i # primeiro valor nao ordenado

		for j in range(i + 1, len(conjunto)):
			if conjunto[j] > conjunto[pos_menor]:
				pos_menor = j

		#tuple swap
		conjunto[i], conjunto[pos_menor] = conjunto[pos_menor], conjunto[i]



if __name__ == '__main__':
	main()