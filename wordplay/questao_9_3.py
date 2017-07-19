from util import avoids


def main():
	arquivo = open('words.txt')
	contator_geral = 0
	contator_avoids = 0

	letras_indesejadas = raw_input('Letras Proibidas: ')


	for linha in arquivo:
		contator_geral += 1
		palavra = linha.strip()
		if avoids(palavra, letras_indesejadas):
			contator_avoids += 1
			print palavra

	print 'Qtd Palavras LIMPAS: %d' % contator_avoids






if __name__ == '__main__':
	main()