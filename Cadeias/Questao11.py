#__*__  encoding:utf8 __*__
"""11. Um dos recursos disponibilizados pelos editores de texto mais modernos é a contagem da quantidade de
palavras de um texto. Escreva um programa que determine o numero de palavras de um texto digitado."""
def main():
	texto = raw_input('Digite um texto: ')
	espaco = ' '
	quantidade_palavras = 1
	for letra in texto:
		if letra == espaco:
			quantidade_palavras += 1
	print quantidade_palavras
if __name__ == '__main__':
	main()