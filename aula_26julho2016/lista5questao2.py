def main():
	frase = raw_input('Digite uma frase: ')

	for letra in frase:
		pass
		#if contar(frase, letra) > 1:
		#	print 'Tem letras repetidas'
		#	break

	for i in range(len(frase)):
		for j in range(i+1, len(frase)):
			#print 'par: ', frase[i], frase[j]
			if frase[i] == frase[j]:
				print 'Tem letras repetidas'




def contar(lista, item):
	contador = 0
	for i in lista:
		if i == item:
			contador += 1
	return contador


if __name__ == '__main__':
	main()