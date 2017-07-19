def main():
	primeira_nota = float(input('Nota 1: '))
	segunda_nota = float(input('Nota 2: '))

	media = (primeira_nota + segunda_nota) / 2

	if media < 7.0:
		print 'REPROVADO.'
	elif media < 10.0:
		print 'APROVADO'
	else:
		print 'APROVADO COM DISTINCAO'

if __name__ == '__main__':
	main()