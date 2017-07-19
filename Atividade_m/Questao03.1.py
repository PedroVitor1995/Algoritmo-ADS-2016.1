def main():
	quantidade_linhas = int(input('Quantidade de linhas: '))
	numeros = [0] * quantidade_linhas
	par = ''
	impar = ''
	qtd_par = 0
	qtd_impar = 0
	for i in range(quantidade_linhas):
		numeros[i] = int(input('Numero: '))
	for i in range(quantidade_linhas):
		if numeros[i] % 2 == 0:
			par += (str(numeros[i]) + ' ')
			qtd_par += 1
		else:
			impar += (str(numeros[i]) + ' ')
			qtd_impar += 1
	par = par.strip().split(' ')
	impar = impar.strip().split(' ')
	pares = [0] * qtd_par
	for i in range(qtd_par):
		pares[i] = int(par[i])
	impares = [0] * qtd_impar
	for j in range(qtd_impar):
		impares[j] = int(impar[j])
	for i in range(qtd_par):
		aux = i
		for j in range(qtd_par-1):
			if pares[j] >= pares[aux]:
				aux = j
			pares[aux], pares[i] = pares[i], pares[aux]
	for j in range(qtd_impar):
		aux = j
		for c in range(qtd_impar-1):
			if impares[c] <= impares[aux]:
				aux = c
			impares[aux], impares[j] = impares[j], impares[aux]
	conjunto = pares + impares
	for i in range(quantidade_linhas):
		print(conjunto[i])
if __name__ == '__main__':
	main()