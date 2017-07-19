

def main():

	while True:

		linhas, colunas = [int(i) for i in input().split(' ')]
		if linhas == 0: break

		imagem = [input() for i in range(linhas)]		

		n_linhas, n_colunas = [int(i) for i in input().split(' ')]

		for linha in imagem:
			nova_linha = ''.join([caractere * (n_colunas // colunas) for caractere in linha])
			[print(nova_linha) for i in range(n_linhas // linhas)]

		print()


if __name__ == '__main__':
	main()