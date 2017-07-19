from util import has_no_e
def calcula_percentual(quantidade1,quantidade2):
	quantidade = quantidade1 + quantidade2
	percentual_palavra_nao_tem_e = (quantidade1 * 100) / float(quantidade2)
	return percentual_palavra_nao_tem_e
def main():
	arquivo = open('words.txt')
	quantidade1 = 0
	quantidade2 = 0
	for linha in arquivo:
		quantidade2 = quantidade2 + 1
		palavra = linha.strip()
		if has_no_e(palavra):
			quantidade1 = quantidade1 + 1
			print palavra
	porcentagem_no_e = calcula_percentual(quantidade1,quantidade2)
	print('Porcentagem das palavras que nao tem e %.2f %%') % porcentagem_no_e
if __name__ == '__main__':
	main()
