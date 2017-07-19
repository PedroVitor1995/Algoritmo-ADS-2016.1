"""10. Leia uma data (dia, mes e ano), verifique e escreva se a data e ou nao valida."""
def data_valida(dia,mes,ano):
	if dia >= 1 and dia <= 30 and mes >= 1 and mes <= 12 and ano > 0 :
		print ('\nData valida ')
	else :
		print('\nData invalida ')
def main():
	dia,mes,ano = input ('Dia: '),input('\nMes: '),input('\nAno: ')
	data_valida(dia,mes,ano)
if __name__ == '__main__':
	main()