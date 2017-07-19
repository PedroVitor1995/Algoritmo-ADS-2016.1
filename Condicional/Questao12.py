"""12. Leia 1 (um) numero inteiro e escreva se este numero e par ou impar."""
def par_ou_impar(numero):
	if numero % 2 == 0 :
		print ('\nO numero e par ')
	else :
		print ('\nO numero e impar')
def main():
	numero = input ('Digite um numero inteiro: ')
	par_ou_impar(numero)
if __name__ == '__main__':
	main()


