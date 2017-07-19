# *-* coding: utf-8 *-*
import random
import time
import sys

def main():

	size = int(sys.argv[1])

	dados = [random.randint(0, 10000) for i in range(size)]
	

	#print 'Dados:     ', dados
	inicio = time.time()
	dados.sort()
	#print 'list.sort: ', dados
	fim = time.time()
	print 'listsort-Tempo: %fs' % (fim - inicio)

	random.shuffle(dados)
	inicio = time.time()
	bubble(dados)
	#print 'Bubble:    ', dados
	fim = time.time()
	print 'bubble - Tempo: %fs' % (fim - inicio)

	
	random.shuffle(dados)
	inicio = time.time()
	bubble_while(dados)
	#print 'Bubble2:   ', dados
	fim = time.time()
	print 'bubble2- Tempo: %fs' % (fim - inicio)

	random.shuffle(dados)
	inicio = time.time()
	select(dados)
	#print 'Select:    ', dados
	fim = time.time()
	print 'select - Tempo: %fs' % (fim - inicio)

	random.shuffle(dados)
	inicio = time.time()
	insert(dados)
	#print 'Insert:    ', dados
	fim = time.time()
	print 'insert - Tempo: %fs' % (fim - inicio)



def bubble(conjunto):

	for i in range(len(conjunto)): # qtd max de Execucoes é a qtd de elementos
		trocou = False
		for j in range(len(conjunto) - i - 1): # de Zero ate a Posicao nao ordenada
			if conjunto[j] > conjunto[j + 1]:
				temp = conjunto[j + 1]
				conjunto[j + 1] = conjunto[j]
				conjunto[j] = temp
				trocou = True
		if not trocou:
			break


def bubble_while(conjunto):

	""" Faz flutuar o maior para valor para final da lista, 
	comparando os pares 1 a 1 (vizinho a vizinho), pára ao realizar uma rodada sem troca """

	ultima_pos_nao_ordenada = len(conjunto)
	while True:
		fez_troca = False
		for j in range(ultima_pos_nao_ordenada - 1): # de Zero ate a Posicao nao ordenada
			if conjunto[j] > conjunto[j + 1]:
				temp = conjunto[j + 1]
				conjunto[j + 1] = conjunto[j]
				conjunto[j] = temp
				fez_troca = True
		
		ultima_pos_nao_ordenada -= 1
		if not fez_troca:
			break


def select(conjunto):
	""" Troca o primeiro elemento nao ordenado pelo menor valor entre o nao-ordenados """

	for i in range(len(conjunto) - 1):
		pos_menor = i # primeiro valor nao ordenado

		for j in range(i + 1, len(conjunto)):
			if conjunto[j] < conjunto[pos_menor]:
				pos_menor = j

		#tuple swap
		conjunto[i], conjunto[pos_menor] = conjunto[pos_menor], conjunto[i]


def insert(conjunto):

	for i in range(1, len(conjunto)):
		extraido = conjunto[i]
		for j in range(i - 1, -1, -1):
			atual = conjunto[j]
			if (atual > extraido): # quem vai para j+1 Eu(extrado) ou o J ?
				conjunto[j + 1] = atual
				if (j == 0): # o primeiro elemento for maior que Eu (extraido) entao vou para a pos 0
					conjunto[0] = extraido
			else:
				conjunto[j + 1] = extraido
				break	# Se achei minha posicao, pode interromper o for-j
				

if __name__ == '__main__':
	main()







