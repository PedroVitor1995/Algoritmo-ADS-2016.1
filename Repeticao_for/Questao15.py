"""15. Leia N, calcule e escreva os N primeiros termos de sequencia (1, 3, 6, 10, 15,...)."""

def main():

	numero_n = input('Digite o valor de N: ')

	sequencia = 0

	for i in range(1,numero_n+1):
		sequencia = sequencia + i 
		print sequencia

if __name__ == '__main__':
	main()