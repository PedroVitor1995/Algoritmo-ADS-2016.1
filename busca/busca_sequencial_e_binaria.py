# -*- coding: utf-8 -*-
import random
import time
import sys

def main():

	dados = [random.randint(1,100) for i in range(int(sys.argv[1]))]
	

	#sequencial
	item = random.choice(dados)
	retorno = busca_sequencia(dados, item)

	print '  *** Busca Sequencial ***'
	print 'Dados: ', dados
	if retorno:
		print 'Valor %d encontrado na posicao %d' % (item, retorno)
	else:
		print 'Item %d não localizado na lista' % item

	#binária
	retorno = busca_binaria(dados, item)
	dados.sort()
	print '\n  *** Busca Binária ***'
	print 'Dados: ', 
	if retorno:
		print 'Valor %d encontrado na posicao %d' % (item, retorno)
	else:
		print 'Item %d não localizado na lista' % item


def busca_sequencia(lista, item_buscado):

	#tradicional
	for i in range(len(lista)):
		if lista[i] == item_buscado:
			return i+1

	return None

def busca_binaria(lista, item_buscado):
	lista.sort()
	inicio = 0
	fim = len(lista) - 1
	
	while inicio <= fim:
		meio = (fim + inicio) / 2
		
		if lista[meio] == item_buscado:
			return meio + 1
			
		#ajustar inicio, meio e fim
		if item_buscado < lista[meio]:
			fim = meio - 1
		else:
			inicio = meio + 1

	return None


if __name__ == '__main__':
	main()