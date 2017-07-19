def main():
	texto = raw_input('Frase: ')
	hist = histograma(texto)
	escrever_histograma(hist)

def escrever_histograma(histograma):
	print 'C --> O'
	for chave in histograma:
		print '%s --> %s' % (chave, histograma[chave])

def histograma(frase):
	frequencia = {}
	for letra in frase:
		if letra in frequencia:
			frequencia[letra] += 1
		else:
			frequencia[letra] = 1

	return frequencia

if __name__ == '__main__':
	main()