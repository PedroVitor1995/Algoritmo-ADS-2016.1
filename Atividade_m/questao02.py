def main():
	qtd_testes = int(input())

	for i in range(qtd_testes):
		palavras = input().split(' ')

		palavras.sort(reverse=True, key=len)

		for palavra in palavras:
			print(palavra, end=' ')

		print()


if __name__ == '__main__':
	main()