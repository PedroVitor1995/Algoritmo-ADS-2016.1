def calcula_percentual(quantidade1,quantidade2):
	quantidade = quantidade1 + quantidade2
	percentual_palavra_nao_tem_e = (quantidade2 * 100) / float(quantidade)
	return percentual_palavra_nao_tem_e
def main():
	arquivo = open('words.txt')
	quantidade1 = 0
	quantidade2 = 0
	for linha in arquivo:
		palavra = linha.strip()
		if 'e' in palavra.lower():
			quantidade1 = quantidade1 + 1
		else:
			print palavra
			quantidade2 = quantidade2 + 1
	porcentagem_no_e = calcula_percentual(quantidade1,quantidade2)
	print('Porcentagem das palavras que nao tem e %.2f %%') % porcentagem_no_e		
if __name__ == '__main__':
	main()