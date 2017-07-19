#__*__  encoding:utf8 __*__
"""8. Leia um numero X e, a seguir, leia e escreva uma lista de números com o término da lista ocorrendo
quando a soma de dois números consecutivos da lista for igual a X."""
def main():
	numer_x = input('Digite um numero X: ')
	soma = 0
	anterior = 0
	while True:
		lista_numero = input('Digite um numero: ')
		soma = anterior + lista_numero
		if soma == numer_x:
			break
		anterior = lista_numero
if __name__ == '__main__':
	main()