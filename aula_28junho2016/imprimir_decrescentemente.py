def imprimir(numero):
	print 'begin', numero
	if numero == 0:
		print 'FIM'
	else:
		print numero
		numero = numero - 1
		imprimir(numero)
	print 'end', numero

if __name__ == '__main__':
	imprimir(10)