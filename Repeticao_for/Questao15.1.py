#__*__  encoding:utf8 __*__
"""15. Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...)."""
#usando recursividade
def sequencia(numero_n,contador,termos):
	if contador <= numero_n:
		termos += contador
		contador += 1
		print termos
		sequencia(numero_n,contador,termos)
def main():
	numero_n = input('Digite a quantidade de N: ')
	contador = 1
	termos = 0
	sequencia(numero_n,contador,termos)
if __name__ == '__main__':
	main()