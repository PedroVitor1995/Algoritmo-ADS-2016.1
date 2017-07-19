def main():
	quantidade_casos = int(input('Quantidade de casos: '))
	for i in range(quantidade_casos):
		quantidade_pessoas = int(input('Quantidade de pessoas: '))
		pessoas = []
		for j in range(quantidade_pessoas):
			pessoas.append(input('Idioma nativo: '))
		quantidade_pessoas_diferentes = 0
		pessoa = pessoas[0]
		for k in range(quantidade_pessoas):
			if pessoa != pessoas[k]:
				pessoa = pessoas[k]
				quantidade_pessoas_diferentes += 1
		if quantidade_pessoas_diferentes == 0:
			print(pessoa)
		else:
			print('ingles')
		quantidade_pessoas_diferentes = 0
if __name__ == '__main__':
	main()