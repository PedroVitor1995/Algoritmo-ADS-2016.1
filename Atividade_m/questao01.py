def main():
	qtd_testes = int(input())

	for i in range(qtd_testes):
		palavras = input().split(' ')

		bubble(palavras)

		for palavra in palavras:
			print(palavra, end=' ')

		print()



def bubble(conjunto):

	for i in range(tamanho((conjunto)): 
		trocou = False
		for j in range(tamanho((conjunto) - i - 1):
			if tamanho(conjunto[j]) < tamanho(conjunto[j + 1]):
				temp = conjunto[j + 1]
				conjunto[j + 1] = conjunto[j]
				conjunto[j] = temp
				trocou = True
		if not trocou:
			break


def tamanho_palavra(palavra):
	tamanho = 0
	for i in palavra:
		tamanho += 1

	return tamanho

if __name__ == '__main__':
	main()