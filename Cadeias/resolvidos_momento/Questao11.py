#__*__  encoding:utf8 __*__
"""11. Um dos recursos disponibilizados pelos editores de texto mais modernos é a contagem da quantidade de
palavras de um texto. Escreva um programa que determine o numero de palavras de um texto digitado."""
def main():
	texto = raw_input('Digite um texto: ')
	texto = texto.split()
	quantidade_palavras = 0
	for i in range(len(texto)):
		quantidade_palavras = i + 1
	print quantidade_palavras
	# espaco = ' '
	# quantidade_palavras = 1
	# for local in espaco:
		# texto = texto.replace(espaco,'\n')
	# for local in texto:
		# if local == '\n':
			# quantidade_palavras += 1
	# print quantidade_palavras
if __name__ == '__main__':
	main()