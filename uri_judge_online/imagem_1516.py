

def main():

	while True:

		linhas, colunas = [int(i) for i in input().split(' ')]

		if linhas == 0: break

		imagem = []

		for i in range(linhas):
			imagem.append(input())

		n_linhas, n_colunas = [int(i) for i in input().split(' ')]
		
		for linha in imagem:
			## Qtd Vezes cada linha se repetirá?
			for i in range((n_linhas // linhas)): 
				nova_linha = ''
				# Qtd Vezes cada caractere da linha se repetirá
				for caractere in linha:
					nova_linha += caractere * (n_colunas // colunas) 
				print(nova_linha)

		print()


if __name__ == '__main__':
	main()