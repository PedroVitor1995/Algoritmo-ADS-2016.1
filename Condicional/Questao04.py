"""4. Leia 1 (um) numero de 2 (dois) digitos, verifique e escreva se o algarismo da dezena e igual ou diferente
do algarismo da unidade."""
def igual_ou_diferente(numero,dezena,unidade):
	if dezena == unidade :
		print ('\nO algarismo da dezena e igual ao algarismo da unidade')
	else :
		print ('\nO algarismo da dezena e diferente do algarismo da unidade')
def main():
	numero = input ('Digite 1 (um) numero de 2 (dois) digitos: ')
	dezena = numero / 10
	unidade = numero % 10
	igual_ou_diferente(numero,dezena,unidade)
if __name__ == '__main__':
	main()


