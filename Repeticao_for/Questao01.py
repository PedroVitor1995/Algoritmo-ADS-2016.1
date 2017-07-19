"""1. Leia N e escreva todos os numeros inteiros de 1 a N."""

def main():

	numero_n = input('Digite o valor de N: ')

	for i in range(1,numero_n+1):
		print i
		
if __name__ == '__main__':
	main()