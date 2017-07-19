from util import has_no_e


def main():
	arquivo = open('words.txt')
	contator_geral = 0
	contator_has_no_e = 0
	
	for linha in arquivo:
		contator_geral += 1
		palavra = linha.strip()
		if has_no_e(palavra):
			contator_has_no_e += 1
			print palavra

	percentual_has_no_e = (contator_has_no_e / float(contator_geral)) * 100
	print 'Percentual HAS_NO_E: %.2f %% (de %d)' % (percentual_has_no_e, contator_geral)


if __name__ == '__main__':
	main()