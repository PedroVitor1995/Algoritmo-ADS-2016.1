from util import avoids
def main():
	arquivo = open('words.txt')
	contador_avoids = 0
	letras_proibidas = raw_input('Letras proibidas: ')
	for linha in arquivo:
		palavra = linha.strip()
		if avoids(palavra,letras_proibidas):
			contador_avoids += 1
	print('Quantidade de palavras que nao tem qualquer uma das letras proibidas %d ') % contador_avoids
if __name__ == '__main__':
	main()