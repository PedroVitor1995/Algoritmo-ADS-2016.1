dados = [8, 1, 5, 3, 4, 7, 6]
tam = len(dados)
for i in range(tam - 1):
	posicao_minimo = i
	for j in range(i+1, tam):
		if dados[j] < dados[posicao_minimo]:
			posicao_minimo = j
	dados[i], dados[posicao_minimo] = dados[posicao_minimo], dados[i]
