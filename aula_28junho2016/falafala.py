def escreva(palavra, vezes=3):
	if vezes == 0:
		print 'Trabalho feito.'
	else:
		print palavra
		escreva(palavra, vezes-1)

if __name__ == '__main__':
	escreva('WD', 12)
	escreva('Erico')
	escreva('Fabiano', vezes=1)