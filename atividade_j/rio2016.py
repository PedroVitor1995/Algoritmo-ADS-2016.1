from consultas import consultas
from medalhas import *


def main():
	cabecalho = '\n   ****** SIS - RIO 2016 ***** \n\n'
	menu = ''' 1 - Nova Medalha \n 2 - Listar Todas Medalha \n 3 - Remover Medalha 
 4 - Consultas Estatisticas \n 0 - Sair \n\n opcao >>> '''

	paises = inicializar_paises()
	medalhas = inicializar_medalhas()

	while True:
		opcao = input(cabecalho + menu)

		if opcao == 0:
			finalizar(paises, medalhas)
			break
		elif opcao == 1:
			medalha = nova_medalha(paises)
			medalhas.append(medalha)
		elif opcao == 2:
			lista_todas_medalhas(medalhas, paises)
		elif opcao == 3:
			remover_medalha(medalhas, paises)
		elif opcao == 4:
			consultas(medalhas, paises)
		else:
			print "Opcao invalida"


def inicializar_paises():
	arq_paises = open('paises.txt', 'r')
	dados = arq_paises.readlines()
	paises = []
	codigo = 1
	
	if (len(dados) == 0): #importar
		arq_paises_importacao = open('paises_importacao.txt', 'r')
		for linha in arq_paises_importacao:
			temp = linha.strip().split('-')
			pais = {'id': codigo,'nome': temp[0], 'continente': temp[1], 'populacao': int(temp[2]), 'atletas': int(temp[3])}
			codigo += 1
			paises.append(pais)
		arq_paises_importacao.close()
		return paises

	else: #carregar paises em memoria
		arq_paises.seek(0)
		for linha in arq_paises:
			paises.append(eval(linha))
		return paises


def inicializar_medalhas():
	arq_medalhas = open('medalhas.txt', 'r')
	medalhas = []
	for linha in arq_medalhas:
		medalhas.append(eval(linha))

	arq_medalhas.close()
	return medalhas

def finalizar(paises, medalhas):
	# Gravar Paises
	arq_paises = open('paises.txt', 'w')
	for pais in paises:
		arq_paises.write(str(pais) + '\n')

	arq_paises.close()

	#Gravar Medalhas
	arq_medalhas = open('medalhas.txt', 'w')
	for medalha in medalhas:
		arq_medalhas.write(str(medalha) + '\n')

	arq_medalhas.close()


if __name__ == '__main__':
	main()
