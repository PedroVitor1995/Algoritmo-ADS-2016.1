def principal():
	multiplos(4, 1)

def multiplos(numero, qtd):
	while qtd <= 10:
		mult = numero * qtd
		print 'M = %d' % mult
		qtd = qtd + 1


if __name__ == '__main__':
	principal()