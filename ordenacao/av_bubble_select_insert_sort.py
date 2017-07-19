import random
import time
import sys

def main():

	dados = range(sys.argv[1])
	random.shuffle(dados)
	dados2 = list(dados)
	dados3 = list(dados)
	dados4 = list(dados)
	#print 'Dados: ', dados
	'''
	inicio = time.time()
	dados.sort()
	fim = time.time()
	#print 'PySort: ', dados
	print 'Time PySort: %fs' % (fim - inicio) 
	'''
	inicio = time.time()
	bubble(dados2)
	fim = time.time()

	#print 'Bubble: ', dados2
	print 'Time Bubble: %fs' % (fim - inicio) 
'''
	inicio = time.time()
	bubble2(dados3)
	fim = time.time()

	#print 'Bubble: ', dados2
	print 'Time Bubble2: %fs' % (fim - inicio)

	inicio = time.time()
	select(dados4)
	fim = time.time()

	print 'dados: ', dados
	print 'select: ', dados4
	print 'Time Select: %fs' % (fim - inicio)
'''

def bubble(dados):

	for i in range(len(dados) - 1, 0, -1): # qtd vezes
		for j in range(i):
			if dados[j] > dados[j + 1]:
				aux = dados[j+1]
				dados[j + 1] = dados[j] 
				dados[j] = aux

def bubble2(dados):

	for i in range(len(dados) - 1, 0, -1): # qtd vezes
		fez_trocas = False
		for j in range(i):
			if dados[j] > dados[j + 1]:
				aux = dados[j+1]
				dados[j + 1] = dados[j] 
				dados[j] = aux
				fez_trocas = True
		if not fez_trocas:
			break

def select(dados):

	
	for i in range(len(dados) - 1):
		pos_menor = i
		for j in range(i + 1, len(dados)):
			if dados[j] < dados[pos_menor]:
				pos_menor = j
		dados[i], dados[pos_menor] = dados[pos_menor], dados[i]




if __name__ == '__main__':
	main()











