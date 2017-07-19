#__*__  encoding:utf8 __*__
"""5. Leia uma data no formato DD/MM/AAAA e escreva o mês por extenso (DD de mês de AAAA)."""
def main():
	data = raw_input('Digite uma data no formato (DD/MM/AAAA): ')
	for i in range(len(data)):
		dia = data[0] + data[1]
		mes = data[3] + data[4]
		ano = data[6] + data[7] + data[8] + data[9]
	if mes == '01':
		data = dia + " de Janeiro de " + ano
		print data
	elif mes == '02':
		data = dia + " de Fevereiro de " + ano
		print data
	elif mes == '03':
		data = dia + " de Marco de " + ano
		print data
	elif mes == '04':
		data = dia + " de Abril de " + ano
		print data
	elif mes == '05':
		data = dia + " de Maio de " + ano
		print data
	elif mes == '06':
		data = dia + " de Junho de " + ano
		print data
	elif mes == '07':
		data = dia + " de julho de " + ano
		print data
	elif mes == '08':
		data = dia + " de Agosto de " + ano
		print data
	elif mes == '09':
		data = dia + " de Setembro de " + ano
		print data
	elif mes == '10':
		data = dia + " de Outubro de " + ano
		print data
	elif mes == '11':
		data = dia + " de Novembro de " + ano
		print data
	elif mes == '12':
		data = dia + " de Dezembro de " + ano
		print data
if __name__ == '__main__':
	main()