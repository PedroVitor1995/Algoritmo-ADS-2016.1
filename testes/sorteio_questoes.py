from random import shuffle

def main():
	sorteio(25, 10)


def sorteio(qtd_itens, qtd_sorteio):
	lista = range(1, qtd_itens+1)
	shuffle(lista)
	print 'Questoes Sorteadas: '
	for i in range(qtd_sorteio):
		print "\t %d >> %d" % (i+1, lista.pop())


if __name__ == '__main__':
	main()