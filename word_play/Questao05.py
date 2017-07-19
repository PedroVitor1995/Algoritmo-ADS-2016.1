from util import uses_all
def main():
	letras = raw_input('Letras: ')
	arquivo = open('words.txt')
	contador_all = 0

	for linha in arquivo:
		palavra = linha.strip()
		if uses_all(palavra, letras):
			contador_all += 1
			print palavra

	print 'Qtd palavras: %d' % contador_all
	
if __name__ == '__main__':
	main()