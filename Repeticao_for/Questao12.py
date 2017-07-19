"""12. Leia N e uma lista de N numeros e escreva a soma e a media de todos os numeros da lista."""
def calcula_media(soma,quantidade_numeros):
	media = soma / float(quantidade_numeros)
	return media
def main():

	numero_n = input('Digite o valor de N: ')

	soma = 0
	quantidade_numeros = 0

	for i in range(1,numero_n+1):
		lista_numero_n = input('Digite um numero: ')

		soma = soma + lista_numero_n
		quantidade_numeros = quantidade_numeros + 1
	media = calcula_media(soma,quantidade_numeros)
	print('A soma dos numero eh %d ') % soma
	print('A media dos numeros eh %.1f ') % media

if __name__ == '__main__':
	main()